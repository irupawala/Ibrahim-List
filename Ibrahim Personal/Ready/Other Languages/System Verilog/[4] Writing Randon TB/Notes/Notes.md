## [2] Random Variables in SV

### Random Variables

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\1.JPG)

### Random Variables in Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\2.JPG)

* Here to set different data packets to your DUT you have to create objects of the packet with different  address and data members. **This is Directed programming approach.**
* In this approach you have to create object for all the random packets you need to send to the DUT. Hence as the number of packets increases complexity of your program increases.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\3.JPG)

* Instead of the direct programming if we can make data members of the class itself as random then we can avoid assigning values to each data member of the class individually in each object declaration. To do this we have to just add the keyword "rand" before the data type declaration.
* Notice here when we write `p1=new()` there is no values getting assigned to the members of the class. Handle of the object is just created.
* All the data members will get assigned when you call the function randomize() on the object of class. Hence the advantage here is we don't need to assign individual values to each data members.
* Notice that if there is any issue with randomization of the data members (can be with constraints given), object.randomize() function will return false.
* Hence one should always call randomize function with the assert statement. what assert statement will do is that it will print the error message whenever there is any error mentioning the object which encountered error.

## [3] Limit the Randomness

* Constrains can be added to random declaration to limit the randomness.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\5.JPG)

* Notice that while adding the constrains to a data member you should ensure that constrains does not contradict each other otherwise randomization will fail giving the false message.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\6.JPG)

## [4] Control the Randomness

### Weighted Distribution within constraint

* Notice that in the previous topic when we declare the values as random using `rand logic [7:0] address` then the probability of getting any value is equal but lets say if we want to give priority to any particular values then we can add distribution to the random variables and this is added using dist operator in SV.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\7.JPG)

### Controlling Multiple Constraint Blocks

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\8.JPG)

* Notice here in the example given when we do p1.d_short.constraint_mode(0) then only d_short constraints turns off but when we do p1.constraint_mode(0) then all the constraint turns off.

### Inline Constraints

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\9.JPG)

## [5] Pre & Post Randomize functions 

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\10.JPG)

* Notice in this case we want crc as xor of data hence even when we have written the crc as rand during the declaration the crc will get overwritten with the ^data values in the post random function.

### Random Number Functions

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\11.JPG)

## [6] Random Control

### Randcase

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\12.JPG)

* Notice that previous methods discussed randomizes the member of the class while this Random control method can randomize the individual data members within the program.
* Also one can add multiple statements to the single rand case by adding the statements between begin and end.

## [7] Random Scenario Generator

### Random Scenario Generator

* Till now we have seen how to randomize a single packet or a single statement but this is not enough to create a real time random stimulus for a DUT. The reason is you may want to create random scenarios as well.
* We can create random scenarios using random packets.
* Consider a DUT to which we want to send memory/processor transactions back to back. Sometimes we want to send only memory transactions back to back, sometimes only processor while sometimes both mem and processor trans back to back. This stream of transactions is called sequence in SV.
* `randsequence` command helps to generate random sequences as per the user need.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\13.JPG)

### Randsequence_1

* In the example below main is the **first** production name given in a round brackets of the rand sequence.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\14.JPG)

* Notice that production contains a name and a list of other **productions**

* **Productions** are further classified into terminals and non terminals.

### Randsequence_2

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\15.JPG)

* Notice here that cfg_read production selects randomly between the two tasks given and writing cfg_read at the end of the production will again call this production and that's how a sequence of cfg_read_task is generated.
* But notice here that instructor has not made it clear on how the production loop will get terminated.
* Also note that probability of selecting any production in `stream` and any tasks within the production is equal. SV also allows adding weight to the production branches.
* Observe the image below for a new statement for production stream.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\16.JPG)



## [8] Typical SV Test bench structure

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\17.JPG)

### A Simple TB Example

Example of a Simple DUT and TB program.

The DUT is a counter with 3 inputs (clock, reset and up/down count) and a single output count of parametrized width. The testbench module name is counter_tb(). It instantiates counter with name counter_1 with a change is parameter width. A clock generator toggles the 'clk' signal in every #10 time unit. Since the time unit is set to 1ns, the clk toggles on every 10ns resulting a clock time period of 20ns.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\18.jpg)

*In the initial clock, after asserting reset, the up/down count signal is set 1 for 20 clocks, 0 for 12 clocks and again 1. Thus the counter counts from 0 to 20 (0x14) , then 19 (0x13) to 8 and so on. Below is the simulation waveform.*

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\19.jpg)



## [9] Class Based SV TB Structure

* Notice the conventional TB shown below, the disadvantage of this TB is that it is not reusable at all.
* Hence when verifying a complex DUT it is highly recommended to use class based TB.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\20.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\21.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\22.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\23.JPG)

* DUT is connected to driver using virtual interface. Transaction/ Generator are connected to Driver using inbuilt methods like Mailboxes.
* A wrapper around all these TB components is called as Environment. All the TB components are instantiated in the environment class and are connected together.

## [10] Coding a class based random TB

### Command Specification

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\24.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\25.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[4] Writing Randon TB\Images\26.JPG)





 ### Refer the TB Code snapshots in the course folder



