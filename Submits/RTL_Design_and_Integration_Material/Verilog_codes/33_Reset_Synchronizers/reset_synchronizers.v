// Reset Synchronizers

// Assertion happens ASynchronously and De-Assertion happens Synchronously.

module reset_sync(asyncrst_n, clk, rst_n);

	input asyncrst_n, clk;
	output reg rst_n;
	reg rff1;

	always @(posedge clk or negedge asyncrst_n) begin 
		if (~asyncrst_n) begin // assert immediately
			rff1 <= 0;
			rst_n <= 0;
		end 
		else begin 
			rff1 <= 1;
			rst_n <= rff1;
		end 
	end
endmodule