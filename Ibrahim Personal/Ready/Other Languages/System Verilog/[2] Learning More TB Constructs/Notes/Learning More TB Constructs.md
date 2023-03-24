# [2] Sequential and Parallel Blocks

## Blocks in SV

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\1.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\2.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\3.JPG)

* Notice that in fork-join, the sequence of the statements does not matter as the time at which the statement will be executed is already given in the statement.

## Fork-Join

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\4.JPG)



* Note in the figure above on the right hand side both the begin-end blocks will start at the same time but the individual statements within it will be executed sequentially. Statement 1 and 3 will start executing parallely.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\5.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\6.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\7.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\8.JPG)

* Observe the disable_fork here.
* Note here that as soon as task a gets completed task d will be launched. Hence the remaining statements of task b and c will not be completed. When we use disable_fork these remaining threads a and b will be killed.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\9.JPG)



* Notice here that when fork-join_none is used then all the task gets launched from the beginning itself.
* When join_none is used it will not wait for any of the statements to be completed. The task after join_none will also get started immediately.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\10.JPG)

* Notice that when wait_fork is used the all the tasks within the fork-join statement will get executed and then the next tasks will be launched 
* but notice that it will not wait for task_d() as it is outside. It will be waiting for all the tasks only within the fork-join.

# [3] Inter-process Synchronization & Communication

* Inter-process communication and synchronization is used to communicate between the processes or tasks which has been launched independently or to synchronize between the process.

## Semaphore

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\11.JPG)

* **Semaphore and Named Events - To synchronize between different process**

* **Mail Boxes - To communicate between different events**

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\12.JPG)

* If you have a limited resource then it can be shared with multiple processors and clients using a semaphore.
* Imagine you have a task which is sending command to a DUT and also imagine that other two tasks/ clients/ sequences/ agents are sending commands to this DUT.
* We need to limit the access of the DUT asked to be accessed by these 3 tasks. In this case we use a semaphore.
* In the example below task_a(), task_b() and task_c()  all have the function to send the transaction to the DUT `// send txn`. 
* But DUT can only be accessed by one task at a time as number of keys is 1 sema1 = new(1). In that case we will use a semaphore.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\13.JPG)



* After declaring a semaphore you need to create an instance of it using the new() function.
* After that any client can get the semaphore using the get function.
* After completing the execution, the key needs to be returned back to the resource manager using the put method.
* Both get() and put() are blocking tasks meaning the get() task will block the task_a() until the semaphore key is available.
* To know if any key is available without blocking the task `try_get()` statement is used. It will return a success value if key is available.



* With all these arguments we can pass an optional argument which is number of keys. This is initialized when semaphore is being declared.
* If you are passing 1 then single key will be created and it needs to be managed across different clients.
* If you are passing 3 keys then at a time 3 different clients can get that semaphore.
* But if 4 clients is trying to get the semaphore then it will be blocked.
* The default number of keys is 1.



* **Do not forget to put the key back after the task is used. Only then the other tasks will be able to use the semaphore.**



* **If all the tasks call the semaphore at the same time then any task will get the semaphore. This is not controlled by the user but the simulator.**
*  



## MailBox

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\14.JPG)

* Way to communicate between two different components which does not have any information about each other.
* Most commonly used to communicate between class based tb in system verilog.
* some of the commonly associated methods with mailbox are
  1. new() - will create a mailbox
  2. put() - send something to mailbox
  3. get() - get something from the mailbox

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\15.JPG)

**axi_generator Class:** 

* A class has a constructor called function `new()` which will be present in all the classes in SV. It is a function which will be called every time the class is created. **Notice that function/ constructor name in SV has to be `new().`**
* Within the new() function, the new() function of the mailbox is called again. 
* `mbox = new()`. New function of mailbox is created and returned to a handle mbox. Hence mailbox is created within a class constructor function.
* Notice the user-defined task run(). In this task we are creating transactions and sending some transactions. 
* axi_txn is another class which has not been shown in the example above. It is a class which is representing a transaction.
* In a for-loop the object of the class is created 10 times. This is how object of the class is created in SV.
* And then we are randomizing class object. What has been understood here is when you call randomize function on the object txn it feeds the random values to the member variable. Now txn will have some values to send.
* Next is to send this txn values to somebody, but it doesn't know who is going to consume this transaction hence it is putting the transaction to the mailbox.
* Hence any consumer which is connected to this mailbox can take the transaction and consume it.
* Hence in the generator class it is just putting the transactions into the mailbox named mbox which is a member variable of the class axi_generator.

**axi_driver class:**

