module tb;
	
	parameter ADD = 4'b0001;
	parameter SUB = 4'b0010;
	parameter MULT = 4'b0011;
	parameter DIV = 4'b0100;
	parameter CONCAT = 4'b0101;
	
	integer p, q, alu_result;
	
	initial begin 
		p = $urandom_range(10, 100);
    	q = $urandom_range(10, 100);
		alu_result = alu_func(p, q, MULT);
		$display("p = %0d, q = %0d, alu_result = %0d", p, q, alu_result);
	end
	
	//function reg [31:0] alu_func (input [7:0] a, input [7:0] b, input [3:0] operation); 
	function integer alu_func (input integer a, input integer b, input integer operation); 
	begin
		case (operation)
			ADD : begin 
				alu_func = a + b; // function name itself is an output argument
			end 
				
			SUB : begin 
				alu_func = a - b;
			end
				
			MULT : begin
				alu_func = a * b;
			end
				
			DIV : begin 
				alu_func = a / b;
			end
				
		endcase // note that there is no return argument in system verilog 
	end
	endfunction 	
endmodule
