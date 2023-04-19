module up_down_counter(clk, reset, up_down, counter);
	input clk, reset, up_down;
	parameter WIDTH = 4;
	output reg [WIDTH-1:0] counter;

	always @ (posedge clk) begin
		if (reset) counter <= 'b0;
		else if (up_down == 'b1) counter <= counter + 1;
		else counter <= counter - 1;
	end 
endmodule
