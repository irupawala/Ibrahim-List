`timescale 1ns/1ps

module tb;
reg clk;
real tp, freq, duty;
real jitter_factor, tp_jitter, jitter;
real prev_edge_time, cur_edge_time, tp_calc, freq_calc;

always begin
	jitter_factor = $urandom_range(100-jitter, 100+jitter)/100.0;
	tp_jitter = tp*jitter_factor;
	clk = 1; #(tp_jitter * (duty/100));
	clk = 0; #(tp_jitter * ((100-duty)/100));
end

// Use a separate initial block for command line argument parsing
initial begin
	// Parse the command line argument
	$value$plusargs("freq=%f", freq); //in MHz
	$value$plusargs("duty=%f", duty); //in MHz
	$value$plusargs("jitter=%f", jitter); //in MHz
	// Convert the frequency to time period
	tp = 1000.0 / freq; // in ns
	
	#200;
	$finish;
end

// Dump the waveforms to a VCD file
initial begin 
	$dumpfile("clock.vcd");
	$dumpvars;
end

always @(posedge clk) begin
	prev_edge_time = cur_edge_time;
	cur_edge_time = $realtime;
	tp_calc = cur_edge_time - prev_edge_time;
	freq_calc = 1000/tp_calc; // ns to MHz conversion equation
	$display("freq_cal = %f", freq_calc);


end

endmodule


// to run this code enter the following in Run Options
// +freq=50 +duty=20 +jitter=50
// The command for running this in iCarus is not known