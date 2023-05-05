module swap_block;
integer a, b;

initial begin 
	#0; a = 10; b = 20;
	#10 $display("a=%0d, b=%0d", a, b); // a=20, b=10
end

// here a will be assigned b, hence a = 20
initial begin 
	#5;
	a = b; //after 5 units, assigning a=b
end 

// now a will be assigned to b, hence b = 20
initial begin 
	#5;
	b = a; // after 5 units, assigning b=a
end


endmodule

// Note that in this example the output will be 20, 20. This is happening because at time #5 both
// the intial blocks a=b and b=a will be executed but as a = b comes first it will eb executed first
// because there is a small delay between the statements.

// Hence over here the output depends on the order of the statements, this is called as Race condition 
// of tb

// if we swap the procedural statements for a=b and b=a, then the output will be 10, 10 

// Ideally order of initial block should not happen the output
// To resolve this race condition we have to use non-blocking assignments