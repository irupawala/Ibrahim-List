## Part 1: SATA Overview

### Evolution of parallel ATA

* **SATA** stands for **Serial Advanced Technology Attachment or Serial ATA**.
* SATA is an **interface that connects various storage devices such as hard disks, optical drives, SSD’s, etc to the motherboard**.
* Serial ATA 1.0 (SATA) provides a high-speed (1.5Gb/s) serial connection between the HBA and Mass Storage devices.
* Why Serial Interface (SATA)? Lower Cost, Reduced pin count, higher speed, enhanced reliability due to cables/ connector, Low Voltage support.
* Historically HDD and HD Controller card were different. Compaq and WD introduced one integrated drive that combined the controller card and disk drive. This solution also included a simple bus interface to which the integrated drive cable was attached. This interface was known as IDE.
* Eventually group was formed to define a standard for Integrated device. These drives were known as ATA drives. Today ATA standard is directed by INCITS.
* **HBA Host Bus Adapter** acts as an interface between the system (host) bus and the drives.
* HBA Registers:
  * Device register: Software selects target device by writing either 0 or 1 into the device registers. 
  * Start sector Address register: Prior to reading or writing to disc, software must initialize sector address based on CHS registers (Cylinder, Head, Sector)
    * Physical disc address registers
    * Logical block address registers
  * Transfer Size register (Sector Count): To specify the size of the data transfer
  * Feature register: Software writes the desired feature value into the register during initialization to specify the feature that is to be set.
  * Command register: Software writes to the command register, which triggers execution of the selected command. Busy bit is set indicating that the drive is executing the command and has taken control of the registers.
  * Data register
  * Status register: Updated by drive to reflect the current status of the command being performed.
  * Error register: When errors occur during execution of a command, bits are set in the error reg to reflect the nature of error condition.
  * Control register
  * Alternate Status register

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\1.PNG)

* Device Signature: Each ATA drive provides a device signature via the register set. Upon completion of the diagnostics, driver load the ATA registers with the following information:
  * Device Signature - Indicating the device as either an ATA device or an ATAPI device
  * Diagnostic results - Indicating whether the drive passed the diagnostics.
* Commands
  * Commands without Data transfer
  * Commands with Data transfer
* Command Execution
* Overlap feature - Overlap provides a method for drives to relinquish ownership of the shared ATA interface. For example, a slower ATAPI CD ROM drive could release the bus while processing a command; thereby making it possible for software to issue a command to a faster ATA drive. Thus, two commands overlap allowing simultaneous command processing.
* Device Identify Command - Software can detect a drives capabilities by reading its configuration information via this command. 

### The Motivation for SATA

* Max PATA transfer rate - 133MB/s
* SATA transfer rates:
  * SATA I - 150MB/s
  * SATA II - 300MB/s
  * SATA III - 600MB/s
* PATA drives have jumper/ switches to configure device 0 or 1. SATA drives are implemented as point to point interconnects and don't need device selection.
* Hot Plugging supported.
* Number of server-related features were introduced with SATA II specifications: Port Multipliers, Port Selectors, Higher speed, Compatibility to PATA



### SATA Overview



![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\2.PNG)



![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\3.PNG)

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\4.PNG)



**SATA Protocol Layer Overview**

* Application Layer
  * Consists of the **programming interface to the SATA environment**. 
  * In legacy implementations this is represented by the register set (Shadow registers in the HBA). 
  * In the AHCI implementations the programming interface consists of **shadow registers, HBA-specific registers and memory data structures located in main DRAM.**
  * In SATA a copy of the legacy ATA registers, called "shadow registers" is kept in the host adapter. Host software initializes the shadow registers as required for the particular command to be issued. This action causes the SATA Application layer to forward the shadow register contents to Transport layer.
  * The actual command is issued when host software writes the command code to the command register. When software writes to the shadow command register, the HBA must set the BSY status bit within 400nS of command register write. When BSY is set software is not permitted to write other shadow registers.
  * The command register write triggers the delivery of the entire shadow register contents to the transport layer.
* Command Layer (**Command Sequence State Machine**)
  * Defines the sequence of FIS's to be exchanged between the host adapter and the drive during command execution. 
  * The type and sequence of FISs exchanged is a function of the command being performed. The command layer is responsible for managing the high-level protocol, by verifying the receipt of the expected FIS and by issuing any subsequent FIS to be returned in response.
  * Based on the command type and the type of packet received the command layer determines the next packet to send and initiates its delivery.
