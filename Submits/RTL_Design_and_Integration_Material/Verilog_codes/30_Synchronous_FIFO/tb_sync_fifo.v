`include "sync_fifo.v"
module tb();

	parameter DEPTH=16, WIDTH=8, PTR_WIDTH=4;

	//wr_ptr is internal to the design 
	reg clk_i, rst_i, wr_en_i, rd_en_i;
	reg [WIDTH-1:0] wdata_i;
	wire wr_error_o, rd_error_o, full_o, empty_o;
	wire [WIDTH-1:0] rdata_o;

	integer num_wr, num_rd;
	integer i, j;
	reg [30*8:1] testname;

	// instantiate the design
	fifo dut (.clk_i(clk_i), .rst_i(rst_i), .wdata_i(wdata_i), .wr_en_i(wr_en_i), .wr_error_o(wr_error_o), .rdata_o(rdata_o), .full_o(full_o), .empty_o(empty_o), .rd_en_i(rd_en_i), .rd_error_o(rd_error_o));

	// generate clk
	initial begin 
		clk_i = 0;
		forever #5 clk_i = ~clk_i;
		//don't code anything after forever in any language
	end

	// generate test inputs
	initial begin 
		$value$plusargs("testname=%s", testname);
		rst_i = 1; 
		// drive design inputs to 0
		wdata_i = 0;
		wr_en_i = 0;
		rd_en_i = 0;
		// #20;
		@(posedge clk_i); // holding
		rst_i = 0; // releasing
		// apply stimulus: write to the FIFO and read from the FIFO
		case (testname) 
			"test_full": begin 
				write_fifo(DEPTH);
			end
			"test_empty": begin
				write_fifo(DEPTH);
				read_fifo(DEPTH);
			end
			"test_full_error": begin 
				write_fifo(DEPTH+1);
			end
			"test_empty_error": begin 
				write_fifo(DEPTH);
				read_fifo(DEPTH+1);
			end
			"test_concurrent_wr_rd": begin 
			end
		endcase
		
		#50;
		$finish;
	end

	// dump files
	initial begin 
		$dumpvars;
		$dumpfile("waves.vcd");
	end 

task write_fifo(input integer num_wr);
	begin
		for (i = 0; i < num_wr; i=i+1) begin 
			@(posedge clk_i) 
			wr_en_i = 1;
			wdata_i = $random;
		end 	
		@(posedge clk_i);
		wr_en_i = 0;
		wdata_i = 0;
	end
endtask

task read_fifo(input integer num_rd);
	begin
		for (j = 0; j < num_rd; j=j+1) begin 
			@(posedge clk_i) rd_en_i = 1;	
		end
		@(posedge clk_i);
		rd_en_i = 0;
	end
endtask


endmodule
