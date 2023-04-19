module mux_2_to_1 (a, b, out, outbar, sel);
	input [7:0] a, b;
    	input sel;
	output [7:0] out, outbar;
	reg [7:0] out;

	assign outbar = ~out;
	
	always @(a or b or sel) begin 
		out = (sel == 1'b1) ? a : b;
	end

endmodule
