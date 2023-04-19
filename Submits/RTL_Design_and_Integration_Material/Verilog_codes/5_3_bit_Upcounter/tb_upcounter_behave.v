module tb_upcounter_gatelevel();
	reg tb_clk, tb_rst; // default value of reg is x
	wire [2:0] tb_count;
	integer delay;
	
	// instantiate the design 
	upcounter_dataflow DUT (.clk(tb_clk), .rst(tb_rst), .count(tb_count));
					
	// Monitor output
	initial begin
		$monitor("time - %0t, clk = %d, rst = %d, count = %d", $time, tb_clk, tb_rst, tb_count);
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
	
	
	// Drive Inputs
	initial begin 
		tb_rst = 1;
		#100;
		tb_rst = 0;
		#2000;
		$finish;
	end	
	
	initial begin 
		//$dumpvars(0, tb_2x1Mux);
		$dumpfile("tb_up_down_counter.vcd");
		$dumpvars; // This should always come after dumpfile
	end
endmodule