`include "memory_handshake.v"
module tb;

// 1K memory with 16 bit width
// width=16, depth=1024/16 = 64, addr_width=6

// DO NOT CONFUSE MEMORY WITH FLIPFLOP
// This Verilog code is analogous to simple SRAM memory 

parameter WIDTH = 16;
parameter DEPTH = 1024;
parameter ADDR_WIDTH = 10;

reg clk_i, rst_i;
reg [ADDR_WIDTH-1:0] addr_i;
reg [WIDTH-1:0] wdata_i;
wire [WIDTH-1:0] rdata_o; // Output shall be declared as reg as it has to store data
reg wr_rd_i;
reg valid_i;
wire ready_o;

integer i;
reg [30*8:1] testname;

memory_handshake #(.DEPTH(DEPTH), .ADDR_WIDTH(ADDR_WIDTH), .WIDTH(WIDTH)) dut (clk_i, rst_i, addr_i, wdata_i, rdata_o, wr_rd_i, valid_i, ready_o);
//memory_handshake dut (clk_i, rst_i, addr_i, wdata_i, rdata_o, wr_rd_i, valid_i, ready_o);


always #5 clk_i = ~clk_i;

initial begin 
	$value$plusargs("testname=%s", testname);
	clk_i = 0;
	rst_i = 1;
	#20;
	rst_i = 0;
	// now apply the stimulus
	// write to all locations 

	case (testname)
		"test_fd_wr_fd_rd" : begin // write/read verify from waveform
			fd_write_memory(0, DEPTH);
			fd_read_memory(0, DEPTH);
		end 

		"test_fd_wr_bd_rd" : begin  // write verify from waveform, read verify from image file
			fd_write_memory(0, DEPTH);
			bd_read_memory(0, DEPTH);
		end 

		"test_bd_wr_fd_rd" : begin // read verify from waveform, write verify from image file
			bd_write_memory(0, DEPTH);
			fd_read_memory(0, DEPTH);
		end 

		"test_bd_wr_bd_rd" : begin // write/read verify from image file
			bd_write_memory(0, DEPTH);
			bd_read_memory(0, DEPTH);
		end 
		
		"test_random_wr_rd" : begin 
			// TODO
		end 		
	endcase

	
	
	/////////////////////////////////////////////////////////////////////////////////////////////////
	// When you do back door access no data ports are driven 
	/////////////////////////////////////////////////////////////////////////////////////////////////
	// write to first 1/4 locations 
	
	/*
	bd_write_memory(0, DEPTH/4);
	bd_read_memory(0, DEPTH/4);	

	// write to second 1/4 locations 
	bd_write_memory(DEPTH/4, DEPTH/4);
	bd_read_memory(DEPTH/4, DEPTH/4);	

	// write to third 1/4 locations 
	bd_write_memory(DEPTH/2, DEPTH/4);
	bd_read_memory(DEPTH/2, DEPTH/4);	

	// write to last 1/4 locations 
	bd_write_memory((3*DEPTH)/4, DEPTH/4);
	bd_read_memory((3*DEPTH)/4, DEPTH/4);	
	*/
	
	#100;
	$finish;			
	 
end	
// Uncomment the front door access and see how long it takes to access the memory through ports in QuestaSim
/*
	fd_write_memory(0, DEPTH/4);
	fd_read_memory(0, DEPTH/4);	

	// write to second 1/4 locations 
	fd_write_memory(DEPTH/4, DEPTH/4);
	fd_read_memory(DEPTH/4, DEPTH/4);	

	// write to third 1/4 locations 
	fd_write_memory(DEPTH/2, DEPTH/4);
	fd_read_memory(DEPTH/2, DEPTH/4);	

	// write to last 1/4 locations 
	fd_write_memory((3*DEPTH)/4, DEPTH/4);
	fd_read_memory((3*DEPTH)/4, DEPTH/4);		
*/	


task fd_write_memory(input [ADDR_WIDTH-1:0] start_loc, input [ADDR_WIDTH:0] num_loc);
begin
	for (i = start_loc; i < start_loc + num_loc; i=i+1) begin 
		@(posedge clk_i); // at the positive edge of the clock
		// memory is a synchronous design hence all operations should happen at the positive edge of the clock
		addr_i = i;
		wdata_i = $random;
		wr_rd_i = 1;
		valid_i = 1;
	end
		// wait for getting hand	
		wait (ready_o == 1); // wait for ready_o after all 256 locations are written
		// once handshake is completed drop the hand, meaning making the values 0
		// If we don't do this it will continue to hold the values, it will be assumed that throughout the eval you're keeping this value
		@(posedge clk_i);
		valid_i = 0;
		addr_i = 0;
		wdata_i = 0;
		wr_rd_i = 0;
		
end
endtask

task bd_write_memory(input [ADDR_WIDTH-1:0] start_loc, input [ADDR_WIDTH:0] num_loc);
begin
	$readmemh("image.hex", dut.mem, start_loc, start_loc+num_loc-1);
end
endtask

task fd_read_memory(input [ADDR_WIDTH-1:0] start_loc, input [ADDR_WIDTH:0] num_loc);
begin
	
	for (i = start_loc; i < start_loc + num_loc; i=i+1) begin 
		@(posedge clk_i); // at the positive edge of the clock
		// memory is a synchronous design hence all operations should happen at the positive edge of the clock
		addr_i = i;
		wr_rd_i = 0;
		valid_i = 1;
		// wait for getting hand	
		//wait (ready_o == 1); // wait for ready_o after all 256 locations are written
	end
		// once handshake is completed drop the hand, meaning making the values 0
		// If we don't do this it will continue to hold the values, it will be assumed that throughout the eval you're keeping this value
		@(posedge clk_i);
		valid_i = 0;
		addr_i = 0;
		wdata_i = 0;
		wr_rd_i = 0;
end
endtask
		

task bd_read_memory(input [ADDR_WIDTH-1:0] start_loc, input [ADDR_WIDTH:0] num_loc);
begin
	$writememb("image.bin", dut.mem, start_loc, start_loc+num_loc-1);
end
endtask

initial begin 
	$dumpfile("1.vcd");  
  	$dumpvars;
	
end 
endmodule