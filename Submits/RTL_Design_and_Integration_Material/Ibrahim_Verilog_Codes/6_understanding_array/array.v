module tb;

integer intA1 [9:0];
integer intA [9:0];
integer i;

initial begin 
	for (i=0; i<10; i++) begin 
		intA1[i] = $urandom_range(40, 60);
	end 
	
	// Another for loop, print array values.
	for (i=0; i<10; i++) begin 
	//$display("index=%0d, value=%0d", i, intA1[i]); //%0 means no space 
	$display("intA1[%0d]=%0d", i, intA1[i]); //%0 means no space 
	end
	
	for (i=0; i<10; i++) begin 
		intA[i] = intA1[i];
	end 
	
	// Another for loop, print array values.
	for (i=0; i<10; i++) begin 
	$display("intA[%0d]=%0d", i, intA[i]); //%0 means no space 
	end	
	
	
	// compare the arrays
	for (i=0; i<10; i++) begin 
		if (intA[i] == intA1[i]) begin 
			$display("compare passed for index=%0d", i);
		end
		else begin 
			$display("compare FAILED for index=%0d", i);
		end
	end
	
	for (i=0; i<10; i++) begin 
		intA[i] = intA[i] + 1;
	end	
	
	// compare the arrays
	for (i=0; i<10; i++) begin 
		if (intA[i] == intA1[i]) begin 
			$display("compare passed for index=%0d", i);
		end
		else begin 
			$display("compare FAILED for index=%0d", i);
		end
	end	
	
	
end 
endmodule