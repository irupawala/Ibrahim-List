/*
Works on eDA playground but not on Questasim and iCarus

*/

module tb;

integer arr1[4:0];
integer arr2[4:0];
integer arr3[4:0];
integer i;

initial begin 
  arr1 = '{1,2,3,7,8}; // ' can be skipped as well
	arr2 = '{3,4,5,6,7}; // ' can be skipped as well
	for (i=0; i<5; i=i+1) begin 
		arr3[i] = add(arr1[i], arr2[i]);
	end
	
	for (i=0; i<5; i=i+1) begin 
	$display("arr3[%0d] = %0d", i, arr3[i]); // returned value is assigned to r
	end
end



function integer add (input integer a, input integer b);
begin 
	add  = a + b; // output of the function is assigned to the function name itself
end
endfunction

endmodule
