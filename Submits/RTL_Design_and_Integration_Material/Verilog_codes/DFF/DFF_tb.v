`include "DFF.v"

//How to write a verilog code  Hardware description language 
//1. synthesisable code - can be made into a chip  
//2. non-synthesisable code - cannot be made into a chip
// Verilog gives us a flexibility with a set of constructs
  
// Can be synthesised 
// module
// function 
// for block 
// case  (like a mux)
// if else block (like a mux)
// and or xor nor nand  
// wire and reg 
// always block 

// Cannot be synthesised 
// task 
// integer
// real 
// time
// initial block 

// Example of wire : 
// if a is wire 
// a=b; // we will not get it in next simulation time
// if a as reg; 
// a=b; // get in the next simulation time 



// Dflipflop - in a dataflow method 



module tb;
  reg clk;
  reg reset_n;
  reg data;
  wire q;
  
  dff dut (clk,reset_n,data,q);
  
  initial begin 
    clk='b0;
    forever #10 clk=~clk;
  end 
  
  initial begin
    #15 reset_n=0;
    #15 reset_n=1; data=1;
    #15 reset_n=1; data=0;
    #15 reset_n=1; data=1;
    #15 reset_n=1; data=0;
    #15 reset_n=1; data=1;
    #15 reset_n=1; data=0;
    #15 reset_n=1; data=1;
    #15 reset_n=1; data=0;
    #15 reset_n=1; data=1;
    #15 reset_n=1; data=0;
  end 
  
  initial begin 
    $dumpvars(0,tb);
    $dumpfile("dump.vcd");
    $monitor("clk =%d, reset_n=%d, data=%d, q=%d",clk,reset_n,data,q);
    #300 $finish;
  end 
endmodule 



