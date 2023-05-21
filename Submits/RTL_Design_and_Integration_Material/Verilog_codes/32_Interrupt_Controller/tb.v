`include "intr_ctrl.v"

// Declare nets
module tb;
	parameter NUM_INTR = 16; //Number of peripherals
	reg pclk_i; 
	reg prst_i;
	reg [7:0] paddr_i;
	reg [7:0] pwdata_i; 
	wire [7:0] prdata_o; 
	reg pwrite_i; 
	reg penable_i; 
	wire pready_o;
	wire [3:0] intr_to_service_o; 
	wire intr_valid_o;
	reg intr_serviced_i;
	// peripherals
	reg [15:0] intr_active_i;
	
	// tb variables
	reg [3:0] prio_arr[15:0]; // 16 elements, with random unique numbers between 0 to 15	
	integer i, p, q, r;
	integer rand_num;	
	integer seed;
	reg unique_num_f;	
	reg [8*50:1] test_name;

	// instantiate the design 
	intr_ctrl dut (
	.pclk_i(pclk_i), 
	.prst_i(prst_i),
	.paddr_i(paddr_i),
	.pwdata_i(pwdata_i), // [3:0] is sufficient to store priority of all the 16 registers
	.prdata_o(prdata_o), 
	.pwrite_i(pwrite_i), 
	.penable_i(penable_i), 
	.pready_o(pready_o), 
	.intr_to_service_o(intr_to_service_o), 
	.intr_valid_o(intr_valid_o),
	.intr_serviced_i(intr_serviced_i),
	.intr_active_i(intr_active_i)
	);

	// clk generation 
	initial begin 
		pclk_i = 0;
		forever #5 pclk_i = ~pclk_i;
	end 
	
	// stimulus generation
	initial begin 
		$value$plusargs("test_name=%s", test_name);
		$value$plusargs("seed=%d", seed);
		prst_i = 1;
		reset_design_inputs(); // whenever reset is applied drive all the design inputs to 0
		repeat(2) @(posedge pclk_i);
		prst_i = 0;
		fill_prio_array(); // generating unique random numbers between 0 to 15
		// stimulus : 1. programming of registers by Processor
		// programming the registers ==> writing to the memory
		for (i = 0; i < NUM_INTR; i=i+1) begin 
			if (test_name == "test_lowest_peri_lowest_priority") write_reg(i, i); // 0->0, 1->1, ..... 15-15
			if (test_name == "test_lowest_peri_highest_priority") write_reg(i, NUM_INTR-i-1); // 0->15, 1->14, ..... 15->0 // reversing the priority
			if (test_name == "test_random_priority") begin 
				write_reg(i, prio_arr[i]); // random priority 
				// display the priority reg
			end
		end
		
		if (test_name == "test_random_priority") begin
			for (r = 0; r < NUM_INTR; r=r+1) begin
				$display("index = %0d, number = %0d", r, prio_arr[r]); 
			end
		end
		
		// stimulus : 2. generate interrupts
		// Peripheral controller generating interrupts and waiting #500 for the interrupts to be serviced
		intr_active_i = $random;
		#500; // taking time to answer the questions
		intr_active_i = $random;
		#500; // taking time to answer the questions
		intr_active_i = $random;
		#500; // taking time to answer the questions		
		$finish; // finishing the class
	end
	
	// Processor writing the priority register
	task write_reg(input reg [3:0] addr, input reg [3:0] data); 
	begin 
		@(posedge pclk_i);
		paddr_i = addr; // address of the registers
		pwdata_i = data; // priority value
		pwrite_i = 1;
		penable_i = 1;
		wait (pready_o == 1); // This is very important, notice how he is waiting for design signal to respond
		@(posedge pclk_i);
		paddr_i = 0;
		pwrite_i = 0;
		pwdata_i = 0;
		penable_i = 0;
	end 
	endtask

	// Processor Responding to Interrupts
	initial begin 
	forever begin 
		@(posedge pclk_i); 
		if (intr_valid_o == 1) begin 
		#20; // time taken by the instructor to anwer one question 
		intr_active_i[intr_to_service_o] = 0; // dropping the interrupt since it has been answered(service)
		intr_serviced_i = 1; // Inst have answered the question => to admin 
		@(posedge pclk_i);
		intr_serviced_i = 0;
		end 
	end 
	end 
	
	// Processor resetting design inputs
	task reset_design_inputs();
	begin 
		penable_i = 0;
		pwrite_i = 0;
		paddr_i = 0;
		pwdata_i = 0;
		intr_serviced_i = 0;
		intr_active_i = 0;
	end
	endtask

	// Processor generating random prority array 
	task fill_prio_array();
		begin
			p = 0;
			while (p < NUM_INTR) begin
				//rand_num = $urandom_range(0,15);
				rand_num = $random(seed) % 16; // 0 to 15
				unique_num_f = 1;
				for (q=0; q<p; q=q+1) begin 
					if (rand_num == prio_arr[q]) begin 
						q = p; // to break for loop
						unique_num_f = 0; // number already exists in the array
					end 
				end
				// keep generating random number till we get a unique number
				if (unique_num_f == 1) begin 
					prio_arr[p] = rand_num;
					p = p + 1;	
				end 
			end
		// by this stage, we have filled the array with 16 unique random numbers between 0 to 15
		end 
	endtask
	
endmodule
	
	
	