* Driver class is one which is sending transaction to DUT.
* It has a virtual interface handle **virtual axi_intf m_intf** which is interface handle pointing to DUT interface.
* This also contains mailbox named mbox. Here also mailbox is created within a class constructor function.
* It also got the task run which is receiving transaction and sending these transactions into the interface.
* It is receiving transaction into the mailbox using mbox.get(txn). Now remember that get() is also a blocking statement meaning it will block until the transaction is seen in the mailbox after that it will proceed further.

**test_bench() :**

* Now in order to use both of these classes in the tb, we need to create the classes and connect them appropriately.
* First 4 lines we are instantiating the interface, DUT, generator and driver respectively.
* In the initial begin block 1. local mbox is instantiated using mbox1 and then 2. instance of driver and generator is created.
* Now notice that before run task of driver and generator is called using the statements inside fork-join, we have to first connect the driver and generator, this is because mbox object within the driver and generator are different objects
* This connection is made using the statements m_gen.mbox = mbox1 and m_driver.mbox = mbox1, here both the mbox are pointing to local mailbox mbox1. 
* Also driver interface is pointed to local interface instantiation as well. m_driver.m_intf=m_intf
* Also notice that m_gen.run() and m_driver.run() are forked-join meaning both the statements will execute parallelly, hence as soon as transactions are generated by the generator it will be available for use by the driver.
* finally $finish() example.



**Parameterized mailbox:**

* Notice that the in the last example the mailbox was type less meaning it can send any data type but if we want to restrict the datatype then we can use **parameterized mailbox**.
* This can be done by passing the datatype during the declaration
* `mailbox #(datatype) m1;`. 
* Consider example below where the mailbox is parameterized with axi_txn type.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\16.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\17.JPG)

* Observe below some functions and tasks which comes along with mailbox instantiation.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\18.JPG)

* If you are passing argument in new function of the mailbox say **mbox = new(100)** (<-- This needs to be confirmed) then only 100 transactions can be queued in the mailbox. After that if you try to put any transaction into the mailbox then the put transaction will be blocked until one transaction is removed from the internal queue.
* try_put and try_get are non-blocking functions/ tasks. meaning try_put will check if we can put some transactions in the mbox, if not it will return immediately it won't wait there (blocking) similarly try_get.
* peek will copy the item from the mailbox (won't remove) while get will move the item from the mailbox.
* try_peek --> non-blocking version of peek
* num --> returns number of messages in the mailbox.



## Events

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\19.JPG)

* Don't stress too much about what is an event.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\20.JPG)

* Event can be triggered using ->
* There are two actions with an event. event can be triggered and wait for the event
* wait for the event can be done using @ symbol.
* These can be used when the main task triggers an event at a logical point in the simulation time and another sub-task or fork task can wait for this event to happen or triggered.
* Apart from @ symbo task can also be waited for using triggered() symbol.
* @e1 and wait(e1.triggered) both are essentially doing the same task. but the later one is more recommended.
* wait_order can be used to confirm the triggering of events in a specific order.

# [4] Clocking Blocks

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\22.JPG)

* Clocking block is a mechanism to synchronize the sampling and driving of input and output signals with  respect to the clock event.
* Normally inputs are sampled at clock edge and outputs are driven at clock edge in a cycle based code (Verification and design). If skew is specified, then input is sampled skew time before clock edge and output is driven after the skew time.
* In the example on the right above the posedge clk is the synchronization event for this clocking block. Also notice that instead of defining individual skews for each signals, default skews for each input and output has been defined here.
* Notice the last two bullet points in the slide, this means that any clocking block input signal can only be used for reading and any output signal can only be used for driving.
* Any signals of the cb can be accessed using the syntax dry_cb.awready

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\23.JPG)

* Here skew is in terms of simulation and not the actual skew of hardware event. This is purely in terms of simulation.
* Input skew is time before the clocking event at which the signal is sampled and the output skew is time after the clocking event during which the signal is driven.
* Notice though that in very rare case we will specify the input and output skews as the time units because if we are changing the clock frequency than these numbers becomes meaningless, hence in most cases the input skews are specified as #1step and output as #0.
* #1step means sampled at the end of the previous time step, just before the corresponding clocking event.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\24.JPG)

* @(cb) is same as @(posedge clk) that is waiting for the clocking event.
* To make clocking block default for the every variable in the scope we can define it as default.

# [5] Interface

## What is an interface ?

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\25.JPG)

* Removes the necessity of writing each individual connection each time. Instead of this we can write the interface each time.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\26.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\27.JPG)

* Notice here that instead of passing each individual logic request, grant in the design we can directly create an instance of the interface `simple_interface intf`. 
* Now the individual elements can be accessed using dot operator intf.request.
* In the tb you need to define the instance of the interface which is local to the tb. this is tb_intf
* similarly design module is also instantiated. This is similar to instantiating a port signal but the signal ported has to be of the same type which in this case is interface.

