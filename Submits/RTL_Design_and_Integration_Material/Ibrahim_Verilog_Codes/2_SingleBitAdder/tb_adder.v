`include "parametarizable_full_adder.v"

module tb;
	// 1. Declare the variables
	parameter WIDTH = 4;
	reg [WIDTH-1:0] a, b;
	reg cin;
	wire [WIDTH-1:0] sum;
	wire cout;

	//2. Instantiate the design 
	param_adder DUT (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

	//3. Drive the inputs
	initial begin 
	repeat (20) begin 
		a = $urandom_range(0, 50);
		b = $urandom_range(0, 50);
		cin = $random;
		#2;
	end 
	end
	
	// Display outputs
	initial begin 
		$monitor("time = %0t, a = %d, b = %d, cin = %d, cout = %d, sum = %d", $time, a, b, cin, cout, sum);
	end			

	//4. Dump Signals
	initial begin
		$dumpfile("adder.vcd");
		$dumpvars;
	end	

endmodule
