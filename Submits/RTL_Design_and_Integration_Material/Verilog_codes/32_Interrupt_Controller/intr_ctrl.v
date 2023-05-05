module intr_ctrl(
	// processor
	input pclk_i, 
	input prst_i,
	input [7:0] paddr_i,
	input [7:0] pwdata_i, // [3:0] is sufficient to store priority of all the 16 registers
	output [7:0] prdata_o, 
	input pwrite_i, 
	input penable_i, 
	output reg pready_o, 
	// input psel_i, // removing sel to simplify the design 
	output reg perror_o, 
	output reg [3:0] intr_to_service_o, 
	input intr_serviced_i,

	// peripherals
	input [NUM_INTR-1:0] intr_active_i
	);

	parameter NUM_INTR = 16; //Number of peripherals
	integer i;

	//registers
	reg [7:0] priority_regA[NUM_INTR-1:0] // Note here that to store the priority of 16 register 4 bits are sufficient 
	// hence reg [3:0] priority_regA[NUM_INTR-1:0] could be used but as we have declared data [7:0] pwdata_i we are 
	// also declaring the registers as 8 bits

	// register programming 
	always @(posedge pclk_i) begin 
		if (prst_i == 1) begin 
			prdata_o = 0;
			pready_o = 0;
			perror_o = 0;
			intr_to_service_o = 0;
			for (i = 0; i < NUM_INTR: i=i+1) begin 
				priority_regA[i] = 0;
			end 
		end 
		else begin 
			if (penable_i == 1) begin 
				pready_o = 1;
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
				end
				S_INT: begin 
				end
				S_INTR_GIVEN_WAIT_FOR_SERVICE: begin 
				end
				S_ERROR: begin 
				end 
			endcase
		end 
	end 
	
always @(next_state) state = next_state;
	
endmodule
