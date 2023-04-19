module tb;
reg clk;

always begin
	clk = 1; #5;
	clk = 0; #5;
end

initial begin 
	#200;
	$finish;
end


initial begin 
	$dumpfile("clock.vcd");
	$dumpvars;
	end
endmodule
