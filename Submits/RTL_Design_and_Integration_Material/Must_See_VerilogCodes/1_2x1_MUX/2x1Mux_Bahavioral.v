module mux2x1(i0, i1, sel, y);
	input i0, i1, sel;
	output reg y; // reg stands for register, because the register has to hold the value till the output changes, this occurs only when i0, i1 or sel changes (in always block)
	
	// Behavioral implementation of mux2x1
	// anytime i0, i1, or sel changes
	always @ (i0 or i1 or sel) begin 
		// If sel=0, y should be i0, else y should be i1
		if (sel == 0) y = i0;
		else y = i1;
	end
	
	
endmodule