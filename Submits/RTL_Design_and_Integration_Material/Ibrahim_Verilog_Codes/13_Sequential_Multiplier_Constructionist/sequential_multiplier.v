// This Code is designed in a way that Multiplicand_length has to be always greater then Multiplier_length


module seq_mult(a, b, ab_valid, ab_ready, clk, rst, z_valid, z);

	parameter Multiplicand_length = 1;
	parameter Multiplier_length = 1;
	
	input [Multiplicand_length-1: 0] a;
	input [Multiplier_length-1: 0] b;
	input ab_valid;
	input clk;
	input rst;
	output reg ab_ready;
	output reg z_valid;
	output reg [Multiplier_length+Multiplicand_length-1: 0] z;
	
	parameter idle = 1'b0;
	parameter mult = 1'b1;
	
	reg state_reg, state_next; 
	reg [Multiplier_length-1: 0] multiplier_reg, multiplier_next;	
	reg [Multiplier_length+Multiplicand_length-1:0] multiplicand_reg, multiplicand_next;	
	reg ab_valid_reg;
	reg [Multiplier_length+Multiplicand_length-1:0] z_reg, z_next; 
	reg ab_ready_next, ab_ready_reg, z_valid_reg, z_valid_next;

	always @ (posedge clk or negedge rst) begin 
		if (~rst) begin
			multiplier_reg <= 'd0;
			multiplicand_reg <= 'd0;
			ab_valid_reg <= 'b0;
			ab_ready_reg <= 'b1; // if rst ab_ready_reg=1 because then we are indicating that our design is in idle state
			z_valid_reg <= 'b0;
			z_reg <= 'd0;
			state_reg <= idle;
		end 
		else begin 
			multiplier_reg <= multiplier_next;
			multiplicand_reg <= multiplicand_next;
			ab_valid_reg <= ab_valid;
			ab_ready_reg <= ab_ready_next;
			z_valid_reg <= z_valid_next;
			z_reg <= z_next; 	
			state_reg <= state_next;
		end 
	end

	always @(*) begin 
		//multiplier_next = multiplier_reg;
		//multiplicand_next = multiplicand_reg;
		//ab_ready_next = ab_ready_reg;
		//z_valid_next = z_valid_reg;
		//z_next = z_reg;
		//state_next = state_reg;

		ab_ready = ab_ready_reg; // here as soon as we are finishing calculations we transfer the values of these to the final output
		z_valid = z_valid_reg;
		z = z_reg;    		
		
		
		case (state_reg)
		
			idle: begin 
				ab_ready_next = 'b1;
				z_valid_next = 'b0;
				if (ab_valid_reg) begin 
					multiplier_next = b;			
					multiplicand_next = 'd0;
					multiplicand_next = multiplicand_next + a;
					ab_ready_next = 'b0;
					z_next = 'd0;
					state_next = mult;
				end 
				else begin
					state_next = idle;
				end
			end 
			
			mult: begin
				if (multiplier_reg[0] == 'b1) begin 
					z_next = z_reg + multiplicand_reg;
				end
				else begin 
					z_next = z_reg;
				end	
				
				multiplier_next = multiplier_reg >> 'b1;
				multiplicand_next = multiplicand_reg << 'b1;
				
				if(multiplier_reg == 'd0) begin
					ab_ready_next = 'b1;
					z_valid_next = 'b1;
					state_next = idle;
				end
				else begin
					state_next = mult;
				end 
			end 
		endcase
	end

endmodule

// problem is that with state machine as soon as ab_valid is high 
// once, the state is locked to mult, how can this be done without
// state machine and be ensured that the state remains mult until
// output is thrown even though ab_valid is high