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

// Notice that Q1, Q2, Q3 values are changing only at the posedge clk, even though d is changing at the respective timestamps as shown above
// Here Q1, Q2, Q3 holds only one value hence it requires only one FF
always @(posedge clk) begin 
	Q1 = d; 
	Q2 = Q1;
	Q3 = Q2;
end

//3 FFs are required in the case below as all Q1, Q2, Q3 holds different values
//always @(posedge clk) begin 
//	Q3 = Q2;	
//	Q2 = Q1;
//	Q1 = d; 
//end


//2 FFs are required in the case below as all Q1, Q2, Q3 holds different values
//always @(posedge clk) begin 
//	Q1 = d; 
//	Q3 = Q2;	
//	Q2 = Q1;
//end

// If the values are not inter-dependent than order of the statements does not matter on the output even if we use blocking statements
//always @(posedge clk) begin 
//	Q1 = a; 
//	Q3 = b;	
//	Q2 = c;
//end

initial begin 
	$dumpfile("1.vcd");
	$dumpvars;
end
endmodule