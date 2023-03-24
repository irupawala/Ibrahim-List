
2.6) Low level languages Vs High level language:

- Low level language - Binary, Assembly
- High level language - All programming languages like C++, Java, Python, etc

2.7) Compiler Vs Interpreter Vs Hybrid Languages:

C++ is a compiler based language while Javascript is an Interpreter based language.

Compiler:

- Compiler will check the codes for the error. If there is any error in the program compiled file will not be generated.
- Compiler  will convert the entire code in to machine code first that is executable file .exe
- After the translation executable file .exe can be run as many times as needed. Compiler is not needed now.

Interpreter:

- Interpreter will translate the source code into machine code line by line and also execute it.
- Note that here line by line translation will happen as well as excution will also take place.
- Note that here the translation (Compilation) will happen the number of times the program is executed hence we need Interpreter each time.
- Also If there is any error in the 10th line of the code then the first 9 liines will be executed, this is not the case in compiler
- Compiler based language runs independently while interpreter based languages required Interpreter each time.

Who is fast ?

Compiled programs are fast because it runs independetly. Interepreter based languages runs inside interpreter and conversion happens each time

Which is easy to write ?

Interpreter based languages are easy because it will run untill the error line is reached.

Hybrid Languages (Java, C#, all .net langauges)

- These have 2 steps. It has both compiler and interpreter.
- compiler here will generate byte code which is an error free code. Then JVM (for Java) will convert byte code to machine code and also excute it (hence Interpreter for byte code and not the source code)

2.8) What is an Operating System ?

Operating Systems is a master program which controls all the resources and provides services.


3.9) Programming Paradigms:

1. Monolithic Program - e.g BASIC

- No functions. All the instructions are in a single piece. Both data and instruction set are included in this single piece of code.

2. Procedural/ Modular Programs - e.g. C Language

- Functions introduced. Allows reusability of the code and hence also makes it possible to divide the task.
- It also introduced the concept of structures in which we can group the similar data together and then there are functions designed to work on that data

3. Object Oriented Programs - e.g. C++ Langauge

- OOP langauges introduced class in which the data and the functions related to that data are grouped together as a class
- Now we can create object of that class and call it as a function.


3.12) Steps for Program Development and Execution:

Steps for programming:

1. Editor - Used to write the program
2. Compiling - Check for errors
3. Linking Library
4. Loading
5. Execution - CPU executes the .exe file

3. Linking Library:

- All the programming languages contains built in codes (e.g Cin, Cout) which are included in libraries. These are included in the programs with the use of the heaser files e.g. <iostream>
- When the program is compiled the contents of library (header file) is copied in to exe file.

4. Loading:

- exe file is to be called in to main memory. This is called loading
- Now main memory is divided into 3 sections:
	* stock - Varaibles used in the executable file is created in the stack during the execution of the programs.
	* heap - Heap is used for dynamic memory allocation.
	* Code section - executable file .exe is loaded here and then CPU starts executing the program from the first line.
