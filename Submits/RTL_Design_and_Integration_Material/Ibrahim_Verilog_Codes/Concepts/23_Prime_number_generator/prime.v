module tb;
integer n, i, j, prime_count, prime_f;
//reg prime_f;

initial begin
	n = 1000;
	prime_count = 0;
	// prime number between 1 to number
	for (i=2; i <= n; i = i+1) begin
		prime_f = 1; // start with assumption that 'i' is a prime number
		// algorithm: if there is a divisor (2 to i-1) for i, then its not a prime number
		// number is always divisible by 1 and same number (i)
		//for (j=2; j <= i-1; j=j+1) begin 
		for (j=2; j <= i/2; j=j+1) begin 
			if (i % j == 0) begin 
				prime_f = 0;
				j = i; //once we provide that, its not a prime number, don't continue further (SV: break can be used)
			end
		end
		if (prime_f == 1) begin 
			$display("Prime number=%0d", i);
			prime_count = prime_count + 1;
		end
	end
	
	$display("Prime number count=%0d", prime_count);
	
end

endmodule

