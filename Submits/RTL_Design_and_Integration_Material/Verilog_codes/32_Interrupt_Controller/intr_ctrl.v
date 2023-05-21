module intr_ctrl(
	// processor
	pclk_i, 
	prst_i,
	paddr_i,
	pwdata_i, // [3:0] is sufficient to store priority of all  16 regs
	prdata_o, 
	pwrite_i, 
	penable_i, 
	pready_o, 
	intr_to_service_o, 
	intr_valid_o,
	intr_serviced_i,

	// peripherals
	intr_active_i
	);
	
	parameter NUM_INTR = 16; // Number of peripherals
	parameter S_NO_INTR = 3'b001, S_INTR_ACTIVE = 3'b010, S_INTR_GIVEN_WAIT_FOR_SERVICE = 3'b100;
	integer i;	
	
	input pclk_i;
	input prst_i;
	input [7:0] paddr_i;
	input [7:0] pwdata_i; // [3:0] is sufficient to store priority of all the 16 registers
	input pwrite_i; // write = 1, read = 0
	input penable_i; 
	input intr_serviced_i;
	output reg [7:0] prdata_o; 
	output reg pready_o; 
	output reg [3:0] intr_to_service_o; 
	output reg intr_valid_o;
	

	// Peripheral Controllers
	input [NUM_INTR-1:0] intr_active_i;	
	// Registers
	reg [7:0] priority_regA[NUM_INTR-1:0]; // Note here that to store the priority of 16 register 4 bits are sufficient 
	// hence reg [3:0] priority_regA[NUM_INTR-1:0] could be used but as we have declared data [7:0] pwdata_i we are 
	// also declaring the registers as 8 bits
	reg [2:0] state, next_state;
	reg first_match_f;
	reg [3:0] cur_high_prio;
	reg [3:0] intr_with_high_prio;

	// register programming 
	always @(posedge pclk_i) begin 
		if (prst_i == 1) begin 
			prdata_o = 0;
			pready_o = 0;
			intr_to_service_o = 0;
			intr_valid_o = 0;
			state = S_NO_INTR;
			next_state = S_NO_INTR;			
			for (i = 0; i < NUM_INTR; i=i+1) begin 
				priority_regA[i] = 0; // reset priority register
			end 
			first_match_f = 1;
			cur_high_prio = 0;
			intr_with_high_prio = 0;
		end 
		else begin 
			if (penable_i == 1) begin 
				pready_o = 1; // behavior of if you're ready then I am also
				if (pwrite_i == 1) begin 
					priority_regA[paddr_i] = pwdata_i;
				end 
				else begin 
					prdata_o = priority_regA[paddr_i];
				end
			end 
			else begin 
				pready_o = 0;
			end
		end 
	end 	
	
	// interrupt handling 
	always @(posedge pclk_i) begin 
		if (prst_i != 1) begin 
			case (state) 
				S_NO_INTR: begin 
					if (intr_active_i != 0) begin
						next_state = S_INTR_ACTIVE;
						first_match_f = 1;
					end 
				end
				S_INTR_ACTIVE: begin 
					// get the highest priority interrupt among all active interrupts,
					// give it to the processor then jump to next state
					for (i = 0; i < NUM_INTR; i=i+1) begin 
						if (intr_active_i[i] == 1) begin 
							if (first_match_f == 1) begin 
								cur_high_prio = priority_regA[i];
								intr_with_high_prio = i;
								first_match_f = 0;
							end 
							else begin 
								if (cur_high_prio < priority_regA[i]) begin 
									cur_high_prio = priority_regA[i];
									intr_with_high_prio = i;
								end
							end 
						end 	
					end
					// cur_high_prio and intr_with_high_prio will be available
					intr_to_service_o = intr_with_high_prio;
					intr_valid_o = 1'b1;
					next_state = S_INTR_GIVEN_WAIT_FOR_SERVICE;
					// give it to the processor, then jump to next state
				end
				S_INTR_GIVEN_WAIT_FOR_SERVICE: begin // Given to processor and waiting 
					if (intr_serviced_i == 1) begin 
						intr_to_service_o = 0;
						intr_valid_o = 0;	
						if (intr_active_i != 0) begin 
							next_state = S_INTR_ACTIVE;
							first_match_f = 1;
						end 
						else begin 
							next_state = S_NO_INTR;
							cur_high_prio = 0;
							intr_with_high_prio = 0;
						end
					end 
				end
				//S_ERROR: begin // removed for simplicity
				//end 
			endcase
		end 
	end 
	
always @(next_state) state = next_state;
	
endmodule
