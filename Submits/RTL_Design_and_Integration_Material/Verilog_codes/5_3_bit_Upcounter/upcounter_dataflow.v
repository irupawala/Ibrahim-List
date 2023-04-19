module dff(clk, rst, d, q);
	input clk, rst, d;
	output reg q;
	
	always @ (posedge clk) begin 
		if (rst == 1) q = 0;
		else q = d;
	end

endmodule


// refer to the course slides for gate level expression

module upcounter_dataflow (clk, rst, count);
	input clk, rst;
	output [2:0] count; // count here will not be reg because we're explicitly declaring regs to hold the value
	
	wire p1, p2, p3, d0, d1, d2;
	
	assign p1 = ~count[0] & count[2];
	assign p2 = ~count[1] & count[2];
	assign p3 = ~count[2] & count[1] & count[0];
	assign d2 = (p1 | p2 | p3);
	assign d1 = (count[0] ^ count[1]);
	assign d0 = ~count[0];
	
	dff g7(clk, rst, d2, count[2]);
	dff g8(clk, rst, d1, count[1]);
	dff g9(clk, rst, d0, count[0]);
	
endmodule

