`timescale 1ns/1ps // time period for 30MHz freq is 33.33ns

//100Mhz => 10ns
// hence clock period is 10ns hence both positive and negative clocks will be 5ns each
// by default time step in verilog and precision is 1ns/1ns

module tb;
reg clk;
real tp, freq, duty;
real jitter_factor, tp_jitter, jitter;

always begin
	jitter_factor = $urandom_range(100-jitter, 100+jitter)/100.0;
	tp_jitter = tp*jitter_factor;
	clk = 0; #(tp_jitter * (duty/100));
	clk = 1; #(tp_jitter * ((100-duty)/100));
end

// Use a seprarate initial block for command line argument passing
initial begin 
	$value$plusargs("freq=%f", freq); //in MHz
	$value$plusargs("duty=%f", duty); //in MHz
	$value$plusargs("jitter=%f", jitter); //in MHz
	// convert frequency to time period
	// equation to convert MHz into ns = 1000/freq ns
	tp = 1000 / freq; // in ns
	#200;
	$finish;	
end

// dump waves
initial begin 
	$dumpfile("waves.vcd");
	$dumpvars;
end

endmodule
