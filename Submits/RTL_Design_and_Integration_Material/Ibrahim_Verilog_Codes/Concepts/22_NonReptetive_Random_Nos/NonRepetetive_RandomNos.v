module tb;

parameter COUNT=30;
parameter BASE=40;
integer intA[COUNT-1:0];
integer i, j, num_exists_f, num;

initial begin 
	for (i=0; i < COUNT; ) begin 
	num = $urandom_range(BASE, BASE+COUNT-1);
	num_exists_f = 0; // start with assumption that, number is not present in array
	
		for (j=0; j < i; j = j + 1) begin 
			if (intA[j] == num) begin 
			j = i; // it will help exit the loop
			num_exists_f = 1;
			end
		end
		
		if (num_exists_f == 0) begin 
			intA[i] = num;
			i = i + 1;
		end
	end

	for (i=0; i < COUNT; i = i+1) begin 
	$display("intA[%0d] = %0d", i, intA[i]);
	end
end
endmodule

// Observe the numbers in the output are repetetive