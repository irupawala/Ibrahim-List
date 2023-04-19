module tb;
	reg [3:0] a, b;
	reg ci;
	wire [3:0] s;
	wire co;
	
	fa_4bit dut(a, b, ci, s, co);
	
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