## [4] Generic UVM based Testbench Structure

* In UVM agent class there will be 3 other classes: Monitor, Driver and Sequencer.
* Sequence class can also contain multiple transaction classes.
* DUT is only interacting with Driver and Monitor class of the agent.
* DUT won't interact with Environment, Sequencer,etc directly at all.
* An Environment can have multiple UVM Agent but a UVM test bench will only have one test.
* Also there can be multiple sequences and each sequence may contain multiple transactions.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[6] UVM in System Verilog\Images\1.JPG)



## [5] Writing UVM Classes in General

 ![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[6] UVM in System Verilog\Images\2.JPG)

* Generalized form of any UVM based class applicable to all the derived classes uvm_test, uvm_env, uvm_agent, etc.
* If you are writing test you will be extending from uvm_test and if you are writing env you will be extending from uvm_env.
* First line after the declaration should be Factory Registration which will be common for all the components uvm_test, uvm_env, etc.
* Factory Reg is mechanism used to reuse the derived uvm components without changing the code at several places.
* **With every  uvm direct class we have to give FR macro immediately after the first line of class definition**

* Only classes interacting with DUT is driver class and monitor class hence the dut_intff_h will be part of only driver and monitor. **None other class will have virtual interface handle**
* Next you have to list all the classes. Say if it is for agent then you have to declared sequencer, driver and monitor classes.
* After that write all the functions and tasks specific to the uvm components.
* Note the first line in this uvm_component will be name of the component derived. For env it will be uvm_env, for agent it will be uvm_agent and so on.

## [6] Writing Data Classes

* There are only data classes to be used in uvm based TB which are class to represent your sequence and a class to represent your transaction.
* sequences are extended from uvm_sequence.
* transactions are extended from uvm_sequence_item.
* Note here that after the FR you list down all the data members of the transaction **class. rand bit [3:0] length; rand bit [31:0] data[];**
* Here constraint is added to limit the randomness of the data members length and data listed above to generate the valid stimulus to the DUT.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[6] UVM in System Verilog\Images\3.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[6] UVM in System Verilog\Images\4.JPG)

* Notice that task body() is a specific to uvm sequence class. This is where you will write the functionalities of class in the uvm sequence.
* You will not find body task in uvm_components or uvm_sequence_item.

## [7] First UVM TB Example

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[6] UVM in System Verilog\Images\5.JPG)

* Notice that all the run_phase tasks of all the components will be called at time 0.
* Study the example written on EDA Playground.
* In a large UVM based TB you have environment written once and you will have many test classes generating different combinations of sequences. In a typical environment you will be writing the behavioral parts like agents, drivers once and after that you will be writing large number of sequence classes and also large number of test classes. Any particular test class will start the corresponding sequence class. 
* Then all these are test and sequences are compiled together. Then during runtime you can pass the test which we want to run on the DUT one by one or during different simulations.