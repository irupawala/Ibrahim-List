module dynamic_pattern_detector(clk, reset, d_in, valid_in, pattern_flag);

input clk, reset, d_in, valid_in;
output reg pattern_flag;

reg[4:0] pattern_to_detect, current_pattern;
integer count;

initial begin 
	pattern_to_detect = 5'b01101; //BCCBC
	current_pattern = 5'b00000;
end

always @(posedge clk) begin 
	if (reset == 1) begin 
		current_pattern = 'b0;
		pattern_flag = 0;
		count = 0;
	end
	else begin 
		pattern_flag = 0;
		if (valid_in == 1) begin 
			current_pattern = {current_pattern[3:0], d_in};
			if (current_pattern == pattern_to_detect) begin 
				pattern_flag = 1;
			end 
		end
	end 	

end 
	
endmodule
