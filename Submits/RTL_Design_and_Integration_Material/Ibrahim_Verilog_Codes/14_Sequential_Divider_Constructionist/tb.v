`include "sequential_divider.v"

module tb;
	// Declare IO's
	parameter NUM_LENGTH = 5;
	parameter DEN_LENGTH = 3;	
	integer seed = 123135;
	
	reg [NUM_LENGTH-1:0] num;
	reg [DEN_LENGTH-1:0] den;
	reg nd_valid;
	reg clk;
	reg rst;
	
	wire nd_ready;	
	wire qr_valid;
	wire [NUM_LENGTH-1:0] quo;
	wire [DEN_LENGTH-1:0] rem;
  	reg [7:0] clk_cnt;
    
  sequential_divider #(.NUM_LENGTH(NUM_LENGTH), .DEN_LENGTH(DEN_LENGTH)) DUT (.num(num),
                .den(den),
                .nd_valid(nd_valid),
                .nd_ready(nd_ready),
                .clk(clk),
                .rst(rst),
                .qr_valid(qr_valid),
                .quo(quo),
                .rem(rem));

	// Declare clk
	initial begin 
		clk = 0;
		forever #1 clk = ~clk;
	end 
  
	// Drive Inputs
	initial begin 
		rst = 0; 
		#5;
		rst = 1;
		#5;
		/*
        nd_valid = 1;
		num = 26;
		den = 5;
        */
      
      repeat (100) begin 
			@(posedge clk) begin
              	nd_valid = $random(seed);
				num = $random(seed);
				den = $random(seed);
			end
		end
		@(posedge clk) begin 
				nd_valid = 0;
			end		
      
		#50;
		$finish();
      
	end 
	
	initial begin 
      $monitor("time=%0d num=%d den=%d nd_valid=%d rst=%d quo=%d rem=%d qr_valid=%d nd_ready=%d", $time, num, den, nd_valid, rst, quo, rem, qr_valid, nd_ready);
	end	
	
	// Dump Variables
	initial begin 
		$dumpfile("waves.vcd");
		$dumpvars;
		
	end
	
endmodule  