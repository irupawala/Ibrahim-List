module memory(clk_i, rst_i, addr_i, wdata_i, rdata_o, wr_en_i, rd_en_i);
//4K memory with 64 bit width
// (4 * 1024)/64 = 64 bit depth

// DO NOT CONFUSE MEMORY WITH FLIPFLOP
// This Verilog code is analogous to simple SRAM memory 

parameter WIDTH = 64;
parameter DEPTH = 64;
parameter ADDR_WIDTH = 6;

input clk_i, rst_i;
input [ADDR_WIDTH-1:0] addr_i;
input [WIDTH-1:0] wdata_i;
output reg [WIDTH-1:0] rdata_o;
input wr_en_i, rd_en_i;

integer i;

reg [WIDTH-1:0] mem [DEPTH-1:0];

always @(posedge clk_i) begin 
	if (rst_i == 1) begin 
		rdata_o = 'b0;
		for (i=0; i<DEPTH; i=i+1) begin 
			mem[i] = 'b0;
		end
	end
	else begin
		if (wr_en_i == 1) mem[addr_i] = wdata_i;
		if (rd_en_i == 1) rdata_o = mem[addr_i];
	end
end
endmodule