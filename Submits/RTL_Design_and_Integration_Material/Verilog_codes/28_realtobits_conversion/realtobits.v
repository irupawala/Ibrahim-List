module tb;
real pie, r_out;
reg [63:0] v;

initial begin 
	pie = 3.1415; // pie value ==> number
	v = $realtobits(pie);
	$display("v = %b", v);
	r_out = $bitstoreal(v); //bit_vector --> real value
	$display("r_out = %f", r_out);

end
endmodule


