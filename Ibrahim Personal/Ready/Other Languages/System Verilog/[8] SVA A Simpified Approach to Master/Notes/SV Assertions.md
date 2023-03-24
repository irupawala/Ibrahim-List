## [2] Introduction to Assertions

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\1.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\2.JPG)

* Design engineers will write white box assertions that is the ones which are specific to the DUT behavior but verification engineers will be writing black box assertions which are not specific to the DUT behavior.
* Formal verification is a technique to verify the behavior of the DUT using Math models. you will not be injecting any stimulus like functional verification but its all about using math models.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\3.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\4.JPG)

* Design errors are caught at an early stage of design development and also it is used to capture the corner cases.



## [3] Types of Assertion

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\5.JPG)

* Immediate Assertion - Checking if specific condition has occurred in the simulation.
* Concurrent Assertion - Checking for the sequence in the simulation
* Immediate is added in procedural block always, always_comb. will be treated like all other statements in the procedural blk.
* concurrent is added outside procedural blk but could be in a module.
* immediate is evaluated in single point of time while concurrent in multiple clock cycles



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\6.JPG)



* assert - if the property is violated in simulation then an error will be flagged
* assume - property is treated as assumption but in simulation it will be again treated as obligation and will throw an error if violated.
* assume is used for formal verification but for simulation based verification both are same.
* cover - checks if the property has occured or not in the simulation
* restrcit - formal based verification keyword. Not used in simulation based env
* assert and cover from all 4 are only used in simulation based env

## [4] Immediate Assertion

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\8.JPG)



* Difference between assert and if is that if is not synthesizable RTL Code and if is used for checker code.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\9.JPG)

* Not advisable to use $error
* $fatal will kill the simulation immediately with an error message. $error will only show error and won't kill the simulation

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\10.JPG)

## [5] Concurrent Assertions

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\12.JPG)

* Main difference between immediate and concurrent is property keyword.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[8] SVA A Simpified Approach to Master\images\13.JPG)



* Second style is more recommended as it can be used to write the coverage for the property.
* cover will check whether the given property has been acquired in the simulation or not. that is if this property has been true at any point of time in the simulation.



!