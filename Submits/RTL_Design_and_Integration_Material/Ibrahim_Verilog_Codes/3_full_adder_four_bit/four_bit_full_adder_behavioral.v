module fa_4bit(a, b, ci, s, co);
	input [3:0] a, b;
	input ci;
	output [3:0] s;
	output co;
	
	assign {co, s} = a + b + ci;
	
endmodule