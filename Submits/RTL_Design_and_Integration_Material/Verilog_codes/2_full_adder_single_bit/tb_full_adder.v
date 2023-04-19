module tb_half_adder();
	reg tb_a; 
	reg tb_b;
	reg tb_carry_in;
	wire tb_sum; 
	wire tb_carry_out;
	
	//instantiate the design
	half_adder dut (.a(tb_a),
					.b(tb_b),
					.carry_in(tb_carry_in),
					.sum(tb_sum),
					.carry_out(tb_carry_out)
					);

	// drive inputs
	initial begin 
		repeat (20) begin 
			tb_a = $random;
			tb_b = $random;
			tb_carry_in = $random;
			#1;
		end
	end 
	
	// dump variables
	initial begin
		$dumpfile("full_adder.vcd");
		$dumpvars;
	end
	
	// monitor outputs
	initial begin
		$monitor("time - %0t, a=%d, b=%d, carry_in=%d, sum=%d, carry_out=%d", $time, tb_a, tb_b, tb_carry_in, tb_sum, tb_carry_out);
	end	
	

endmodule