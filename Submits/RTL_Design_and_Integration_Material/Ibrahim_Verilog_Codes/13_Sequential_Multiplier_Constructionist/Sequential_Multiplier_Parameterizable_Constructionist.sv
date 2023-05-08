// Code your design here
// seqMult.vp
// my $bW = parameter( name=>"bitWidth", val=>16, doc=>"Width of input");

module seq_mult #(parameter Multiplicand_length = 1, parameter Multiplier_length = 1)( 
  input logic [Multiplicand_length-1:0] a, // inputs to the design
  input logic [Multiplier_length-1:0] b,
  input logic ab_valid,
  input logic clk,
  input logic rst,
  output logic ab_ready,
  output logic z_valid,
  output logic [Multiplier_length+Multiplicand_length-1:0] z
);
logic state_reg,state_next; // two  states mult and idle
parameter idle=1'b0;
parameter mult=1'b1;
  logic [Multiplicand_length-1:0] multiplier_reg,multiplier_next; // note here that mult_reg is the value stored in the register while mult_next is the value obtained from the output of the combinational logic
  logic [Multiplier_length+Multiplicand_length-1:0] multiplicand_reg,multiplicand_next;
  logic ab_valid_reg;
  logic [Multiplier_length+Multiplicand_length-1:0] z_reg,z_next;
  logic ab_ready_reg,ab_ready_next,z_valid_reg,z_valid_next;
  always_ff@(posedge clk or negedge rst) // as rst is active low
    begin
      if(~rst) // as rst is active low
        begin 
          multiplier_reg <= 'd0;
          multiplicand_reg <= 'd0;
          ab_valid_reg <= 'b0;
          ab_ready_reg <= 'b1; // if rst ab_ready_reg=1 because then we are indicating that our design is in idle state
          z_valid_reg <= 'b0;
          z_reg <= 'd0;
          state_reg <= idle; // the state of the reg shall remain idle untill the rst is not deactivated 
        end
      else
        begin // when rst is deactivated the values in the register should be loaded with the values obtained from the combinational logic. But does the reg will not get loaded with the values obtained from previous calculations ?
          multiplier_reg <= multiplier_next;
          multiplicand_reg <= multiplicand_next;
          ab_valid_reg <= ab_valid;
          ab_ready_reg <= ab_ready_next;
          z_valid_reg <= z_valid_next;
          z_reg <= z_next; 
          state_reg <= state_next; // here we don't know what the next state will be. This will be decided by combinational logic based on its current mode of operation. If it is busy doing the multiplication next state will be mux. If it has finished computation next state will be idle
        end
    end
  always_comb
    begin
    	  multiplier_next = multiplier_reg; // here why are we assigning the values of the reg back again to the next ??  and how do we transfer the outputs of the reg block to the inputs of the combinational logic ?. Does the combinational logic directly takes the inputs of the reg meaning why are we not conencting the outputs of reg to the inputs of the combinational logic using wires like we did in 525 final project ??
          multiplicand_next = multiplicand_reg;
          ab_ready_next = ab_ready_reg; // here should'nt the value be reg ??
          z_valid_next = z_valid_reg;
          z_next = z_reg; 
          state_next = state_reg;
      case(state_reg)
        idle:
          begin
            ab_ready_next = 'b1;
            z_valid_next = 'b0;
            if(ab_valid_reg)
              begin
              multiplier_next = b; // here shouldn't the values be given to mult_reg and not mult_next if mult_next are we not giving inputs directly to combinational logic ???. Also if we are giving the input here the mult_reg will get the inputs in the next clock cycle
              multiplicand_next = 'd0; // as we want multiplicand to apend the zero's on the right as we are shifting it on the right we are  making the size of the same double the size of the multiplier
              multiplicand_next = multiplicand_next + a; // as we want multiplicand to apend the zero's on the right as we are shifting it on the right we are  making the size of the same double the size of the multiplier
              ab_ready_next = 'b0;
              z_next = 'd0; // here as soon as the inputs are obtained why are we making z_next = 0 ?
              state_next = mult;
              end
            else
              state_next =idle;
          end
        mult:
          begin
            if(multiplier_reg[0] == 'b1) // here we are checking the values of the reg but we have assigned the values of the input to the next, line 59 to 60
            z_next = z_reg + multiplicand_reg;
          else
            z_next = z_reg;
          //$display("Z %b Multiplier_reg %b Multiplicand_reg %b", z_reg,multiplier_reg,multiplicand_reg);
          multiplier_next = multiplier_reg >> 'b1;
          multiplicand_next = multiplicand_reg << 'b1;
            if(multiplier_reg == 'd0)
              begin
                ab_ready_next = 'b1;
                z_valid_next = 'b1;
                state_next = idle;
              end
            else
              state_next = mult;
          end
      endcase
    end
assign ab_ready = ab_ready_reg; // here as soon as we are finishing calculations we transfer the values of these to the final output
assign z_valid = z_valid_reg;
assign z = z_reg;        
endmodule