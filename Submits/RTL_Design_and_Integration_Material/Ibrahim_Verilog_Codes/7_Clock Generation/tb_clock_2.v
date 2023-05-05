`timescale 1ns/1ps

module tb;
reg clk;
real tp, freq;


// Use a separate initial block for command line argument parsing
initial begin
	// Parse the command line argument
	$value$plusargs("freq=%f", freq); //in MHz
	// Convert the frequency to time period
	tp = 1000.0 / freq; // in ns
	
	#200;
	$finish;
end

always begin
	clk = 1; #(tp/2);
	clk = 0; #(tp/2);
end

// Dump the waveforms to a VCD file
initial begin 
	$dumpfile("clock.vcd");
	$dumpvars;
end

endmodule


// to run this code enter the following in Run Options
// +freq=50 +duty=20 +jitter=50
// The command for running this in iCarus is not known