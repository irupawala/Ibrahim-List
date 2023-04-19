module tb;
  
  reg [7:0] var1 = 8'b11001100;
  reg [7:0] var2 = 8'b00110011;
  reg [7:0] result1, result2;

  initial begin
  
	$display("var1 = %d, var2 = %d", var1, var2);
	{result1, result2} = concat_func(var1, var2);
    $display("result1 = %d, result2 = %d", result1, result2);
  end
  
  function reg [15:0] concat_func (input reg [7:0] var1, input reg [7:0] var2);
  begin
	var1 = var1 + 2;
	var2 = var2 + 2;
	concat_func = {var1, var2};
  end 
  endfunction
  
endmodule
