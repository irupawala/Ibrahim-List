module tb_up_down_counter();
	reg tb_clk, tb_rst, tb_up_down; // default value of reg is x
	wire [2:0] tb_count;
	integer delay;
	
	// instantiate the design 
	up_down_counter_behav DUT (.clk(tb_clk), .rst(tb_rst), .count(tb_count), .up_down(tb_up_down));
					
	// Monitor output
	initial begin
		$monitor("time - %0t, clk = %d, rst = %d, , up_down = %d, count = %d", $time, tb_clk, tb_rst, tb_up_down, tb_count);
	end
	
	/*
	// clock generation 
	initial begin 
		tb_clk = 0;
		//repeat (200) begin 
		forever begin
		#50 tb_clk = ~tb_clk;	
		end
	end
	*/
	
	/*
	// clock generation
	initial begin 
		tb_clk = 0;
	end
	always begin
		#50 tb_clk = ~tb_clk;	
	end
	*/
	
	// clock generation
	always begin 
		tb_clk = 0; #50;
		tb_clk = 1; #50;
	end
	
	/*
	// Drive Inputs
	initial begin 
		tb_rst = 1;
		#100;
		tb_rst = 0;
		tb_up_down = 0; // down_counter
		// count will start automatically
		// let the count happen for sometime, then end the simulations ($finish)
		#500;
		tb_up_down = 1;
		#500;
		tb_up_down = 0;
		#500;
		tb_up_down = 1;
		#500;
		tb_up_down = 0;		
		#500;
		$finish;
	end
	*/
	
	// Drive Inputs
	initial begin 
		tb_rst = 1;
		#100;
		tb_rst = 0;
		tb_up_down = 0; // down_counter
		repeat (50) begin 
			tb_up_down = $random;
			delay = $urandom_range(50, 200); //u: unsigned(+number), random_range: number in the range
			#delay;
		end 
		#1000;
		$finish;
	end	
	
	initial begin 
		//$dumpvars(0, tb_2x1Mux);
		$dumpfile("tb_up_down_counter.vcd");
		$dumpvars; // This should always come after dumpfile
	end
endmodule