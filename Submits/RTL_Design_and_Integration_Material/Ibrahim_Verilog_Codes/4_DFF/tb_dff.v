`include "dff.v"

module tb;
	// 1. Add signals
	reg [7:0] d;
	reg clk, reset;
	wire [7:0] q;

	// 2. instantiate design 
	dff dut (.d(d), .clk(clk), .reset(reset), .q(q));

	// 3. Drive inputs
	initial begin
	repeat (50) begin 
		{d, reset} = $random;
		#1;
	end
	end

	// 4. Display output
	initial begin 
		$monitor("time = %0t, clk = %d, d = %d, reset = %d, q = %d", $time, clk, d, reset, q);
		#50;
		$finish;
	end 

	// 5. Generate clock
	initial begin
		   clk = 1'b0;
	       forever #1 clk = ~clk;	
	end

	//6. Dump waves
	initial begin
		$dumpfile("waves.vcd");
		$dumpvars;
	end
endmodule
