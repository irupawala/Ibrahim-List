`include "async_fifo.v"
module tb();

	parameter DEPTH=16, WIDTH=8, PTR_WIDTH=4;
	parameter WR_CK_TP=10, RD_CLK_TP=14;
	parameter MAX_WR_DLY=10, MAX_RD_DLY=10;
	parameter NUM_TXS=10;

	//wr_ptr is internal to the design 
	reg rd_clk_i, wr_clk_i, rst_i, wr_en_i, rd_en_i;
	reg [WIDTH-1:0] wdata_i;
	wire wr_error_o, rd_error_o, full_o, empty_o;
	wire [WIDTH-1:0] rdata_o;

	integer num_wr, num_rd;
	integer i, j, k, l;
	integer wr_delay, rd_delay;
	integer seed;
	reg [30*8:1] testname;

	// instantiate the design
	async_fifo dut (.rd_clk_i(rd_clk_i), .wr_clk_i(wr_clk_i), .rst_i(rst_i), .wdata_i(wdata_i), .wr_en_i(wr_en_i), .wr_error_o(wr_error_o), .rdata_o(rdata_o), .full_o(full_o), .empty_o(empty_o), .rd_en_i(rd_en_i), .rd_error_o(rd_error_o));

	// generate clk
	initial begin 
		wr_clk_i = 0;
		forever #(WR_CK_TP/2.0) wr_clk_i = ~wr_clk_i;
		//don't code anything after forever in any language
	end
	
	initial begin 
		rd_clk_i = 0;
		forever #(RD_CLK_TP/2.0) rd_clk_i = ~rd_clk_i;
		//don't code anything after forever in any language
	end	

	// generate test inputs
	initial begin 
		$value$plusargs("testname=%s", testname);
		rst_i = 1; 
		seed = 415341;
		// drive design inputs to 0
		wdata_i = 0;
		wr_en_i = 0;
		rd_en_i = 0;
		// #20;
		@(posedge wr_clk_i); // holding
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
				fork
					begin 
						for (k=0; k < NUM_TXS; k=k+1) begin //500 people going into bank in whole day
							write_fifo(1); // write one data into FIFO
							//wr_delay = $urandom_range(1, MAX_WR_DLY); //1 to 10 minutes between one person to next person
							wr_delay = 1 + $random(seed)%MAX_WR_DLY; // random number 1 to 10
							repeat (wr_delay) @(posedge wr_clk_i); // applying delay for wr_delay number of times clock edges
						end
					end 
					begin
						for (l=0; l < NUM_TXS; l=l+1) begin //500 people going out from the bank
							read_fifo(1); // read one data from FIFO
							//rd_delay = $urandom_range(1, MAX_RD_DLY); //1 to 10 minutes between one person to next person
							rd_delay = 1 + $random(seed)%MAX_RD_DLY; // random number 1 to 10
							repeat (rd_delay) @(posedge rd_clk_i); // applying delay for rd_delay number of times clock edges
							
						end
					end
				join 
			end
		endcase
		
		#50;
		$finish;
	end

	task write_fifo(input integer num_wr);
		begin
			for (i = 0; i < num_wr; i=i+1) begin 
				@(posedge wr_clk_i) 
				wr_en_i = 1;
				wdata_i = $random;
			end 	
			@(posedge wr_clk_i);
			wr_en_i = 0;
			wdata_i = 0;
		end
	endtask

	task read_fifo(input integer num_rd);
		begin
			for (j = 0; j < num_rd; j=j+1) begin 
				@(posedge rd_clk_i) rd_en_i = 1;	
			end
			@(posedge rd_clk_i);
			rd_en_i = 0;
		end
	endtask

	// dump files
	initial begin
		$dumpfile("waves.vcd");
		$dumpvars;
		
	end 

endmodule
