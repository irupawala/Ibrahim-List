module mux2x1(i0, i1, sel, y);
	input i0, i1, sel;
	output y; 
	wire n1, n2, n3; // wire is of type net
	
	// Gate level implementation of mux2x1
	// gate inst_name(output, inputs);
	
	not g1(n1, sel);
	and g3(n3, n1, i0);
	and g2(n2, sel, i1);
	or g4(y, n3, n2);
	
endmodule