module tb;

integer a, seed;
initial begin 
	seed = 1033932;
	repeat(5) begin 
		a = $random(seed);
		$display("a=%d", a);
	end
end
endmodule