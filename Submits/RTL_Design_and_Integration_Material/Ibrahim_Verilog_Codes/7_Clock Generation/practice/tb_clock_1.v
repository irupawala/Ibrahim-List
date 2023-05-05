//100Mhz => 10ns
// hence clock period is 10ns hence both positive and negative clocks will be 5ns each
// by default time unit in verilog and precision is 1ns/1ns

module tb;
reg clk;
real tp, freq;

// Use a seprarate initial block for command line argument passing
initial begin 
	$value$plusargs("freq=%f", freq); //in MHz
	// convert frequency to time period
	tp = 1000 / freq; // in ns
end

initial begin 
	forever begin
		#5 clk = 0;
		#5 clk = 1;
	end
end


// dump waves
initial begin 
	$dumpfile("waves.vcd");
	$dumpvars;
	#200;
	$finish;
end

endmodule
