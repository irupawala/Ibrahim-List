module mux_2_to_1(a, b, out, outbar, sel);
	// input wire a, b, sel; 
	// output wire out, outbar;

	input a, b, sel; // by default declared as wire
	output out, outbar; // by default declared as wire
	
	assign out = sel ? a : b;
	assign outbar = ~(out);

endmodule;