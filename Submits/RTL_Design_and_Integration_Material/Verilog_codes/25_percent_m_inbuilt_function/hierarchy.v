module sample;
	integer a;
	function reg print(input integer b);
		begin
			$display("a=%m", a);
			// $display("a=%d", a);
			print = 1;
		end
	endfunction
endmodule

module tb;
	real s, f;
	sample s_inst();
	initial begin 
		$display("s=%m", s);
		// $display("s=%f", s);
		s_inst.a = 200;
		f = s_inst.print(50);
	end
endmodule