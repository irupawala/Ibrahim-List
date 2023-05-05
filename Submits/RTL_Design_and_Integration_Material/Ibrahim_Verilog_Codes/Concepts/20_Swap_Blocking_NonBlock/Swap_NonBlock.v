module swap_non_block;
integer a, b;

initial begin 
	#0; a = 10; b = 20;
	#10 $display("a=%0d, b=%0d", a, b); // a=20, b=10
end

initial begin 
	#5;
	a <= b; //value of a doesn't get assigned to b immediately, it is stored in to temp variable (b_t)
end 


initial begin 
	#5;
	b <= a; 
end


endmodule