## Modports and clocking blocks in interface

* SV allows type specification within an interface called as Modports. This is used to specify whether the port is input or output.
* Modports specifies the direction of the signal local to the interface.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\28.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\29.JPG)

* Notice how the modport is called in the design above. In this example the intf instance is exactly same as master modport that is this interface will have all the ports in the same direction as is defined in master modport.



* Now, can we use modports in the test bench ?. The answer is no. In the testbench one must use clocking blocks to get predictable simulation behavior.
* Now the question is how can we define an interface ( a common file) which can be used for both the design and test bench ?
* Now, the problem is in that design contains 2 modes master and slave but the tb contains 3 modes: master, salve and monitor.
* Hence you need to define a SV interface which can be used in master module, slave module and also in top level design module as shown in the figure below.
* And the same interface file will be used in tb also. 

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\30.JPG)



* In the tb there are 3 different modes. 
* In the first mode you will be testing AXI slave unit with a testbench which is working in the master mode.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\31.JPG)



* In the second mode you will be testing the AXI Master unit with the tb acting as a AXI slave

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\32.JPG)



* And finally you will be testing whole design with a tb sitting outside which needs to drive the top level design appropriately.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\33.JPG)

* Next slide shows the interface which can be used across design and tb as well.
* Notice that the modport is defined in the same way as discussed before when used for master it will be instantiated as intf.master and when  used for slave it will be instantiated as intf.slave.

* To use this interface in tb you need to define appropriate clocking blocks.
* In this case you need 3 different clocking blocks
  1. You need a clocking block where you want to drive signal in master mode. This cb is named as drv_mst_cb
  2. You need a cb where signals are driven in slave mode. This is named as drv_slv_cb
  3. One more cb is defined which is used to monitor this interface at the top level. When you are instantiating the whole design in the top level test bench. This interface is not driving master nor slave signals. This top level tb will just check different transactions. In this monitor cb all the signals will have input direction.
* **Please notice that if the interface will not be used in the design file then you don't need to define mode ports. Also if it is used within the tb then you need to define clocking blocks within the interface.**
* different cb's will define different directions of inputs and outputs. and also you need to define monitor cb which will snoop all the signals at the top level.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\34.JPG)





* After defining interface it can be used in both design and test bench.
* In this example design is considered as slave and master tb is testing it.
* In the example below also notice how the master clocking block is being waited for in the test bench using command @(tb_intf.drv_mst_cb)



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\36.JPG)



* **When you drive signals from this testbench you need to use appropriate clocking block.signal name in the interface**

# [6] Compiler Directives

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\37.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\38.JPG)

Optionally includes lines of source code during compilation. The ifdef directive checks that a macro has been defined, and if so, compiles the code that follows. If the macro has not been defined, the compiler compiles the code (if any) following the optional else directive. You can control what code is compiled by choosing whether to define the text macro, either with define or with +define+. The `endif directive marks the end of the conditional code.

Example  of ifdef from ASIC-WORLD

```verilog
// Code your design here
module ifdef ();

initial begin
`ifdef FIRST
    $display("First code is compiled");
`else
  `ifdef SECOND 
    $display("Second code is compiled");
  `else
    $display("Default code is compiled");
  `endif
`endif
  $finish;
end

endmodule
```

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\39.JPG)

# [7] Packages

* Same as packages in C++, used to share the common codes amongst different modules, interfaces, programs, etc.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\40.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\41.JPG)

* Notice in the example on the right that in the mod2 you cannot define bool_t b1 = TRUE because in that mod2 only axi_resp_t is imported and not everything like mod1
* Notice that entire uvm testbench is available in a package called uvm.pkg
* std package is implicitly available in the compilation scope. One does not need to import it.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\42.JPG)

# [8] Parameters and Constants

* Elaboration-time constants - These constants will be fixing there values during compilation. Parameters are Elaboration time constants.
* Run-time constants - These constants will fix there values when simulation runs. Constants are Run-time constants.
* Specparam - out of scope of this course
* defparam - don't use
* parameter and localparam are the same in SV. both can be used interchangably.
* If the type of the parameter is not mentioned then the default type is integer.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\43.JPG)

**Value Parameter**

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[2] Learning More TB Constructs\Images\44.JPG)



**Type Parameter**

* Here you define module, class, interface where you don't want to specify the type of the argument which is being passed.
* Type parameter allows you to have a parameter whose type can be changed anytime.
* Here `module fifo # (parameter list)` is the way by which any module, class, interface can be given parameters.
* In this example notice that MY_TYPE is a parameter of type `type`. And the default type of MY_TYPE is int.
* When we instantiate this module fifo we can change the type of this parameter MY_TYPE to anything required like logic[7:0], byte, int, real, etc. 