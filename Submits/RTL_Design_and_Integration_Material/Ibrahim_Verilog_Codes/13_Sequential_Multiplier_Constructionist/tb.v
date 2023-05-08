`include "sequential_multiplier_NoFSM.v"

module tb;
	// Declare IO's
	parameter Multiplicand_length = 5;
	parameter Multiplier_length = 2;	
	
	reg [Multiplicand_length-1: 0] a;
	reg [Multiplier_length-1: 0] b;
	reg ab_valid;
	reg clk;
	reg rst;
	wire ab_ready;
	wire z_valid;
	wire [Multiplier_length+Multiplicand_length-1: 0] z;
	
	// Declare clk
	initial begin 
		clk = 0;
		forever #1 clk = ~clk;
	end 
	
	// Instantiate design 
  seq_mult #(.Multiplicand_length(Multiplicand_length), .Multiplier_length(Multiplier_length)) dut 	 	(
	.a(a), 
	.b(b), 
	.ab_valid(ab_valid),
	.ab_ready(ab_ready),
	.clk(clk),
	.rst(rst),
	.z_valid(z_valid),
	.z(z));
	
	// Drive Inputs
	initial begin 
		rst = 0; 
		#5;
		rst = 1;
		#5;
      repeat (50) begin 
			@(posedge clk) begin
              	ab_valid = $random;
				a = $random;
				b = $random;
			end
		end
		@(posedge clk) begin 
				ab_valid = 0;
			end		
		#100;
		$finish();
	end 
	
	initial begin 
		$monitor("time=%0t, a=%d, b=%d, ab_valid=%d, rst=%d, z=%d, z_valid=%d, ab_ready=%d", $time, a, b, ab_valid, rst, z, z_valid, ab_ready);
	end	
	
	// Dump Variables
	initial begin 
		$dumpfile("waves.vcd");
		$dumpvars;
		
	end
	
endmodule