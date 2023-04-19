module param_adder(a, b, cin, sum, cout);
	parameter WIDTH = 4;
	input [WIDTH-1:0] a, b;
	input cin;
	output reg [WIDTH-1:0] sum;
	output reg cout;

	always@(*) begin 
		{cout, sum} = a + b + cin;
	end

endmodule
