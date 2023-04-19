module up_down_counter_behav (clk, rst, count, up_down);
	input clk, rst, up_down;
	output reg [2:0] count; // reg is required because in between positive edges count should hold the value
	
	always @ (posedge clk) begin
		if (rst == 1) count = 0;
		else begin 
			if (up_down == 1) count = count + 1;
			if (up_down == 0) count = count - 1;
		end
	end

endmodule