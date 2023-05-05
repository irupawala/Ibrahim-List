module tb;

integer p, q, r;

initial begin 
	p = 10;
	q = 20;
	
	r = add(p, q);
	$display("r = %0d", r); // returned value is assigned to r

end



function integer add (input integer a, input integer b);
begin 
	add  = a + b; // output of the function is assigned to the function name itself
end
endfunction

endmodule
