// Code your design here
`timescale 1ns/1ps // without this line output will be 2.00000/2.0000
module top;
  time t;
  realtime rt;
  
  initial begin 
  	#1.5;
    t = $time;
    rt = $realtime;
    $display("t=%f, rt=%f", t, rt);
  end
  
endmodule
