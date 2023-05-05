module tb;
integer n, i, j, prime_count, prime_f;


initial begin
	n = 1000;
	prime_count = 0;
	// prime number between 1 to number
	i = 2;
	while (i <= n) begin
		prime_f = 1; // start with assumption that 'i' is a prime number
		// algorithm: if there is a divisor (2 to i-1) for i, then its not a prime number
		// number is always divisible by 1 and same number (i)
		j = 2;
		while (j <= i/2) begin 
		//while (j <= i/4) begin // 2,3,4... to 23, no point dividing by 23 onwards if not divisible by 2 to 23, we can do uptill j <= sqrt(i)
			if (i % j == 0) begin 
				prime_f = 0;
				j = i; //once we provide that, its not a prime number, don't continue further (SV: break can be used)
			end
			j=j+1;
		end
		if (prime_f == 1) begin 
			$display("Prime number=%0d", i);
			prime_count = prime_count + 1;
		end
		i = i + 1;
	end
	
	$display("Prime number count=%0d", prime_count);
	
end

endmodule

