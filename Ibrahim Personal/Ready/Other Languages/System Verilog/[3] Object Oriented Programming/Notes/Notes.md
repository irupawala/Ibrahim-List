# [2] Array, Structure and Union

## Arrays & Structures

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\1.JPG)

* student_data s2[100] --> notice that array of structure can also be defined.



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\2.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\3.JPG)

* Notice the above actual example for SV tb, here bus_1 represents the group of some signals

## Union

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\4.JPG)

* Union is used when you want a single memory location to hold different type of data during different point of program execution, in that case you can define a union with all the data members needed.
* Consider the example below where a single memory location is used to store either int, float, bit, string.
* The type of memory location will change at the run time. Notice here that memory for only one data member will be allocated. The memory allocation will be done for the largest memory datatype.
* In the example above the memory allocation for the union will be of size of string s[10]

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\5.JPG)

# [3] Introduction to Class

## Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\6.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\7.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\8.JPG)

* Function new should be present by default in all the classes.



## Object

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\9.JPG)

* Notice that creating an object here means allocating space for it in the memory.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\10.JPG)

## New and This

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\11.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\12.JPG)

# [4] Shallow copy and deep copy

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\13.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\14.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\15.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\16.JPG)

* Notice that in case of shallow copy all the members of one class is copied to another class except objects.
* Objects will not get copied but the address of the object will get copied hence when we refer to the members of the object of the new copy class p2 than it will also refer to the same members of the object p1.
* **Notice the big mistake here before the child class object can be used in the parent class it has to be created/ allocated using ch_obj = new;**



![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\17.JPG)

* When you do deep copy as shown above even the objects in p2 are copied in p1.
* P2.copy(p1) --> Notice that there is a typo in the image above. ; should not be there.

# [5] Inheritance

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\18.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\19.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\20.JPG)



* Notice that if the parent class has a constructor function then the derived class also needs to have the constructor function and the constructor new function in the derived class needs to have first line as super.new().

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\21.JPG)

# [6] Overriding 

## Overriding V/s Overloading

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\22.JPG)

## Overriding Data Members

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\23.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\24.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\25.JPG)

* Notice that this means that overriding is not actually working in System Verilog.

## Overriding Member Functions/ Tasks

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\26.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\27.JPG)

* NOTICE THAT THE CONCEPT OF VIRTUAL FUNCTION IS NOT THE SAME AS THAT OF C++. IN C++ THE DERIVED CLASS HAS TO OVERRIDE THE FUNCTION IN THE BASE CLASS IF DECLARED VIRTUAL. 
* IN VERILOG TO CALL THE METHOD VIA A PARENT CLASS, METHOD NEEDS RO BE DECLARED AS VIRTUAL

## 'Super' Keyword

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\28.JPG)

* Note that in the previous slides we have used new function in the derived class. Whenever the new function in the derived class is called then the new function of the base class is called as well even if we are not using the super keyword.


# [7] Data Hiding

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\29.JPG)

# [8] Abstract Class

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\30.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\31.JPG)

# [9] Parameterized Classes

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\32.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\33.JPG)

* Notice that this feature is very important in System Verilog. Passing user-defined class as type of the parameter is very important feature.

# [10] A Typical SV testbench structure

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\34.JPG)

# [11] Class Based SV TB Structure

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\35.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\36.JPG)

* Everything that we do in SV is transaction based and always consider your TB As stimulus generator where stimuls is a transaction itself.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\37.JPG)





* There will be one more round of class based wrapper around all the testbench component which is called TB environment.

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\38.JPG)

* All the TB components are instantiated in Env and are connected together in Env class.
* Notice that the user gets environment with all the internal details hidden (abstraction). hence the tb gives all the components required by the user to drive the DUT.
* Notice that this class based TB structure is not always the case but will be in use most of the time depending on the requirements.



# [12] Coding A class based TestBench

## Command Specification

* In this example we are focusing on stimulus generation part of the TB. We will not be dealing with DUT commands or Monitor/ Checker part of the TB.

* We will only be dealing with driver part and simulation generation and how these commands can be modelled as transactions on a class based TB and how these transactions can be applied to actual DUT.

* DUT will decode the header byte to identify the command and it will take appropriate action. 

* There are two types of commands as shown in the image. The DUT will identify the type of command using the Header[7:6].

  

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\39.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\40.JPG)

![](C:\Users\1000249643\Desktop\Programming Langauages\System Verilog\[3] Object Oriented Programming\Images\41.JPG)

## Coding Example - Base Class

* Now let us understand how this commands can be modelled as transactions in SV and how a SV based TB can be written to generate n number of transactions.  