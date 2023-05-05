`include "single_bit_full_adder.v"

module fulladder4(Cout, Sum, Ain, Bin, Cin);
	input [3:0] Ain, Bin;
	input Cin;
	
	output [3:0] Sum;
	output Cout;
	
	wire c1, c2, c3; // carry, if we don't declare variable will be taken as wire by default
	
	full_adder FA1 (c1, Sum[0], Ain[0], Bin[0], Cin);
	full_adder FA2 (c2, Sum[1], Ain[1], Bin[1], c1);
	full_adder FA3 (c3, Sum[2], Ain[2], Bin[2], c2);
	full_adder FA4 (Cout, Sum[3], Ain[3], Bin[3], c3);
	
endmodule