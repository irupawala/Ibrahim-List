`include "upDownCounter.v"
module tb;
	//
	reg clk, reset, up_down;
	parameter WIDTH = 4;
	wire [WIDTH-1:0] counter;
	
	//
	up_down_counter dut (.clk(clk), .reset(reset), .up_down(up_down), .counter(counter));
	
	//
	initial begin	
		clk = 1'b0;
		forever #2 clk = ~clk;
	end 

	//
	initial begin
		reset = 1'b1;
		up_down = 1'b0;
		#5;
		repeat (100) begin 
		{reset, up_down} = $random;
		#2;	
	end
	end 

	
	//
	initial begin 
		$monitor("time=%0t, clk=%d, reset=%d, up_down=%d, counter=%d", $time, clk, reset, up_down, counter);
	end

	//
	initial begin 
		$dumpfile("wave.vcd");
		$dumpvars;
		#100;
		$finish;
	end	
endmodule
