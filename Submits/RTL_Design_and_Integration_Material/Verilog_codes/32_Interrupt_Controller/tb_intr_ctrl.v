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
	wire perror_o;
	wire [3:0] intr_to_service_o; 
	reg intr_valid_o;
	reg intr_serviced_i;
	// peripherals
	reg [15:0] intr_active_i;
	reg [3:0] prio_arr[15:0]; // 16 elements, with random unique numbers between 0 to 15
	integer i, r;
	integer seed;
	reg [8*50:1] test_name;

	// instantiate the design 
	intr_ctrl dut (.*);

	// clk generation 
	initial begin 
		pclk_i = 0;
		forever = #5 pclk_i = ~pclk_i;
	end 
	
	// stimulus
	initial begin 
		$value$plusargs("test_name=%s seed=%d", test_name, seed);
		prst_i = 1;
		reset_design_inputs(); // whenever reset is appliedm drive all the design inputs to 0
		repeat(2) @(posedge pclk_i);
		prst_i = 0;
		fill_prio_array(); // generating unique random numbers between 0 to 15
		// stimulus : 1. programming of registers 
		//programming the registers ==> writing to the memory
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
		// generate interrupts
		intr_active_i = $random;
		#500; // taking time to answer the questions
		intr_active_i = $random;
		#500; // taking time to answer the questions
		intr_active_i = $random;
		#500; // taking time to answer the questions		
		$finish; // finishing the class
		
	end
	
task write_reg(input reg [3:0 addr, input reg [3:0] data); 
begin 
	@(posedge pclk_i);
	paddr_i = addr; // address of the registers
	pwdata_i = data; // priority value
	pwrite_i = 1;
	penable_i = 1;
	wait (pready_o == 1);
	@(posedge pclk_i);
	paddr_i = 0;
	pwrite_i = 0;
	pwdata_i = 0;
	penable_i = 0;
end 
endtask

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

task fill_prio_array();
begin
	integer p, q;
	integer rand_num;
	reg unique_num_f;
	begin
		for (p = 0; p < NUM_INTR; ) begin 
			//rand_num = $urandom_range(0,15);
			rand_num = $random(seed) % 16; // 0 to 15
			unique_num_f = 1;
			for (q = 0; q < p; q=q+1) begin 
				if (rand_num == prio_arr[q] begin 
					q == p; // to break for loop
					unique_num_f = 0; // number already exists in the array
				end 
			end
			// keep generating random number till we get a unique number
			if (unique_num_f == 1) begin 
				prio_arr[p] = unique_num_f;
				p = p + 1;	
			end 
		end
	end 
	// by this stage, we have filled the array with 16 unique random numbers between 0 to 15
end 
endtask
	

endmodule