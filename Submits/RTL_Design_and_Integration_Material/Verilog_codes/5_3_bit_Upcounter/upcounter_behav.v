module upcounter_behav (clk, rst, count);
	input clk, rst;
	output reg [2:0] count; // reg is required because in between positive edges count should hold the value
	
	always @ (posedge clk) begin
		if (rst == 1) count = 0;
		else count = count + 1;
	end

endmodule

