module tb;
	reg [5:0] a, b, c, delay;
always @(a) begin // once always is running, other always iteration can't run.
	$display("%t: ENTRY", $time);
	#10 b = a;
	#5 c = b;
end

initial begin 
	repeat(30) begin 
		delay = $urandom_range(5, 10);
		#delay;
		a = $random%100; // random number betweeb 0 to 99
	end
	#100;
	$finish;
end 
endmodule