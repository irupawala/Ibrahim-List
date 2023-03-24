## [3] Introduction to UVM TB

### (3) UVM TB Architecture

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\1.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\2.JPG)



### (4) UVM TB Block Diagram

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\3.JPG)



## [4] Anatomy of UVM Classes and UVM Reporting

### (5) How to code a UVM component class in general

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\4.JPG)



* ``uvm_component_utils` is the Factory Registration Macro for all the classes extending from `uvm_component` class.
* This FR line will register your own class with the uvm factory.
* For more info visit https://www.chipverify.com/uvm/using-factory-to-override-items
* **Note that virtual interfaces are present only for driver and monitor classes.**
* Virtual interfaces is the handle to the actual interface module in SV which is used to drive the transactions to DUT.
* Notice that we have to override all the functions like build_phase and connect_phase such that they behave according to your requirements.
* build_phase is the place where you should create object of the sub classes. Note that here new() is not used to create the object but factory registration statements are used to create the instance.
* connect_phase is the place where you should make connections between uvm components.
* run_phase task is the place where intelligence of uvm structural components lies. For example in case of driver this is the place where you will drive the stimulus to DUT.

### (6) How to code a UVM data class in general

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\5.JPG)



* Note that my_transaction will always be extended from uvm_sequence_item and NOT uvm_transaction 
* task body() in uvm_sequence is the place where intelligence of the sequence is placed. Is is the place where transactions are created and managed and sent to DUT

### (7) UVM Reporting

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\6.JPG)



* Notice the 4 functions used for the uvm reporting.
* Note that the uvm_report, error, fatal does not have verbosity level which means that all the messages related to them will be printed.
* Default Actions is the criteria which differentiates the 4 reporting functions

## [5] Writing UVM components in your Test Bench

### (8) The Module: tes_bench()

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\7.JPG)

* Notice here we have to also create the instance of the interface which will be passed as a port to DUT. This instance of the interface is needed in the TB to pass the actual workload condenser or the class based environment to the actual DUT.
* Notice that by "Set all Configuration in UVM ENV" it means that adding all the components in UVM config DB.
*  UVM DB is a data base where you can put any components, modules, class handles, etc and use a name to reference particular component and get access to them anytime.
* Here interface handle axi_we_addr_intf1 handle can be accessed from the driver using the configDB.
* Also you should put all the DUT interface handle to configDB.
* run_test is used to initiate the test on DUT 
* **you need to call run_phase task of the test class to start the sequence on the sequencer**
* **Instead of instantiating the test object we can use run_test() UVM function which creates the object of top level test class running at current simulation. Also it will call the run method of the test class which requires the build_phase hence it will first call build_phase of the test which will ultimately call all other test components. In a nutshell when run_phase is called entire TB hierarchy is created.**

### (9) The Test Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\8.JPG)



* Note that there is no parent argument for the sequence because it is a data component.
* **phase.raise_objections is the main part of the run_phase. At time 0 if the uvm executes the run_phase and does not find objections then it will close the simulation In other words the UVM will run the simulation until it finds the objection raised. This is how UVM manages start and end of the simulation.**
* Notice that seq1.start passes the pointer to the sequencer as an argument. 
* **The seq1 will call the body method of the sequence which will inject txns to the DUT.** After the txns is completed the objection is dropped and hence simulation will be finished



###########################################################

* For the example of TB in the course note the following: 
* **Note that all the sequences should start parallelly hence all the seq1.start should come between the fork join statement. This will start the body method of all the sequences in parallel.**
* 

### (10) The Env Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\9.JPG)

* Notice that connect_phase is a place where you will connect the analysis port of the agent to the analysis port of the scoreboard.
* Analysis port only exist if there is a monitor.
* run_phase for env will be empty in most of the cases

###########################################################

* For the example of TB in the course note the following: 
* There is only one scoreboard shown in the figure but note that there are actually 4 scoreboards.  2 set of scoreboard for read and write for each agent.
* 



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\10.JPG)

### (11) The Agent Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\11.JPG)



* Typically you will be defining agent per interface in DUT. If you have USB interface or AXI interface then you will be defining two different agents to deal with different interface component.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\12.JPG)



* Note here that analysis port is declared explicitly which will be connected to the scoreboard but then the question is **how does the txns reaches sequencer without ports ?.**
* Ans is there is no direct port connection from sequence to the sequencer. Instead the sequence which is sending the txns will get the handle of a particular sequencer and the sequence will always be initiated in particular sequencer handle. Thus there is no explicit connection from sequence ti the sequencer but once the txns has reached the sequencer it should go to the driver and other parts using explicit connection.
* Notice that axi_wr_port is an aport present in the agent. you have to make a connection from aport of the monitor to the aport of the agent in the connect phase.
* run_phase will be empty in uvm_agent

### (12) The Scoreboard Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\13.JPG)



* The scoreboard will receive input transactions and output transactions through a monitor.
* Transactions received as input will be passed to reference model and this model will mimic the behavior of DUT in some other programming language or even in SV and will convert the input transactions to expected output transactions thus calculated expected transactions will be compared against actual output transactions that is monitored at the output interface. Hence its functionality is to check the correctness of the DUT.
* analysis_export is required to get the transactions coming from different monitors or through different analysis ports in the agent class. 
* **axi_wr_export of the scoreboard is connected to the axi_wr_aport of the agent in the environment.**
* Advantage of using analysis fifo is that it already gives you an implementation of the analysis export, So every analysis export should be connected to final implementation then only you will be able to send transaction and receive transaction in the UVM verification environment.
* tlm analysis fifo already has built in implementation of analysis export which is called analysis_export hence we can call fifo_name.analysis_export (AXI_RD_F1.analysis_export) to connect the analysis export in the component such that this (fifo/analysis_export ?) will act as an endpoint to the connection diagram.
* In a nutshell you need final implementation of analysis_export and if you are using a tlm fifo then it will provide the built in analysis export and will put all the txns in the built in fifo.
* You get the txns from the tlm_analysis_fifo using get function
* In the run_phase you will write actual comparison of output to input
* 



###########################################################

* For the example of TB in the course note the following: 
* Scoreboard is parameterized with both OCP (Resp) and AXI (Req) txns.
* analysis port will be available for both
* In the run_phase you will wait for both resp and req txns to come and then will do comparison

### (13) The Sequencer Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\14.JPG)

* You should parameterize your own sequencer with the type of txns that you need to pass from sequence to the sequencer #(axi_transaction)

### (14) The Driver Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\15.JPG)

* Driver converts txns coming from the sequencer to actual pin level DUT signals
* Here in the build_phase we have to get the handle which was kept in the config DB by top level TB.
* Sometimes you might want to send response txn for the every txns received. if that is the case you should create the object of the resp_txn and you should set the information regarding txn id to which you are sending the response.
* set_id_info will copy the txn id of the particular txns to resp_txn.
* After that you can fill the fields in the response txns as needed and you can send the resp by saying put_response(resp_txn). If that is the case your sequence will wait for the response before sending the next txn.
* If there is no need to send the response back to the sequence from the driver then this part is not needed.

### (15) The Monitor Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\16.JPG)

* Passive entity that samples DUT signals
* Collects transactions. Keeps monitoring interface signals and whenever particular information regarding txn is arrived from the pin level DUT it will convert it to new txn with relavent field and send this txn to the upper level component like scoreboard. monitor_wr_addr() and monitor_wr_data() are the two functions for this.
* **Both the driver and monitor should get the handles to the virtual interface through UVM config DB.**
* In the run_phase task the functionality to monitor pin level signal is written
* Whenever any txn from any task is received then you will create new txn with all the reqd fields and will put the txn in to appropriate analysis write port.
* Also note that implementation of the monitoring task in run_phase which will convert the pin level signals to txn is specific to your DUT specification



### (16) A Transaction Class



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\17.JPG)

* Here Data members specific to DUT interface specifications are added. Data members can be made random if you want random transactions in the sequence.
* constraints to data members are also added.
* do_copy is a function which is called whenever you call the copy function with the object of this class.
* convert2string is also uvm specific and cannot be changed

### (17) The Sequence Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\18.JPG)



* Here you will generate the txns that you will be sending to sequencer and driver,
* body is the class where you generate txns and send them to the sequencer.
* You will always be calling sequence.start() on a sequencer. Typically this is done in a test. Whenever you call sequence.start with a sequence handle then body function of that particular sequence will be called. This body function will create txns and send them to the sequence.
* Note that sequencer must receive response from driver to send stream of txns if response mechanism has been created in driver.

## [6] Data Flow between UVM Classes

### (18) Transaction Level Modelling (TLM)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\19.JPG)

* ```verilog
  // port.connect(export)
  
  // connect inbuilt port of the driver to the inbuilt port of the sequencer
  m_driver.seq_item_port.connect(m_sequencer.seq_item_export);
  ```

* ```verilog
  // child_port.connect(parent_port)
  
  // connect the analysis port of the monitor to the analysis port in agent
  m_monitor.axi_wr_aport.connect(axi_wr_aport);  
  ```

* ```verilog
  // aport.connect(export)
  
  // connect the scoreboard ports to agent aports
  m_agent.axi_wr_aport.connect(m_scoreboard.axi_wr_export); 
  ```

* ```verilog
  //parent_export.connect(child_export)
  
  axi_wr_export.connect(AXI_WR_F1.analysis_export); // analysis export connected to FIFO export
  ```

* Communication between any two classes are made between port and export or an analysis port and analysis export.

* Note that type of connections possible in TLM (port/ export, child_port/ parent_port, parent_export/ child_export) are the types of port where the request transactions are flowing and for the response transactions TLM is defining another port which is called analysis port.

### (19) Data Flow from Sequence to Driver through Sequencer

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\20.JPG)



* Notice that there is no direct port connection between sequence and sequencer. 
* sequence will always start on a particular sequencer eg: seq1.start(sequencer handle).
* **To pass the txns from seq to driver there should be export in seq and port in driver. These port and export are internally defined in UVM hence we have to just connect them in agent.**

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\21.JPG)

### (20) Data Flow from Monitor to Scoreboard 

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\22.JPG)



* **Notice that for txns from DUT to scoreboard there needs to be analysis port in the monitor, analysis port in the agent and an analysis export in the Scoreboard.**
* **The difference between sequence_export and Driver_port and Monitor_port and Scoreboard_export is that there is no default implementation of ports in Monitor/Scoreboard like in Driver/Sequencer.**
* **You have to manually add analysis port to your monitor class and analysis export to your scoreboard class.**



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\23.JPG)



* **Notice that whenever the valid txns is seen in the monitor interface, monitor will write the txns to the analysis port using the command axi_wr_aport.write(txn) in the run_phase function.**
* Note the 3 methods in the slide above to connect analysis_port of monitor to analysis_implementation. We are going to adopt method 3 here to increase the modularity of the design. This connection is made in agent.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\24.JPG)



* **For every analysis port/ export connection there should be a final termination point called implementation of analysis component**. So we need to supply implementation of analysis port/export which is the termination point.
* For this there are two options: 
  * Either write your own implementation for analysis export
  * Instantiate  a built-in UVM analysis fifo which is providing an implementation for analysis export 
* If you are instantiating an object of uvm_tlm_analysis_fifo then there is a built-in implementation of the analysis export with the name **analysis_export**.
* Hence you just need to connect your own defined analysis_wr_export to the **analysis_export implementation** in the scoreboard





![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\25.JPG)

## [7] Working Example. Developing a UVM based Test Bench

### (21) DUT Specifications

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\26.JPG)



* TB for Interconnect DUT - DUT is connecting two AXI masters with one OCP slave

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\27.JPG)



* No response for read because read itself is a response. You can embed the response data with read

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\28.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\29.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\30.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\31.JPG)

### (22) AXI and OCP Transactions

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\32.JPG)



* AXI Master 1 will send all the txns with ID 0 to 7 while AXI Master 2 will send the txns from ID 8 to 15. Note that width of the ID field is [3:0].
* Using these ID's sent by AXI you can identify the responses coming from OCP slave and route them appropriately between two AXI Master 1 and 2



## [8] UVM Factory 

### (31) Factory Overriding

* For a working TB if you want to use the same tb with a txn which is derived from the txn for which tb was defined initially then Factory Overriding is used to use the same tb without making any change in the original TB.
* In a nutshell you can specify the type of object being created at the runtime. The only thing is you need to register your object creation using factory.
* This is only possible if static allocation function is used instrad of new function as shown below and creation of this obj using the uvm factory is possible if and only if you have registered the original class using the FR macro's.
* Two types of overrides are possible either to override by type or override the instance that has been created.
* If we are using type overiding then all the instance of the class will be overridden but if you are using instance overriding then only that instance of the class will be overridden to the new type

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\33.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\34.JPG)

* Note in the figure above that my_driver_h instance of my_driver should be created using **static allocation function and not new function**
* Now if set_inst_override_by_type is used before creating instance of my_driver in the hierarchy then the type of this my_driver_h will be modified_driver



## [9] Virtual Sequence and Best Practice for UVM TB

### (32) Virtual Sequence

Virtual Sequencer is a deprecated concept hence don't use

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\35.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\36.JPG)



* Notice in the figure above how different sequences (sequencers in the agent) are initiated one by one in test. There is a better way where we can handle all the sequence interdependencies within another sequence. That sequence is called virtual sequence.

### (33) Virtual Sequence Example

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\37.JPG)

* Notice that there is no class called uvm_virtual_sequence hence you have to typedef to cast uvm_sequence to uvm_virtual_sequence.



* Note that virtual_sequence requires the handle of all the sequencers. 
* The only difference by using virtual sequence is that in the virtual sequence you need to declare the handles of all the sequencers in the environment and you will start the child individual sequences respectively in the corresponding sequencers.
* Also note that in the test before starting the virtual sequence you have to fill in the handles that we have already defined in the virtual sequence

### (34) Developing VIPs

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\38.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\39.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[7] UVM in SV Learn the architecture and code your VIP\Images\40.JPG)