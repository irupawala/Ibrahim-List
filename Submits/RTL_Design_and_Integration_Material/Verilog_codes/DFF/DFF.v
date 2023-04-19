// Code your design here
module dff(input clk,   // defaults it datatype as wire
           input reset_n,
           input data,
           output reg q ); 
  
  always@(posedge clk) begin 
    if(!reset_n) 
     begin 
       q<='b0;
     end 
    else 
     begin 
       q<=data;
     end
  end 
endmodule 
