# [2] Design and TB Hierarchy

* System Verilog is 'Verilog + supporting features for Verification'.
* SV supports object oriented programming.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\1.PNG)

# [3] Language Constructs

## Language Constructs

* Comments - //, /* ... */
* List of all keywords

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\2.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\3.JPG)

Built-in Functions (Tasks)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\4.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\5.JPG)

* Binary case equality operators and binary wildcard equality operators are used for x and c in SV.

## Number Constructs

Integer Numbers

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\6.JPG)

Real Numbers

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\7.JPG)

Time Constants

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\8.JPG)

## Datatypes

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\9.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\10.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\11.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\12.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\13.JPG)



# [4] Arrays in System Verilog

## Arrays in SV

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\15.JPG)

* Instead of arr[15:0] you can also declare array like C. arr[16].
* Convention is to represent packed array as [15:0] and unpacked array as [16]

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\16.JPG)

* The main difference between packed and unpacked arrays is in unpacked arrays the continuity of individual array declaration in the memory locations cannot be guaranteed

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\17.JPG)

## Dynamic Array, Associative Array and Queue

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\18.JPG)

* addr = new[200]addr - This will not delete the previous array declared just doubles it's size.
* addr = new[200] - This will delete the previous addr array and declare a new array of size 200.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\19.JPG)

* Associative arrays are like dictionaries in system verilog where all the elements can be represented as key-value pairs.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\20.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\21.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\22.JPG)

# [5] Procedural Assignment Blocks

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\23.JPG)

* initial - will be executed in the beginning of the simulation
* always - will be executed always in the simulation
* final - will be executed at the very end of the simulation

* functional code can also be written within task and function and you can call task and function anywhere within the initial, always or final block.
* Also with task and function we do not need to write begin and end blocks because those are built-in within task and function.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\24.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\25.JPG)



# [6] Flow Control and Looping statements

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\26.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\27.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\28.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\29.JPG)

## [7] Tasks and Function



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\30.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\31.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\32.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\33.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[1] Starting Learning TB Constructs\Images\34.JPG)

* Function - Used where some computation, conversion, comparison is needed.

* Task - used when you abstract the set of code into subroutine that consumes time. Example a driver code where some functionalities are kept in some subroutine and some another functionalities are kept in some another subroutine and those are consuming time then you have to define tasks for them and port them at higher level.

* **Functions are Synthesizable While tasks are not synthesizable as they are consuming time.**

