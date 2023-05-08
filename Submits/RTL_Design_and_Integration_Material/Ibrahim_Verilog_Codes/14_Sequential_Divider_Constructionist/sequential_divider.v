/*

Watch the Video - https://www.youtube.com/watch?v=VKemv9u40gc
				  https://www.youtube.com/watch?v=MVpOKwTKVSc&t=297s
- Design is similar to Multiplier 

*/

module sequential_divider (num, den, nd_valid, nd_ready, clk, rst, qr_valid, quo, rem);
	parameter NUM_LENGTH = 1;
	parameter DEN_LENGTH = 1;
	input [NUM_LENGTH-1:0] num;
	input [DEN_LENGTH-1:0] den;
	input nd_valid;
	input clk;
	input rst;
	
	output reg nd_ready;	
	output reg qr_valid;
	output reg [NUM_LENGTH-1:0] quo;
	output reg [DEN_LENGTH-1:0] rem;
	
	parameter idle = 2'b00;
	parameter div = 2'b01;
	parameter undefined_div_by_0 = 2'b10;
	
	reg [1:0] state_reg, state_next;
	reg [NUM_LENGTH-1:0] quo_reg, quo_next;
	reg [NUM_LENGTH+DEN_LENGTH:0] rem_reg, rem_next;
	reg [NUM_LENGTH+DEN_LENGTH-1:0] divisor_reg, divisor_next;
	reg nd_ready_reg, nd_ready_next;
	reg qr_valid_reg, qr_valid_next;
	reg [DEN_LENGTH-1:0] counter_reg, counter_next;
	//reg nd_valid_reg; // This will make the design grab inputs on next clock edge
	
	always @(posedge clk or negedge rst) begin 
		if (~rst) begin 
			quo_reg <= 0;
			rem_reg <= 0;
			divisor_reg <= 0;
			nd_ready_reg <= 1;
			qr_valid_reg <= 0;
			counter_reg <= 0;
			state_reg <= idle;
			//nd_valid_reg <= 0;
		end
		else begin 
			quo_reg <= quo_next;
			rem_reg <= rem_next;
			divisor_reg <= divisor_next;
			nd_ready_reg <= nd_ready_next;
			qr_valid_reg <= qr_valid_next;
			counter_reg <= counter_next;	
			state_reg <= state_next;
			//nd_valid_reg <= nd_valid;			
		end
	end 
	
	always @(*) begin 
		////////// These lines are needed in Div but not in Mult because in Mult design all the variables on LHS is *_reg
		quo_next = quo_reg;
		rem_next = rem_reg;
		divisor_next = divisor_reg;
		nd_ready_next = nd_ready_reg;
		qr_valid_next = qr_valid_reg;
		counter_next = counter_reg;
		state_next = state_reg;      
	
		quo = quo_reg;
		rem = rem_reg[DEN_LENGTH-1:0];
		nd_ready = nd_ready_reg;
		qr_valid = qr_valid_reg;
		
		case (state_next) 
			idle:
			begin 
              	nd_ready_next = 1;
				state_next = idle;	
				qr_valid_next = 0;
				counter_next = 0;	
				if (nd_valid) begin 
					if (den == 0) begin 
						nd_ready_next = 0;
						state_next = undefined_div_by_0;
						quo_next = 0;
						divisor_next = 0;
						rem_next = 0;
					end
					else begin 
						nd_ready_next = 0;
						state_next = div;					
						quo_next = 0;
						
						divisor_next = 0;
						divisor_next = divisor_next + den;
						divisor_next = divisor_next << NUM_LENGTH; 

						rem_next = 0;
						rem_next = rem_next + num;
					end 
				end
			end
			div:
			begin 
				//$display("pre_rem_sub quo_next %b divisor_next %b rem_next %b",quo_next, divisor_next,rem_next);
				rem_next = rem_next - divisor_next;
				//$display("post_rem_sub quo_next %b divisor_next %b rem_next %b",quo_next, divisor_next,rem_next);
				if (rem_next[NUM_LENGTH+DEN_LENGTH] == 0) begin 
					quo_next = quo_reg << 1;
					quo_next = quo_next + 1;
				end 
				else begin 
					rem_next = rem_next + divisor_next;
					quo_next = quo_reg << 1;
				end
				//$display("post_rem_add quo_next %b divisor_next %b rem_next %b",quo_next, divisor_next,rem_next);
				divisor_next = divisor_next >> 1;
				counter_next = counter_next + 1;
				//$display("post_div_shf quo_next %b divisor_next %b rem_next %b",quo_next, divisor_next,rem_next);
				//$display("post_cnt_add counter_next %d",counter_next);
				if (counter_next == (NUM_LENGTH+1)) begin 
					nd_ready_next = 1;
					qr_valid_next = 1;
					state_next = idle;
				end 
			end 
			
			undefined_div_by_0: // division by 0
			begin 
				quo_next = 0;
				rem_next = 0;
				divisor_next = 0;
				nd_ready_next = 1;
				qr_valid_next = 1;
				state_next = idle;				
			end
		endcase
	end
	
endmodule