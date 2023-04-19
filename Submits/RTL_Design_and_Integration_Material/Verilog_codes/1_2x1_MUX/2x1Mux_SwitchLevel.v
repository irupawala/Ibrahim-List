module mux2x1(i0, i1, sel, y);
	input i0, i1, sel;
	output reg y; // reg stands for register, because the register has to hold the value till the output changes, this occurs only when i0, i1 or sel changes (in always block)
	
	// Implementation using pmos and nmos
	
endmodule