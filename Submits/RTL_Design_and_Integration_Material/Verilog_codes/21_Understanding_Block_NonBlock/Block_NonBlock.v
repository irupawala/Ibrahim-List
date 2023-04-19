module tb;
reg clk;
reg d, Q1, Q2, Q3;

initial begin
	clk = 0;
	forever #5 clk = ~clk;
end

initial begin 
	d = 0; #12;
	d = 1; #10;
	d = 0; #13;
	d = 1; #12;
	d = 0; #10;
	$finish;
end

always @(posedge clk) begin 
	Q1 = d; 
	Q2 = Q1;
	Q3 = Q2;
end

initial begin 
	$dumpfile("1.vcd");
	$dumpvars;
end
endmodule