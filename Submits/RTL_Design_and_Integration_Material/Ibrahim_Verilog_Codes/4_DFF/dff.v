module dff(d, clk, reset, q);
	input [7:0] d;
	input clk, reset;
	output reg [7:0] q;
	
	always @(posedge clk) begin 
		if (reset) q <= 8'b0;
		else q <= d;
	end
endmodule
