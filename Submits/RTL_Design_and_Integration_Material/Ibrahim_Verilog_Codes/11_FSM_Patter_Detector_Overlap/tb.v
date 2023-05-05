`include "fsm_pattern_detector_overlap.v"

module tb;
	// Add the nets
	reg clk, reset, d_in, valid_in;
	wire pattern_flag;
	integer seed;
	integer count;

	// generate clk
	always begin 
		#5 clk = 0;
		#5 clk = 1;
	end

	//instantiate
	fsm_pattern_detector dut (clk, reset, d_in, valid_in, pattern_flag);

	//dump vars
	initial begin 
		$dumpfile("waves.vcd");
		$dumpvars;
	end
	
	//generate inputs
	initial begin
		count = 0;
		seed = 37934298;
		reset = 1;
		#20;
		reset = 0;
		repeat (540) begin 
			@(posedge clk) begin
				valid_in = 1'b1;	
				d_in = $random(seed);
			end
		end 
		@(posedge clk) begin 
			valid_in = 1'b0;
			d_in = 1'b0;
			end
		#50;
		$display("total count = %0d", count);
		$finish;
	end 
	
	always @(posedge pattern_flag) count = count + 1;
	
endmodule
