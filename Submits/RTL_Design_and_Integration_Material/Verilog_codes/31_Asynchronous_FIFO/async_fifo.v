module async_fifo(
	// write interface
	rd_clk_i, wr_clk_i, rst_i, wdata_i, wr_en_i, wr_error_o,
	// read interface	
	rdata_o, full_o, empty_o, rd_en_i, rd_error_o
	
);

parameter DEPTH=16, WIDTH=8, PTR_WIDTH=4;

//wr_ptr is internal to the design 
input rd_clk_i, wr_clk_i, rst_i, wr_en_i, rd_en_i;
input [WIDTH-1:0] wdata_i;
output reg wr_error_o, rd_error_o, full_o, empty_o;
output reg [WIDTH-1:0] rdata_o;

// mem declaration 
reg [WIDTH-1:0] mem [DEPTH-1:0];

// internal signals
reg [PTR_WIDTH-1:0] rd_ptr, wr_ptr;
reg wr_toggle_f, rd_toggle_f;

reg [PTR_WIDTH-1:0] rd_ptr_gray, wr_ptr_gray;
reg [PTR_WIDTH-1:0] rd_ptr_gray_wr_clk, wr_ptr_gray_rd_clk;

reg wr_toggle_f_rd_clk, rd_toggle_f_wr_clk;

integer i; // Remember to remove unwanted integers

// write always block
always @(posedge wr_clk_i) begin 
	if (rst_i == 1) begin // reset should happen w.r.t write clock domain
		wr_error_o = 0;
		rd_error_o = 0;
		full_o = 0;
		empty_o = 1;
		rdata_o = 0;
		rd_ptr = 0;
		wr_ptr = 0;
		rd_ptr_gray = 0;
		wr_ptr_gray = 0;
		rd_ptr_gray_wr_clk = 0;
		wr_ptr_gray_rd_clk = 0;	
		wr_toggle_f = 0;
		rd_toggle_f = 0;
		wr_toggle_f_rd_clk = 0;
		rd_toggle_f_wr_clk = 0;		
		// clear the memory
		for (i=0; i<DEPTH; i=i+1) begin 
			mem[i] = 0;
		end
	end	

	else begin 
		wr_error_o = 0;
		if (wr_en_i == 1) begin 
			if (full_o == 1) begin 
				wr_error_o = 1;
			end
			else begin 
				// store data into memory
				mem[wr_ptr] = wdata_i;
				// increment the wr_ptr
				if (wr_ptr == DEPTH-1) begin 
					wr_toggle_f = ~wr_toggle_f;
				end
				wr_ptr = wr_ptr + 1;
				wr_ptr_gray = {wr_ptr[PTR_WIDTH-1], (wr_ptr[PTR_WIDTH-1:1] ^ wr_ptr[PTR_WIDTH-2:0])}; // Gray code conversion 
			end
		end

	end 
end 

// read always block
always @(posedge rd_clk_i) begin 
	if (rst_i != 1) begin
		rd_error_o = 0;
		if (rd_en_i == 1) begin
			if (empty_o == 1) rd_error_o = 1;
			else begin 
				rdata_o = mem[rd_ptr];
				// increment the rd_ptr
				if (rd_ptr == DEPTH-1) rd_toggle_f = ~rd_toggle_f;
				rd_ptr = rd_ptr + 1;
				rd_ptr_gray = {rd_ptr[PTR_WIDTH-1], (rd_ptr[PTR_WIDTH-1:1] ^ rd_ptr[PTR_WIDTH-2:0])}; // Gray code conversion 
			end 		
		end
	end
end 


always @(posedge rd_clk_i) begin 
	wr_ptr_gray_rd_clk <= wr_ptr_gray;
	wr_toggle_f_rd_clk <= wr_toggle_f;
end 

always @(posedge wr_clk_i) begin 
	rd_ptr_gray_wr_clk <= rd_ptr_gray;
	rd_toggle_f_wr_clk <= rd_toggle_f;
end

// logic to create empty and full condition
/*
wr_ptr and rd_ptr are changing in different clock domains and hence cannot 
be compared directly
*/

always @(*) begin 
	empty_o = 0;
	full_o = 0;
	// full
	if (wr_ptr_gray == rd_ptr_gray_wr_clk) begin 
		if (wr_toggle_f != rd_toggle_f_wr_clk) full_o = 1;
	end
	// empty
	if (wr_ptr_gray_rd_clk == rd_ptr_gray) begin 
		if (wr_toggle_f_rd_clk == rd_toggle_f) empty_o = 1;	
	end	
end

endmodule

/*
- Aynchronous FIFO we have developed will work in RTL simulations without any issues.
- If we synthesize and make a chip out of it => it might have some glitch conditions.
- wr_ptr is 4 bit variable, when change happens from 0111 to 1000 there will be a temporary change from 0111 -> 0110 -> 0100 -> 0000 -> 1000
- when wr_ptr during this temporary change becomes 0000, it will match to rd_ptr which is also 0000 hence unwanted empty condition will be generated
- To resolve this issue we have to use grey code counter which changes only one bit while going from one value to another value => hence there
is no possibility of intermediary states => thus there is no chance of glitch
*/
