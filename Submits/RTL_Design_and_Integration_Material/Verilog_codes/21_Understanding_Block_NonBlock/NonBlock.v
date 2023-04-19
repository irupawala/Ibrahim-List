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

// Here Q1, Q2, Q3 are holding previous values hence 3 FF's are required
// Q1 will be updated in first posedge of clk, Q2 in next and Q3 in next to next
// with Non-Blocking statements update only happens at the end of the timestep hence order of the statements does not matter (This is not the case with Blocking statements)
// Using Non-Blocking statements 3 FF's are required always
always @(posedge clk) begin 
	Q1 <= d; 
	Q2 <= Q1;
	Q3 <= Q2;
end

initial begin 
	$dumpfile("1.vcd");
	$dumpvars;
end
endmodule