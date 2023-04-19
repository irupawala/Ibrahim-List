`include "fa_1bit.v"

module fa_nbit(a, b, ci, s, co);

	parameter WIDTH = 12;
	input [WIDTH-1:0] a, b;
	input ci;

	output [WIDTH-1:0] s;
	output co;

	wire [WIDTH:0] c;
	assign c[0] = ci;
	assign co = c[WIDTH];

	genvar i; // don't declare as integer
			  // genvar: generation variable
			  // code generation variable
			  
	// Note that genvar will create a code unlike normal for loop hence fa_1bit over here will be replaced by 8 lines of code.
	// This is called compile time. During the compile time while it is converting code to object file, this single line will be 
	// replaced by 8 lines of code 
	// genvar is a compile time concept
	// when i is integer we have to write it inside initial begin block
			  
	for (i=0; i< WIDTH; i=i+1) begin 
		fa_1bit u(a[i], b[i], c[i], s[i], c[i+1]);
	end

endmodule