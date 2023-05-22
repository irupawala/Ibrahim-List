module async_fifo_practice(
wr_clk_i, rd_clk_i, rst_i, 
wdata_i, wr_en_i, full_o, wr_error_o, // write 
rdata_o, rd_en_i, empty_o, rd_error_o
);

	parameter DEPTH = 1, WIDTH = 1, PTR_WIDTH = 1;

	input wr_clk_i, rd_clk_i, rst_i, wr_en_i, rd_en_i;
	input [WIDTH-1:0] wdata_i;
	output reg full_o, wr_error_o, empty_o, rd_error_o;
	output reg [WIDTH-1:0] rdata_o;

	// Internal wire declaration 

	reg [PTR_WIDTH-1:0] wr_ptr, rd_ptr;
	reg wr_toggle_f, rd_toggle_f;
	reg [PTR_WIDTH-1:0] wr_ptr_rd_clk, rd_ptr_wr_clk;
	reg wr_toggle_f_rd_clk, rd_toggle_f_wr_clk;
	reg [PTR_WIDTH-1:0] wr_ptr_gray, rd_ptr_gray;

	// mem declaration 

	reg [WIDTH-1:0] mem [DEPTH-1:0]; // mem

	// integer declaration
	integer i;

	/* Steps

	1. [Done] Declare internal pointers. wr_ptr, rd_ptr, wr_toggle_f, rd_toggle_f;
	2. [Done]logic when full and empty occurs.
	3. [Done]logic when wr_error and rd_error occurs.
	4. [Done]two different always module for wr_clk_i and rd_clk_i
	5. [Done]mem declaration 
	6. Gray Code declaration

	wr_en_i = 1, full_o = 0, crosses 15, then wr_toggle_f = 1

	*/

	// Write seq logic
	always @ (posedge wr_clk_i) begin 
		if (rst_i) begin 
			full_o = 0; // will there be non-blocking over here ?
			empty_o = 1;
			wr_error_o = 0;
			rd_error_o = 0;
			rdata_o = 0;
			wr_ptr = 0;
			rd_ptr = 0;
			wr_toggle_f = 0;
			rd_toggle_f = 0;
			wr_ptr_rd_clk = 0;
			rd_ptr_wr_clk = 0;
			wr_toggle_f_rd_clk = 0;
			rd_toggle_f_wr_clk = 0;
			wr_ptr_gray = 0;
			rd_ptr_gray = 0;
			for (i=0; i<DEPTH; i=i+1) begin 
				mem[i] = 0;
			end
		end
		else begin 
		wr_error_o = 0;
			if (wr_en_i) begin 
				if (full_o == 0) begin // Not Full
					mem [wr_ptr] = wdata_i;
					wr_ptr = wr_ptr + 1;
					wr_ptr_gray = {wr_ptr[PTR_WIDTH-1], wr_ptr[PTR_WIDTH-1:1] ^ wr_ptr[PTR_WIDTH-2:0]};
					if (wr_ptr == DEPTH) begin // toggle wr_ptr
						wr_toggle_f = ~wr_toggle_f;
					end 
				end
				else begin // Full
					wr_error_o = 1;
				end 
			end
		end 
	end

	//read seq logic
	always @ (posedge rd_clk_i) begin 
		if (rst_i != 1) begin
			rd_error_o = 0;
			if (rd_en_i) begin 
				if (empty_o == 0) begin // Not empty
					rdata_o = mem[rd_ptr];
					rd_ptr = rd_ptr + 1;
					rd_ptr_gray = {rd_ptr[PTR_WIDTH-1], rd_ptr[PTR_WIDTH-1:1] ^ rd_ptr[PTR_WIDTH-2:0]};
					if (rd_ptr == DEPTH) begin // toggle rd_ptr
						rd_toggle_f = ~rd_toggle_f;
					end 
				end 
				else begin // empty
					rd_error_o = 1;
				end 
			end 
		end
	end 

	// logic to generate full and empty

	always @ (*) begin 
		empty_o = 0;
		full_o = 0;
		// full	
		if (rd_ptr_wr_clk == wr_ptr_gray) begin 
			if (rd_toggle_f_wr_clk != wr_toggle_f) full_o = 1;
		end
		// empty		
		if (rd_ptr_gray == wr_ptr_rd_clk) begin 
			if (rd_toggle_f == wr_toggle_f_rd_clk) empty_o = 1;
		end	
		
	end 


	// Now the problem is rd_clk_i and wr_clk_i does not 
	// have same frequency. Hence we need to define synchronizers

	// full happens on wr_clk_i, hence we need to bring rd_ptr
	// and rd_toggle_f to wr_clk_i frquency
	// V.V for empty 

	always @ (posedge wr_clk_i) begin 
		rd_ptr_wr_clk <= rd_ptr_gray;
		rd_toggle_f_wr_clk <= rd_toggle_f;
	end

	always @ (posedge rd_clk_i) begin 
		wr_ptr_rd_clk <= wr_ptr_gray;
		wr_toggle_f_rd_clk <= wr_toggle_f;
	end 

endmodule