module tb;
integer b, c; // integer means reg [31:0]
wire [31:0] a; // because assign can only be made to wire
assign #3 a = b & c; // a changes 3ns after b&c changes, this is what happens in real life

initial begin 
	#0;
	b = 0;
	c = 0;
	#10;
	b = 101;
	c = 115;
	#10;
	$finish;
end
endmodule