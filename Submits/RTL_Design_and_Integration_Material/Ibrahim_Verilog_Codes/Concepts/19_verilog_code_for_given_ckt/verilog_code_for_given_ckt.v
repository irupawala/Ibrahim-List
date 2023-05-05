// Refer the lecture's slides for the schematic of these circuits

// Ibrahim's Code
module dff (d, clk, res, q);
	input d, clk, res;
	output reg q;
	
	always @ (posedge clk)
		if (res == 1) q = 0;
		else q = d;
endmodule

module sample (a, b, c, clk, res, y, w);

	input a, b, c, res, clk;
	output y, w;
	wire n1, n2;
	
	and u1 (n1, a, b);
	not u2 (n2, c);
	
	dff d1 (.d(n1), .clk(clk), .res(res), .q(y));
	dff d2 (.d(n2), .clk(clk), .res(res), .q(w));
	
endmodule

// Sreenivasan's Code

module sample (a, b, c, clk, res, y, w);

	input a, b, c, res, clk;
	output reg y, w;
	wire n1, n2;
	
	always @(posedge clk) begin 
	if (rst == 1) begin 
		y = 0;
		w = 0;
	end
	else begin 
		y = a & b;
		w = ~c;
	end
	end
endmodule


// 2nd Example
module sample(a, b, rst, clk, Y);
	input a, b, rst, clk;
	output reg Y;
	wire n1, n2;
	//always @(*) begin 
	//	n2 = n1 & b;
	//end
	// always @(n1 or b) n2 = n1 & b;
	assign n2 = n1 & b;
	
	always @ (posedge clk) begin 
	if (rst == 1) begin
		y = 0;
	end
	else begin 
		n1 <= a;
		y <= n2;
	end
	end
	
endmodule