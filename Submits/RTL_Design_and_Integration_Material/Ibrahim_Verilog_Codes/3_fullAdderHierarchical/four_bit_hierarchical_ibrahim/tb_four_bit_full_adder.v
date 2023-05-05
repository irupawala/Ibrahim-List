module tb_fulladder4();
	reg [3:0] tb_Ain, tb_Bin;
	reg tb_Cin;
	wire [3:0] tb_Sum; 
	wire tb_Cout;
	
	//instantiate the design
	fulladder4 dut (.Cout(tb_Cout),
					.Sum(tb_Sum),
					.Ain(tb_Ain),
					.Bin(tb_Bin),
					.Cin(tb_Cin)
					);

	initial begin // started at time 0
		tb_Ain = 4'd1;
		tb_Bin = 4'd1;
		tb_Cin = 1;
		#1;
		tb_Ain = 4'd2;
		tb_Bin = 4'd5;
		tb_Cin = 0;
		#1;	
		tb_Ain = 4'd3;
		tb_Bin = 4'd7;
		tb_Cin = 1;
		#1;		
		tb_Ain = 4'd15;
		tb_Bin = 4'd1;
		tb_Cin = 0;
		#1;		
		tb_Ain = 4'd15;
		tb_Bin = 4'd15;
		tb_Cin = 1;
		#1;				
		// simulation will exit here, since intial functionality has completed
	end // 0 time
	
	// dump variables
	initial begin
		$dumpfile("tb_fulladder4.vcd");
		$dumpvars;
	end
	
	// monitor outputs
	initial begin
		$monitor("time - %0t, a=%d, b=%d, carry_in=%d, sum=%d, carry_out=%d", $time, tb_Ain, tb_Bin, tb_Cin, tb_Sum, tb_Cout);
	end	
	

endmodule