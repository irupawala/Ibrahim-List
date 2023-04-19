module half_adder(a, b, carry_in, sum, carry_out);
	input a;
	input b; 
	input carry_in;
	
	output sum;
	output carry_out;
	
	wire s1; // sum wires 
	wire c1, c2; // carry
	
	xor x1 (s1, a, b);
	// xor (s1, a, b); This is allowed as well. You can skip giving gate name
	xor x2 (sum, s1, carry_in);
	and a1 (c2, a, b);
	and a2 (c1, s1, carry_in);
	or o1(carry_out, c1, c2);
	
endmodule