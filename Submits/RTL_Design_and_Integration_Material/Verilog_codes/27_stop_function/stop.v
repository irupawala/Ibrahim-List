module tb;
reg [7:0] a;
initial begin 
	#10;
	a = $random;
	$stop; // 1st break point => temnporarily stop the simulation, analyze the results, then run(continue) the simulation again
	#20;
	a = $random;
	$stop; // 2nd break point 
	#25;
	a = $random;
	$stop; // 3rd break point 
	#35;	
	a = $random;
	$stop; // 4th break point 
	#35;	
	a = $random;
	$finish; // finish simulation
end
endmodule