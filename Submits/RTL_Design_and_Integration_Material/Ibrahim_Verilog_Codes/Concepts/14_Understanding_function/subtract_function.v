module tb;

integer p, q, r;

initial begin 
	p = 10;
	q = 20;
	
	r = subtract(p, q);
	$display("r = %0d", r); // returned value is assigned to r

end



function integer subtract (input integer a, input integer b);
begin 
	subtract  = a - b; // output of the function is assigned to the function name itself
end
endfunction

endmodule
