module tb;
	// 1. Declare variables
	reg [7:0] a, b;
	reg sel;
	wire [7:0] out, outbar;
	
	// 2. Instantiate the design
	mux_2_to_1 dut (.a(a), .b(b), .sel(sel), .out(out), .outbar(outbar));

	// 3. Drive Inputs
	initial begin // started at time 0
		repeat (20) begin 
		a = $urandom_range(1, 900);
		b = $urandom_range(1, 900);
		sel = $random;
		#1;
		end
		// simulation will exit here, since intial functionality has completed
	end // 0 time
	// 4. Monitor Inputs
	initial begin
		$monitor("time = %0t, a = %d, b = %d, sel = %d, out = %d, outbar = %d", $time, a, b, sel, out, outbar);
	end
	
	//5. Log waves
	initial begin 
		$dumpfile("mux.vcd");
		$dumpvars; // This should always come after dumpfile
	end
endmodule
