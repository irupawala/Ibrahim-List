module seqDiv #(parameter LENGTH = 4) (
	input logic [LENGTH-1:0] num,
	input logic [LENGTH-1:0] den,
	input logic nd_valid,
	output logic nd_ready,

	input logic clk,
	input logic rst,

	output logic qr_valid,
	output logic [LENGTH-1:0] quo,
	output logic [LENGTH-1:0] rem
	);


	logic [1:0] state_reg, state_next;
	parameter idle = 2'b00;
	parameter div = 2'b01;
	parameter undefined_div_by_0 = 2'b10;

	logic [LENGTH-1:0] quo_reg, quo_next;
	logic [2*LENGTH:0] rem_reg, rem_next;
	logic [2*LENGTH-1:0] divisor_reg, divisor_next;
	logic nd_ready_reg, nd_ready_next;
	logic qr_valid_reg, qr_valid_next;
	logic [LENGTH-1:0] counter_reg, counter_next;

		
	  
	always_ff @ (posedge clk or negedge rst)
	begin
	if (~rst)
		begin
			quo_reg <= LENGTH'b0;
			rem_reg <= 'b0;
			divisor_reg <= 'b0;
			nd_ready_reg <= 1'b1;
			qr_valid_reg <= 1'b0;
			counter_reg <= LENGTH'b0;
			state_reg <= idle;
		end
		else begin
			quo_reg <= quo_next;
			rem_reg <= rem_next;
			divisor_reg <= divisor_next;
			nd_ready_reg <= nd_ready_next;
			qr_valid_reg <= qr_valid_next;
			counter_reg <= counter_next;
			state_reg <= state_next;
		end
	end
  
	always_comb begin
		quo_next = quo_reg;
		rem_next = rem_reg;
		divisor_next = divisor_reg;
		nd_ready_next = nd_ready_reg;
		qr_valid_next = qr_valid_reg;
		counter_next = counter_reg;
		state_next = state_reg;

		case(state_next) // state_reg
		idle:
		  begin
			nd_ready_next = 1'b1;
			qr_valid_next = 1'b0;
			counter_next = LENGTH'b0;
			if(nd_valid)
			  begin 
				quo_next = LENGTH'b0;
				divisor_next = {den, LENGTH'b0};
				rem_next = {(LENGTH+1)'b0, num};
				nd_ready_next = 1'b0;
				if (divisor_next == 'b0) 
				begin
				  state_next = undefined_div_by_0;
				end
				else
				  begin
				state_next = div;
				  end
				
			  end
			else 
			  state_next = idle;
		  end
		div:
		begin
			rem_next = rem_next - divisor_next;
			if(rem_next[2*LENGTH] == 1'b0)
			begin
			  quo_next = quo_reg << 1'b1; 
			  quo_next = quo_next + 1'b1;
			end
		   
			else
			  begin
				rem_next = rem_next + divisor_next;
			   quo_next = quo_reg << 1'b1;
			  end
			divisor_next = divisor_reg >> 1'b1;
			counter_next = counter_next + 1'b1;

			if(counter_next == LENGTH'd(LENGTH+1))
			  begin
				nd_ready_next = 1'b1;
				qr_valid_next = 1'b1;
				state_next = idle;
			  end
			else
			  state_next = div;
		end

		undefined_div_by_0:
		  begin
			divisor_next = 'b0;
			rem_next = 'b0;
			quo_next = LENGTH'b0;
			nd_ready_next = 1'b1;
			qr_valid_next = 1'b1;
			state_next = idle;
		  end

		  

		endcase
	end

	assign quo = quo_reg;
	assign rem = rem_reg [LENGTH-1:0];
	assign nd_ready = nd_ready_reg;
	assign qr_valid = qr_valid_reg;
  
endmodule


  
  
