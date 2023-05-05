module full_adder(Cout, Sum, Ain, Bin, Cin);
	output Cout, Sum;
	input Ain, Bin, Cin;
	
	wire s1; // sum wires 
	wire c1, c2; // carry
	
	xor x1 (s1, Ain, Bin);
	// xor (s1, Ain, Bin); This is allowed as well. You can skip giving gate name
	xor x2 (Sum, s1, Cin);
	and a1 (c2, Ain, Bin);
	and a2 (c1, s1, Cin);
	or o1(Cout, c1, c2);
	
endmodule