* Transport Layer (**Transport layer is responsible for creating a compliant FIS**)
  * **Decodes FIS received**
  * **Formats and requests transmission of FISs**
  * Manages flow control. Uses a flow control mechanism to ensure that transmit buffer/ receive buffer do not overflow or underflow.
  * Notifies Link layer of FIS pending delivery
  * Notifies link of flow control requirements during transmission.
  * **Detects FIS errors and retries some FIS transmission failures**
* Link Layer (**generating and decoding small packets called primitives**)
  * Generates and receives primitives used in the link protocol. A major part of this protocol is generating and decoding small packets called primitives
  * Responsible for preparing each FIS for transmission
  * FIS delivery notification 
  * CRC generation
  * Framing each FIS with start and end primitives
  * Detecting transmission errors 
  * Data Scrambling/ De-Scrambling
  * 8B to 10B Encoding/ Decoding
  * FIS Ready for Transfer
    * Upon receiving FIS transfer request, the Link layer creates a "Transfer Ready" (X_RDY) primitive and forwards it to the physical layer for transmission to the drive. The drive detects the X_RDY primitive and if it's ready to receive a FIS, it returns a "Receive Ready" (R_RDY) primitives to the HBA.
  * Flow Control During FIS Transmission
    * The transport layer transmission buffer is much smaller than the maximum payload size of a Data FIS, which is 8KB. Note that flow control can only occur during Data FIS transmission. During DMA Write commands, the contents of the Transport layer data buffer may be emptied faster than data can be delivered to the buffer. If buffer approaches dry condition, Transport layer requests the Link layer to send a HOLD primitive, thereby notifying the receiver that FIS transmission has temporarily been suspended.

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\9.PNG)

* Physical Layer (**Establishing link communication via OOB signaling and transmit/ receive FIS primitive traffic**)
  * When Link layer has delivered FIS to the physical layer for transmission, two operations are performed: 1. Parallel to Serial Conversion of the primitives and the FIS 2. Differential transmission of the serial stream at 1.5Gb/s or 3.0Gb/s.
  * Prepares data for transmission (e.g. serialization of data) or to recover it properly at the receiver (e.g. deserialization of data and clock recovery)
  * Transmits/ receives data - consists of high speed electrical interface that comprises the differential transmitter, receiver and transmission line.
  * Consists of the link transceiver used to send and receive all SATA link traffic
  * Link Initialization
  * Link Power management
  * Hot Plug Operations

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\5.PNG)

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\6.PNG)

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\7.PNG)

![](C:\Users\1000249643\Documents\Finance\Job Search\2021 Job Search\FaceBook, Hardware Systems Engineer - Storage\SATA\Images\8.PNG)

* **Major feature of SATA II:**
* SATA II introduces many features with majority focusing on better support for SATA server based solutions.
  * Native command Queuing (NQC)
    * NCQ increases drive performance by enqueuing up to 32 commands within the drive and processing these commands in an out of order (asynchronous) fashion to reduce overall access latency
  * Port Multipliers 
    * A given HBA may not support sufficient numbers of drivers for larger drive rack implementations. Port Multipliers connect to a single HBA port and provide support for up to 15 additional ports
  * Port Selectors
    * Port Selector is a mechanism that allows two different host ports to connect to the same device in order to create a reductant path to that device. Port selectors can be thought of as a simplex multiplier.
  * Enclosure Services
    * Large Cabinets (enclosure) that house large no of drives require special hardware and software to monitor and control environmental conditions such as temperature, fan speeds, drive activity, power, etc.  Existing standards have been developed in the SCSI environment to manage these enclosure services. The SATA II specs defines support for two standards: 1. SCSI Attached Fault-Tolerant Enclosure 2. SCSI Enclosure Services.
  * Enhanced hot plug support
    * SATA II adds additional support to the physical layer state machines to accommodate detection of drive insertion and removal.
  * Doubling the serial transmission rate to 3.0Gb/s
    * In the wake of port multipliers where a single HBA port interface has up to 15 drives connected, higher transfer rates becomes more critical, particularly when Native Command Queuing is also employed.



* **The AHCI Programming Interface**
  * In SATA I IO-mapped legacy registers are used as the means to send commands to the HBA via series of IO writes. 
  * In SATA II HBA's use software data structures in main memory (DRAM) where the legacy registers are virtualized. This another method of command delivery that does not include legacy registers is called the AHCI (Advanced Host Controller Interface).
  * The register contents are provided in the form of a Register FIS that is ready to be forwarded from memory to the SATA drives. The data structures in DRAM containing these Register FISes that are pending execution is provided via the command list. The command list includes up to 32 entries and each one provides the information needed to fetch a Register FIS.
  * The FIS's returned from the drive during command execution are forwarded directly to another data structure called the Received FIS structure.

