`include "memory_handshake.v"

module tb;

// 1K memory with 16 bit width
// width=16, depth=1024/16 = 64, addr_width=6

// DO NOT CONFUSE MEMORY WITH FLIPFLOP
// This Verilog code is analogous to simple SRAM memory 

parameter WIDTH = 16;
parameter DEPTH = 16;
parameter ADDR_WIDTH = 4;

reg clk_i, rst_i;
reg [ADDR_WIDTH-1:0] addr_i;
reg [WIDTH-1:0] wdata_i;
wire [WIDTH-1:0] rdata_o; // Output shall be declared as reg as it has to store data
reg wr_rd_i;
reg valid_i;
wire reg ready_o;

integer i;

memory_handshake #(.WIDTH(WIDTH), .DEPTH(DEPTH), .ADDR_WIDTH(ADDR_WIDTH)) dut (.clk_i(clk_i), .rst_i(rst_i), .addr_i(addr_i), .wdata_i(wdata_i), .rdata_o(rdata_o), .wr_rd_i(wr_rd_i), .valid_i(valid_i), .ready_o(ready_o));

always #5 clk_i = ~clk_i;

initial begin 
	clk_i = 0;
	rst_i = 1;
	#20;
	rst_i = 0;
	// now apply the stimulus
	// write to all locations 
	write_memory(0, DEPTH);
	read_memory(0, DEPTH);
	#100;
	$finish;

end

task write_memory(input [ADDR_WIDTH-1:0] start_loc, input [ADDR_WIDTH:0] num_loc);
begin 
	for (i=start_loc; i<start_loc+num_loc; i=i+1) begin
	@(posedge clk_i); // at the positive edge clk_i
	addr_i = i;
	wdata_i = $random;
	wr_rd_i = 1;
	valid_i = 1;
	end
	wait (ready_o == 1);
	@(posedge clk_i);
	valid_i = 0;
	wr_rd_i = 0;
	addr_i = 0;
	wdata_i = 0;
end
endtask

task read_memory(input [ADDR_WIDTH-1:0] start_loc, input [ADDR_WIDTH:0] num_loc);
begin 
	for(i=start_loc; i<start_loc+num_loc; i++) begin 
	@(posedge clk_i); // at the positive edge clk_i
	addr_i = i;
	wr_rd_i = 0;
	valid_i = 1;
	end
	wait (ready_o == 1);
	@(posedge clk_i);
	valid_i = 0;
	wr_rd_i = 0;
	addr_i = 0;
	wdata_i = 0;
end
endtask


initial begin 
	$dumpvars;
	$dumpfile("waves.vcd");
end
endmodule