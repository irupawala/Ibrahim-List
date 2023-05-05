//`include "parametarizable_full_adder.v"

module tb;
	// 1. Declare the variables
	parameter WIDTH = 2;
	reg [WIDTH-1:0] a, b;
	reg cin;
	wire [WIDTH-1:0] sum;
	wire cout;

	//2. Instantiate the design 
	// parameter overriding by position
	param_adder #(WIDTH) dut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout)); //parameter overriding. overriding WIDTH here 
	// changes it in design as well
	
	// parameter overriding by name
	//fa_nbit #(.WIDTH(WIDTH_XYZ)) dut(a, b, ci, s, co);
	
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
