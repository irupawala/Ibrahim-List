module fa_1bit(a, b, ci, s, co);
	input a, b, ci;
	output s, co;
	
	assign {co, s} = a+b+ci;

endmodule