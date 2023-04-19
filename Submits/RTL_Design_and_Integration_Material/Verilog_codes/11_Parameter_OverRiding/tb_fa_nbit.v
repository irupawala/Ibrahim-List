module tb;
	parameter WIDTH_XYZ = 12;
	reg [WIDTH_XYZ-1:0] a, b;
	reg ci;
	wire [WIDTH_XYZ-1:0] s;
	wire co;
	
	// parameter overriding by position
	fa_nbit #(WIDTH_XYZ) dut(a, b, ci, s, co); //parameter overriding. overriding WIDTH here 
	// changes it in design as well
	
	// parameter overriding by name
	//fa_nbit #(.WIDTH(WIDTH_XYZ)) dut(a, b, ci, s, co);
	
	
	// Can also be written using defparam
	defparam dut.WIDTH = WIDTH_XYZ;
	
	initial begin 
		repeat (10) begin
			#1;
			{a, b, ci} = $random; // $random generates 32 bit number
			// ci will get 0th bit of $random 
			// b will get [4:1] bits of $random
			// a will get [8:5] bits of random 
		end	
	end
	
	initial begin
		$monitor("time = %0t : a=%0d, b=%0d, ci=%b, co=%b, s=%0d", $time, a, b, ci, co, s);
	end
	
endmodule