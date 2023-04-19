module mux2x1(i0, i1, sel, y);
	input i0, i1, sel;
	output y; // reg is not required here because assign is also "continuous" assignment
			  // even wire is not required because by default every variable is a wire
	
	// Dataflow implementation of mux2x1
	assign y = (sel == 1) ? i1: i0; // Whenever you use assign it is called data flow type of implementation
	// assign y = (i0 & ~sel) | (i1 & sel);
	
endmodule