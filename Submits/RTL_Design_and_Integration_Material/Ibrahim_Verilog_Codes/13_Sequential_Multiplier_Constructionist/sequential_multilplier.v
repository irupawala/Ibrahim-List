module sequential_mult(a, b, ab_valid, ab_ready, clk, rst, z_valid, z);

parameter Multiplier_length = 4;
parameter Multiplicand_length = 4;

input [Multiplicand_length-1: 0] a;
input [Multiplier_length-1: 0] b;
input ab_valid, clk, rst;
output reg z_valid, ab_ready;
output reg [(Multiplier_length+Multiplicand_length+1): 0] z;

reg [Multiplicand_length-1: 0] Multiplicand_next, Multiplicand_reg;
reg [(Multiplier_length+Multiplicand_length+1):0] CAQ_next, CAQ_reg;


always @ (posedge clk) begin 
	if (rst) begin 
		z = 0;
		z_valid = 0;
		ab_ready = 0;
	end 
	else begin 
		if (ab_valid == 0) begin 
			
		end
		else begin 
		end

	end 
end

endmodule
