/*
Mistakes
1. Forgot reset logic 
2. Forgot default case statement
*/

/*
Comments
- Moore State Machine => Last State included in the design as Moore output depends only on state
*/

module fsm_pattern_detector(clk, reset, d_in, valid_in, pattern_flag);

input clk, reset, d_in, valid_in;
output reg pattern_flag;

parameter S_RESET = 3'b000;
parameter S_B = 3'b001;
parameter S_BC = 3'b010;
parameter S_BCC = 3'b011;
parameter S_BCCB = 3'b100;
parameter S_BCCBC = 3'b101;

parameter C = 1'b0; // Car
parameter B = 1'b1; // Bike

// 3FF requied for storing states
reg [2:0] state, next_state;

always @ (posedge clk) begin 
	if (reset == 1) begin 
		// all reg variables make to 0 or reset value
		pattern_flag = 0;
		state = S_RESET;
		next_state = S_RESET;
	end 
	else begin  
		pattern_flag = 1'b0;
		if (valid_in == 1) begin
			case (state) 
				S_RESET: begin 
					if (d_in == B) next_state = S_B;
					else next_state = S_RESET;
				end
				S_B: begin 
					if (d_in == B) next_state = S_B;
					else next_state = S_BC;
				end
				S_BC: begin 
					if (d_in == B) next_state = S_B;
					else next_state = S_BCC;
				end
				S_BCC: begin 
					if (d_in == B) next_state = S_BCCB;
					else next_state = S_RESET;
				end
				S_BCCB: begin 
					if (d_in == B) next_state = S_B;
					else next_state = S_BCCBC;
				end
				S_BCCBC: begin 
					pattern_flag = 1'b1;
					if (d_in == B) next_state = S_B;
					else next_state = S_BCC;
				end
				default: begin
					$display("Error Condition");
					next_state = S_RESET;
				end 
			endcase
		end 
	end
end 

always @(next_state) state = next_state;

endmodule
