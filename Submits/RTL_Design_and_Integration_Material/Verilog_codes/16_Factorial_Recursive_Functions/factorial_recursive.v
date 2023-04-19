module tb;
	integer a, fact;
	initial begin 
		a = 5;
		fact = factorial(a);
		$display ("fact = %0d", fact);
	end
	
	// here the answer is always one because the function is static in nature 
	// factorial method is getting called 5 times, each time memory location gets updated => the final value impacts all earlier calculations => static function 
	
	// factorila method is getting called 5 times, each time different memory location gets used for each output => the final value won't impact all earlier calculations => automatic function 
	function automatic integer factorial (input integer a);
	begin 
		if (a > 1) factorial = a * factorial(a-1);
		else factorial = 1; 
	
	end
	endfunction 
endmodule