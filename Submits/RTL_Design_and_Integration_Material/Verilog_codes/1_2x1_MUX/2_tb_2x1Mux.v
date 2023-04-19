// include the design
//`include "2x1Mux.v"

// declare the module
module tb_2x1Mux;
	// Declare the variables 
	reg tb_i0, tb_i1, tb_sel; // design inputs are declared as 'reg' variables in TB
	wire tb_y; // design outputs are declared as 'wire' variables in TB
	
	// Instantiate the design
	mux2x1 dut(.i0(tb_i0), .i1(tb_i1), .sel(tb_sel), .y(tb_y));
	
	// drive design inputs
	
	initial begin // started at time 0
		repeat (100) begin 
		tb_i0 = $random;
		tb_i1 = $random;
		tb_sel = $random;
		#1;
		end
		// simulation will exit here, since intial functionality has completed
	end // 0 time
	
	initial begin 
	$monitor("time = %0t - i0=%b, i1=%b, sel=%b, y=%b", $time, tb_i0, tb_i1, tb_sel, tb_y);
	// even though above code is one line, it repeats for whole simulation time,
	// it keeps monitoring and printing throughout the simulation time
	end
	
	initial begin 
		//$dumpvars(0, tb_2x1Mux);
		$dumpfile("mux.vcd");
		$dumpvars; // This should always come after dumpfile
	end
endmodule