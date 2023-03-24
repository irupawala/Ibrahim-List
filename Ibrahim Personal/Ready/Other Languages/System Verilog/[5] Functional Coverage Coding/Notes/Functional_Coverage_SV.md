## [2] Coverage Analysis in Verification

### Coverage

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\1.JPG)

### Code Coverage

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\2.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\3.JPG)

### Functional Coverage

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\4.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\6.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\7.JPG)

## [3] Covergroups and Coverpoints

### Covergroup and Coverpoint Syntax

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\8.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\9.JPG)

### Covergroup and Coverpoint examples

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\10.JPG)



## [4] Using Coverage Bins

### Automatic Array of Bins

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\11.JPG)



### Default Bins

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\12.JPG)



### Adding Conditions to sample a signal

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\13.JPG)



## [5] Transition Bins

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\14.JPG)



## [6] Bins Generated Automatically

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\15.JPG)

## [7] Wildcard Bins

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\16.JPG)

## [8] Ignore & Illegal Bins

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\17.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\18.JPG)

## [9] Cross Coverage

### Cross Coverage Definition

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\19.JPG)

* Variables can also be specified instead of coverage point name. This can be a variable name or a coverpoint name shown in the example above `validXaddr: cross valid, addr_range;`
* When a variable name is used then explicitly all the cover points of the variables will be created and it will be crossed with other variable defined.

### Bins in Cross Coverage

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\20.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\21.JPG)

* Notice here that && produces 4*4 = 16 bins in the example shown above.

### Ignoring unwanted cross products

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\23.JPG)

* **When you define cross products by default all the individual listed bins of the individual cover points are crossed together.**
* **Now there are few sets of values which are not relevant when you crossed them together.**
* **There are two possible options.** 
  * **Either to specify all the valid combinations of two crossing cover point.**
  * **Or to ignore few cover points which are not relevant.**
* **If you specify few bins of cross coverage as ignore bins then all other bins which are not listed in ignore bins will be considered for cross product.**
*  Thus while creating cross coverage we have two options
  * Either to list all the valid bins
  * specify all the invalid bins using the ignore_bins keyword.
* Instead of ignore_bins one can also use illegal_bins which will flag an error if the listed bin is a hit.
* Illegal bins are more often used to flag an error when you don't want the bins from two cover points to cross each other which can be an illegal scenario. Also notice that it can be possible that a single bin is not a problem but when they cross then the illegal scenario hits in the simulation.

### Generate Only Cross Coverage

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\24.JPG)

* When weight = 0; both the coverage point will not be counted towards final coverage and only cross coverage will be counted as it is given weight other than 0.
* **ALWAYS REMEMBER THAT ALL THE CROSS COVERAGE INDIVIDUAL COVERPOINTS ARE SAMPLED AT THE SAME TIME AT THE POSEDGE OF THE CLK.** 
* Hence here both the address and data coverage point are sampled at the same posedge of the clk when defined as cross coverage.
* Also when the individual cover point in the cross coverage listing is using an array of bins then every element in the array bin will be crossed with other coverpoint bins.



## [10] Coverage Options

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\34.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\35.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\36.JPG)



### Type Options

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\37.JPG)



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\39.JPG)



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\40.JPG)



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\41.JPG)



## [11] Bind a Module to an instance

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\42.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\43.JPG)



## [12] Parameterized Covergroup

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\44.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\45.JPG)



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[5] Functional Coverage Coding\Images\46.JPG)