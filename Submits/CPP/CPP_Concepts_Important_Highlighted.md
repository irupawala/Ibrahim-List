# Skeleton of a Program

## Hello World

```c++
#include <iostream> // library header file

using namespace std; // some built-in function in the header file are grouped under name std. for using that we have to say using namespace std                        

int main() // int is return type hence we have to write return 0 in the end
{

//std::cout << "Hello world!"; // :: is known as scope resolution operator. If we are going to use cout frequently it is better to use nampespace
                                 
	cout << "Hello world!" ; // cout and cin stands for console operation. << is called insertion operator

    return 0;
}

```

## Add two numbers - Explain taking in two numbers

```C++
#include <iostream>

using namespace std;

int main()
{
    int a, b, c;

    cout << "Enter the two numbers" << endl;
    cin >> a >> b;
    c = a+b;
    cout << "The addition of 2 nums is " << c << endl;



    return 0;
}
```

## Getline - Input a string

```C++
#include <iostream>

using namespace std;

int main()
{
    string name;

    cout << "Please enter your name ";
    //cin >> name; // This will display only one word and not the contents after the space
    getline(cin, name);
    cout << "Welcome to C++ " << name;

    return 0;
}
```

# Primitive Data Types

C++ supports several built-in data types, including:

1. Integer Types:
   - char (1 byte)
   - short (2 bytes)
   - int (4 bytes)
   - long (4 bytes)
   - long long (8 bytes)
2. Floating-Point Types:
   - float (4 bytes)
   - double (8 bytes)
   - long double (10 bytes or more)
3. Boolean Type:
   - bool (1 byte)
4. Void Type:
   - void (no storage)

## Int Data Types

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[1] Int.PNG)

## Char Data Types

In C++, `char` is a built-in data type that represents a single character. It can be used to store alphanumeric characters, symbols, and special characters.

The `char` data type is defined using the `char` keyword. It has a size of 1 byte (8 bits) and can represent 256 different values, including all uppercase and lowercase letters, digits, punctuation marks, and control characters.

Here are some examples of using the `char` data type in C++:

```c++
char c1 = 'A'; // Initializing a char variable with a character literal
char c2 = 66; // Initializing a char variable with an integer value
char c3 = '\n'; // Initializing a char variable with an escape sequence

cout << "c1 = " << c1 << endl; // Output: c1 = A
cout << "c2 = " << c2 << endl; // Output: c2 = B
cout << "c3 = " << c3 << endl; // Output: c3 = (newline)
```

In addition to representing single characters, `char` arrays can be used to store strings of characters in C++. To represent strings, `char` arrays are typically null-terminated, meaning that a null character (`\0`) is added to the end of the array to indicate the end of the string.

```c++
char str1[] = "Hello"; // Initializing a char array with a string literal
char str2[6] = {'H', 'e', 'l', 'l', 'o', '\0'}; // Initializing a char array with individual characters

cout << "str1 = " << str1 << endl; // Output: str1 = Hello
cout << "str2 = " << str2 << endl; // Output: str2 = Hello
```

* **Notice that char datatype can take character, integer, special characters and symbols as an input but will store ASCII value (integer) of them.**
* **While outputting the value char will return the char/ symbol corresponding to that ASCII value.**

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[2] Char.PNG)

## Strings

To define and print a string in C++, you can use the `string` data type and the `cout` statement. Here's an example:

```c++
#include <iostream>
#include <string>

using namespace std;

int main() {
   string str = "Hello, World!"; // Defining a string variable
   cout << str << endl; // Printing the string to the console
   return 0;
}
```

Note that the `string` data type is part of the C++ Standard Library and provides many useful functions for working with strings. You can concatenate, compare, and manipulate strings using various string functions. For example:

```c++
string str1 = "Hello, ";
string str2 = "World!";
string str3 = str1 + str2; // Concatenating two strings
cout << str3 << endl; // Printing the concatenated string
```

* **In C++ characters are represented in Single Quotes ' ' while strings are represented in double quotes " "**

## Modifiers

In C++, modifiers are used to modify the behavior of the basic data types by changing their storage requirements, range of values, and other characteristics. Here are some commonly used modifiers in C++:

1. const: This modifier is used to make a variable constant, meaning its value cannot be modified once it is initialized. The `const` keyword is placed before the data type in the variable declaration. For example: `const int num = 10;`
2. volatile: This modifier is used to indicate that a variable's value may change unexpectedly due to external factors. The `volatile` keyword is placed before the data type in the variable declaration. For example: `volatile int sensorValue;`
3. signed/unsigned: These modifiers are used to specify whether a variable can hold negative values or not. By default, integer types in C++ are signed. To specify an unsigned integer, use the `unsigned` keyword before the data type. For example: `unsigned int num;`
4. short/long: These modifiers are used to specify the range of values that a variable can hold. `short` indicates that a variable can hold smaller values than the standard data type, while `long` indicates that it can hold larger values. For example: `short int num1; long int num2;`
5. static: This modifier is used to create a variable that retains its value even when its scope is exited. The `static` keyword is placed before the data type in the variable declaration. For example: `static int count = 0;`
6. mutable: This modifier is used to allow a data member of a const object to be modified. The `mutable` keyword is placed before the data type of the data member. 

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[3] Modifiers.PNG)

## Variables

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[4]Variables.PNG)

# Operators and Assignments

## Operators and Expressions

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[1] Operators.PNG)

## Type Casting

**Notice in this figure that Modulo Operator % is allowed on int and char but not float **



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[2] Type Casting, Mod is allowed on int and char but not float.PNG)



## Operators Precedence

**Notice the header file #include<cmath> or <math.h> to be included for using the functions like sqrt() and pow() **

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[3] Operator Precedences, function for sqrt, pow, include cmath.PNG)



## Compound Assignment

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[4] Compund Assignment.PNG)



## Pre-Post Increment Operator

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[5] Pre-Post Increment Operator.PNG)

## Multiple Increment Operator not allowed in a single line

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[6] Multiple Increment Operator is not allowed in a single line.PNG)

## Overflow and Underflow condition

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[7] Overflow.PNG)

## Program to demonstrate Overflow

```c++
// Program to Demonstrate Overflow
#include <iostream>
using namespace std;
int main()
{
	char a=128;
	cout<<(int)a<<endl;
    
	char b=127;
	b++;
	cout<<(int)b<<endl;
    
	char c=-129;
    cout<<(int)c<<endl;

    char d=-128;
    d--;
	cout<<(int)d<<endl;
    
	int e=INT_MAX;
	cout<<e<<endl;  
	e++;
	cout<<e<<endl;
    
return 0;
}
```

## Bitwise Operator

**Notice the NOT of 5 is -6**



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[9] Bitwise Operator, NOT of 5 is -6.PNG)

## Left shift by one position is multiply by 2 and right shift by one position is divide by 2

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[10] Bitwise Operator, left shift multiply.PNG)

# Conditional Statements

## If-else

```c++
if(a>b && a>c)
    {
    cout<<a<<endl;
    }
else if(b>c)
    {
    cout<<b<<endl;
    }
else
    {
    cout<<c<<endl;
    }
```

## Switch Statement

- switch is a branch and control statement.

- switch is faster then if-else because unlike if-else it doesn't check all the conditions

- `switch(exp)` --> note that this code **exp can be char or int**

- **note that in the statement `case 1:` there is a space between case and 1. It will generate wrong results if you don't give this space**

  ```C++
  switch(exp)
  {
  case 1:
  ---
  break;
  
  case 2:
  ---
  break;
  
  default:
  ---
  }
  ```

- default is optional. it won't throw an error if you don't include default. 

- If you give any value in the expression for which there is no case then the default will be executed.

- default can also be written anywhere in the program but if not in end then the break statement has to be included with it.

- Every case block must terminate with break. 

- **If you don't mention break after any case then it will execute that case and the case after that until the break statement is reached. This is called fall through in programming.**

- **If int type then cases can be 0,1,2.... If the char type then we have char labels like 'a', 'b', 'c'..... but cases names cannot be STRINGS.**

# Loops

- There are 4 loops statements in C++

1. pre-tested loop while()
2. post-tested loop do..while()
3. counter controlled loop for()
4. for each loop for Collections for()

## While statement

- Condition is checked first and then process is done.

```c++
while(int i <= n)
{
	process...
}
```

## Do-While statement

- Process is done once then condition is checked if it is true then execution is done again

  ```c++
  do
  {
  	process...
  }while(int i <= n);
  
  ```



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[8] Loops\[2] While_Do_While.PNG)



## For loops

```c++
for (i=0; i<=n; i++)
{
}
```

- Note that initialization, condition and increments are optional but if we don't include condition in for loop we have to manually add the condition
  in the for block to break it off.

```c++
	{ // This is completely valid piece of code.
	int i=0;
	for (;i<=n;)
		{
		cout << i << "Hello\n";
		i++;
		}
	}
```

- We can also skip the condition but then we have to add condition manually

```c++
{ // This is completely valid piece of code.
int i=0;
for (;;)
	{
	cout << i << "Hello\n";
	i++;
	if (i>10)
		break;

	}
```

## Nested For Loop

```c++
for (int i=0; i<3; i++)
	{
		for (int j=0; j<3; j++)
			{
				cout << i << j << endl;
			}
	}
```

## For-each statement

- Introduced from C++ 11.
- For each loops are used with the collections of the elements like arrays, vectors, etc.
- **For each loop will NOT work on Pointers.**
- Benefit of for each over for is that here we don't have to know the total no of elements in the array

```c++
int A[] = {8, 6, 3, 9, 7, 4}

 for (int x : A) // read it as for each x in A
	{
		cout << x << endl; // note that in for statement i was index but here x is element itself
		}
```

Another example: (what if we do ++x in place of x ?)

```c++
for (int x: A)
	{
	cout << ++x << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}
```

Another example: (What if we want to change the value in array itself ?)

```c++
for (int &x: A) // note that this &x is called the reference. meaning it gives the name to the same value
				// This way the elements in original array will change
		{
	cout << ++x << endl; 
		}	
```

## Auto Data Type

- One more benefit for using for each loop is AUTO datatype
- If we don't know the datatype of the elements in array we can write AUTO datatype in for each		

```c++
for (auto x: A) // This will automatically make the datatype of x as the datatype available in the array.
	{
		cout << x << endl;
		}
```

**Program Demonstrating for - each statement use**

```c++
#include <iostream>

using namespace std;

int main()

{

    int A[] = {8, 6, 3, 9, 7, 4};

    cout << "Displaying the incremented values and also storing it." << endl;


    for (int &x: A)
        {
        cout << ++x << " "; // here 9, 7, 4... will be printed and also stored in original array 
		}
		cout << endl;


    cout << "Displaying the original values but storing incremented." << endl;

    for (int &x: A)
        {
        cout << x++ << " "; // here 9, 7, 4... will be printed but note that original values in the array will remain be incremeted
		}
		cout << endl;

    // Displaying A

     cout << "Displaying A" << endl;

    for (int x: A)
        {
        cout << x << " "; // printing incremented values
		}
		cout << endl;


    return 0;
}
```

# Array

## Single Dimensional Array

Array is a collection of similar data elements under one name, each element is accessible using its index

• Memory for array is allocated contagiously
• For-each loop is used for accessing array
• N-dimension arrays are supported by C++
• Two-Dimensional Arrays are used for Matrices
• Array can be created in Stack or Heap Section of memory

- int A[5] = {1, 2, 3}
- float B[3] = {1.2, 3.4, 5.6}
- Char C[] = {'A', 'B', 'C'}

```c++
#include <iostream>

using namespace std;

int main()
	{
		float A[] = {2.3f, 4.5f, 9, 8, 7};
		
		for (int x:A)
			cout << x << endl;
			
		return 0;
		
	}
```

```c++
#include <iostream>

using namespace std;

int main()
	{
		char A[] = {'A', 66, 'C', 68};
		
		for (auto x:A)
		// for (int x:A)
			cout << x << endl;
    	
    	// here char C can be accessed using following commands
    	cout << A[3] << endl;
		cout << 3[A] << endl;
    	cout << *(A + 3) << endl;
    	cout << *(3 + A) << endl;
    
		return 0;
		
	}
```

- Always notice that here the name of the array name A, B, C never stores the value itself but the address of the array
- In C the operator a[b] = b[a] = *(a+b) hence individual elements of array can be accessed as a[b], b[a], *(a+b)
- Visit the link https://stackoverflow.com/questions/381542/with-arrays-why-is-it-the-case-that-a5-5a/381549#381549



## Multi Dimensional Array

```c++
int A[2][3]={{2,3,4}, {5,6,7}};
int B[2][3]= {2,3,4,5,6,7};

```

## For-each for Multi Dimensional Array

```c++
#include <iostream>

using namespace std;

int main()
{
   // int A[2][3] = {2,3,4,6,3,5};
   int ROWS, COLS;

   cout << "Enter the number of row ";
   cin >> ROWS;
   cout << "Enter the number of columns";
   cin >> COLS;

   int A[ROWS][COLS] = {};

    //* For (int &x:A) // Notice that we cannot use x of type int here because x must be of type "ROW"
    //* Also notice that x is "ROW" hence we have to take it as type reference using "&" or else it will throw compilation error
    //* using reference here x is of type "ROW" of A and y is of type "COLUMN" of x
    //* Note that reference symbol here is a syntax. It won't create a new variable but use the same variable.    
    
    cout << "Input the array" << endl;
    for (auto &x:A)
    {
        for(auto &y:x )
        {
           cin >> y;
        }

        cout << endl;
    }

    // printing each element of for-each loop

    for (auto &x:A)
    {
        for(auto &y:x )
        {
           cout << y << " ";
        }

        cout << endl;
    }

    return 0;
}
```

# Pointers

## Introduction

- In C++, a pointer is a variable that stores the memory address of another variable. **Pointers allow us to indirectly access and manipulate the values of other variables by pointing to their memory addresses.**
- Based on this variables are classified into two types:
  1. Data Variables
  2. Address Variables
- Data variable - int x = 10, meaning x is stored in location say 200/ 201
- Address variable - int *P; P = &x. This means P is stored in location say 300/301 and
  it contains the address of x which is 200/ 201.
- **int *P = &x. This also means that P contains the address of a variable whose data type is int**
- Definitions:
  - Declaration - int *p;
  - Initialization p = &x;
  - Dereferencing cout << *p

```c++
#include <iostream>

using namespace std;

int main()
{
    int a=10; // declare an integer variable
    int *p; // declare a pointer variable of type int*
	p = &a; // assign the address of x to the pointer variable p
    
    int A[]={1,2,3,4,5};
    int *q = A; // here we have not written &A because when we write A, &A[0] is automatically assigned to q
    // int *q = &A[3] // this is also allowed as we are storing address of integer at A[3]

    cout << a << endl;  // Displays 10
    cout << &a << endl; // Displays address of a
    cout << p << endl; // Displays address of a
    cout << &p << endl; // Displays address of p
    cout << *p << endl; // Displays data of the address where p is pointing. This is called "Dereferencing".

    q = q+1;
    cout <<"Elements of A: " << *q << endl;

    q = q+3;
    cout <<"Elements of A: " << *q << endl;

    cout <<"Elements of A: " << q[-4] << endl; //  q[-4] is equivalent to *(q-4)

    return 0;
}
```

## Pointer Arithmetic

We can also use pointer arithmetic to access other values in memory. For example, to access the next integer value after "x", we can increment the pointer variable:

```c++
int A[5] = {1,2,3,4,5}

int *p = A; // here lets say 1 is stored in mem location 200,201 then p stores 200
cout << *p << endl;
p++;      // increment the pointer variable to point to the next integer value in memory
cout << *p << endl; // prints the value of the next integer in memory
```

There are five operations allowed on pointers.

1. p++;

- This means that p will now contain address 202 and not 201
- **The value of the pointer incremented depends on the datatype of the pointer**
- If the datatype is float then the pointer will be incremented by +4
- If it is char the pointer will be incremented by +1.

2. p--;

3. p = p + 2;

- if pointer is pointing at 202 then now it will point at 206.

4. p = p - 2;

5. d = q - p; 

- Distance between two pointers or the number of elements between 2 pointers

```c++
int A[5] = {1,2,3,4,5}

int *p = A;
int *q = &A[3]
```

- Hence q-p here will give 206-200 = 6 and 6/2 (as datatype is int) = 3. Meaning there are 3 elements between pointers p and q

6. d = p-q;

- here the answer will be 200-206 = -6 
- hence this tells us which pointer is far away 
- In this example it means that q is far away as the difference is negative and v.v. for positive difference.

**Pointer Arithmetic Example **

```c++
#include <iostream>

using namespace std;

int main()
{
    int A[5]= {1,2,3,4,5};
    int *p=A;

    cout << *p << endl;
    p++;
    cout << *p << endl;
    p--;
    cout << *p << endl;


    // observing the addresses

    cout << p << endl;
    p = p+2;
    cout << p[-2] << endl; // This is because c standard defines [] operator as a[b] = *(a+b)
    return 0;
}
```

## Why Pointers

1. 

- Main programs can directly access code section and stack ONLY but NOT HEAP.
- Directly means it can take address directly go there and take the data.
- But it can access heap memory indirectly. The pointer in stack can have the address
  of the data in heap thus allowing the program to access the data in heap.

2. The files in the Disk are accessed using only FILE pointers
3. Network connections are accessed by the program using pointers
4. Keyboard/ Monitors/ Printers are accessed indirectly accessed using pointers.

**Pointers - Important Facts**

- **LANGUAGES LIKE JAVA AND C# DOES NOT HAVE POINTERS HENCE WE CANNOT ACCESS THESE DEVICES THROUGH THE PROGRAM AT ALL.YOU CAN ACCESS THESE ONLY USING JVM OR COMMON LANGUAGE RUNTIME IN C# OR .NET**
- **Hence System level programming cannot be done using Java or C#. Operating systems and device drivers are thus programmed using C++.**
- **POINTERS OF ANY TYPE TAKES THE SAME SIZE.**
  - int *p;
  - double *q;
  - then sizeof(p) will be equal to sizeof(q)

## Dynamic Heap Memory Access using pointers 

- It's important to note that pointers can also be used to allocate memory dynamically on the heap, which can be useful in cases where we don't know how much memory we need at compile time. We can use the "new" operator to dynamically allocate memory, and the "delete" operator to release the memory when we're done using it.
- Heap memory is accessed dynamically. Meaning memory is allocated dynamically.
- **The size of the memory required in the heap is decided at run time not at compile time.**
- Mostly we allocate the arrays in the heap and not just float or int.

**Array created in stack:**

```c++
int A[5] = {1,2,3,4,5}
```

**Array created in heap:**

```c++
int *p; // This creates p in stack which stores the address of array in heap.
p = new int[5];// This new means memory is allocated in heap. whenever you create an array in heap then you need to take its address and assign it to a pointer.
```

- Note that the variable p is stored in stack.
- **IBRAHIM: Note here that pointer *p and array in heap new int[5] should always be of same data type**
- The same thing is written in single line

```c++
int *p = new int[5];
```

**Heap Memory De-allocation**

- One more difference is stack memory is automatically deleted when the array goes out of scope
  but heap memory will be there as long as program is running hence if you need heap memory for 
  a limited amount of time then you should also DE-ALLOCATE it.

```c++
- delete []p; // here we write [] as we have created an array in heap
- p = NULL; // This means that pointer p is not pointing anywhere. 
- p = nullptr; // Also in mordern C++ we can use nullptr instead of NULL.
```

- If we write p=NULL before delete []p then pointer is not pointing to the memory in heap 
  but the memory is still there as long as program is running. This problem is called Memory leak problem.

**Accessing array in heap memory**

- Similar to regular array the array in heap can be accessed using same syntax P[2] = 15;
- Here note that pointer to an array P is treated the same way as name of an array.

### Dynamically changing the size of memory in heap

To understand this concept first consider the example where it is not possible to change the size of memory in stack

```c++
#include <iostream>

using namespace std;

int main()
{
    int size;
    cout << "Enter number of elements";
    cin >> size;
    int A[size];

    cout << sizeof(A) << endl;
    // This array A is created inside stack
    // Now if we want to change the size of this array using the command
    // below then it is not possible, there is no such syntax in c++

    //size = 35; This cannot be done
    //A[size];

    return 0;
}
```

**But this can be done using heap by creating a dynamic array in heap.**

```c++
#include <iostream>

using namespace std;

int main()
{
    int *p = new int[20];

    delete []p; // Always delete the older array in heap before declaring the new array pointed by the same pointer p or else it will result in memory leak.


    p = new int[40]; // here now using the same pointer we have created a new array of larger size 40. This is the advantage of having a heap or dynamically creating a memory

    return 0;
}

```

## Reference

* In C++, a reference is a type of variable that acts as an alias for another object or variable.
* To declare a reference in C++, you use the ampersand symbol (&) after the data type. For example:

```c++
#include <iostream>

using namespace std;

int main()
{
    int x = 5; // let us say x is stored in memory location 200/ 201
    int& ref_x = x; // here ref_x is alias or nickname of the x. you can acess the same memory location using both x and ref_x name

    x++;  // value at memory address incremented by 1, x = 6
    ref_x++; // value at memory address incremented by 1, x = 7
    cout << x << " " << ref_x << endl; // this both will print the value at 200
}
```

* In this code, `ref_x` is a reference to `x`. Any changes made to `ref_x` will also affect `x`.

**Concept behind the address-of operator:**

**R-Value Vs L-Value**

  ```c++
int a;
a = x; // x is called r value, 12 will be stored in a. hence here x is "data", literal, constant value.
x = 25; // here x is called l value. Here we want 25 to be stored in the location (200) where x is pointing. the data at this location (200) gets overwrtitten by 25. So In this case x is "address of x"
  ```

- **Variable written on right hand side r-value means "DATA"**
- **Variable written on left hand side l-value means "ADDRESS"**

**Case when L-Value is assigned to the variable on left hand side**

```c++
int& y = x; // here though x is written on right but what is given to the name of y ?. The same address which x is poiting to. 
// This means the x here is l-value of x;
```

**Reference does not occupy any memory**

Here x is occupying 2 bytes of memory (Integer). Then what amount of memory y is occupying ?. Answer is y is not occupying any memory. hence "REFERENCE DOES NOT OCCUPY ANY MEMORY".

**Reference  name cannot be used for any other variable**

Once the Alias or reference y is created. The name "y" cannot be used as a reference for any other variable.
int &y = a; // This cannot be written in the same function at all.

```c++
#include <iostream>

using namespace std;

int main()
{
    int x = 25; // here x is called l value. Here we want 25 to be stored in the location (200) where x is pointing. the data at this location (200) gets overwrtitten by 25. So In this case x is "address of x"
    int a = x; // x is called r value, 12 will be stored in a. hence here x is "data", literal, constant value.
    int& y = x; // here though x is written on right but what is given to the name of y ?. The same address which x is poiting to. 
// This means the x here is l-value of x;

    cout << x << " " << a << " " << y << endl;
    a++; // x value will not change
    cout << x << " " << a << " " << y << endl;
    y++; // x value will get changed. Reference does not occupy any memory but is pointing to same memory address
    cout << x << " " << a << " " << y << endl;
}
```

**Difference between Pointer and Reference :** 

* Pointer Ptr creates a separate memory location containing the address of x
* ref does not create a separate memory location but is the variable which points towards the same address of x

```c++
#include <iostream>

using namespace std;


int main()
{
    int x = 25;
    int* Ptr = &x;
    int& ref = x;

    cout << "data of x = " << x << endl;
    cout << "address of x = " << &x << endl;
    cout << "data of ref = " <<  ref << endl;
    cout << "address of ref = " <<  &ref << endl;
    cout << "data of Ptr = " << Ptr << endl;
    cout << "address of Ptr = " << &Ptr << endl;
    
    }
```

**Creating alias of a pointer**

```c++
#include <iostream>

using namespace std;


int main()
{
    int x = 5;
    int* ptr_x = &x;  // ptr_x is a pointer to x
    int*& ref_ptr_x = ptr_x;  // ref_ptr_x is a reference to ptr_x

    //*ref_ptr_x = 10;  // modifies the value of x

    cout << "data of x = " << x << endl;
    cout << "address of x = " << &x << endl;
    cout << "data of ptr_x = " <<  ptr_x << endl;
    cout << "address of ptr_x = " <<  &ptr_x << endl;
    cout << "data of ref_ptr_x = " << ref_ptr_x << endl;
    cout << "address of ref_ptr_x = " << &ref_ptr_x << endl;

    // dereferences  value of x
    cout << "data of x = " << *ptr_x << endl;
    cout << "data of x = " << *ref_ptr_x << endl;
    }
```

In this code, `ptr_x` is a pointer to `x`. The line `int*& ref_ptr_x = ptr_x;` creates a reference `ref_ptr_x` to the pointer `ptr_x`. Any changes made to `ref_ptr_x` will affect `ptr_x`.

The last line `*ref_ptr_x = 10;` dereferences `ref_ptr_x` (i.e., gets the value pointed to by `ptr_x`) and assigns the value `10` to it. This modifies the value of `x` to `10`.

**References are often used as function parameters to avoid creating a copy of an object.** For example:

```c++
void double_value(int& value) {
    value *= 2;
}

int main() {
    int x = 5;
    double_value(x);
    std::cout << x << std::endl;  // outputs 10
    return 0;
}
```

In this code, `double_value` takes a reference to an `int` and doubles its value. When `double_value(x)` is called, it modifies the value of `x`.

## Pointer to a function

* In C++, a pointer to a function is a variable that holds the memory address of a function. It can be used to call the function indirectly or to **pass the function as an argument to another function.**
* Here is an example of declaring a pointer to a function:

```c++
int add(int x, int y) {
    return x + y;
}

int (*ptr_add)(int, int) = &add;
```

* In this code, `add` is a function that takes two `int` arguments and returns their sum. `(*ptr_add)` declares a pointer to a function that takes two `int` arguments and returns an `int`. `&add` assigns the address of the `add` function to `ptr_add`.

* The pointer to a function can be called like a regular function using the function call operator `()`. Here is an example:

```c++
int result = (*ptr_add)(3, 4);
std::cout << result << std::endl;  // outputs 7
```

* In this code, `(*ptr_add)(3, 4)` calls the `add` function indirectly through the pointer `ptr_add`. The result is assigned to `result` and printed to the console.

* A pointer to a function can also be passed as an argument to another function. Here is an example:

```c++
void apply_operation(int x, int y, int (*op)(int, int)) {
    int result = (*op)(x, y);
    // int result = op(x,y); // This is allowed too
    std::cout << result << std::endl;
}

int multiply(int x, int y) {
    return x * y;
}

int main() {
    apply_operation(3, 4, &add);  // outputs 7
    apply_operation(3, 4, &multiply);  // outputs 12
    //  apply_operation(3, 4, multiply);  // This is allowed too
    return 0;
}
```

* Notice in the example above for a function `&multiply` and `multiply` has the same meaning as whenever the function is created the address(lvalue) is transferred to op. But this is not the case with the data. For a data `&variable` means address(lvalue) and `variable` means data(rvalue),
* Similarly while dereferencing `*op` and `op` is the same as op always contains address of the function.

**Introductory Example - Calling function by pointer name**

```c++
#include <iostream>

using namespace std;

void display(int x)
{
    cout << "Value" << endl;
    cout << x << endl;
}

int main()
{
    /*Call by Function Name*/
    display();

    /*Call by Pointer Name*/

    // Function Declaration
    void (*fp) (int); // Declaration syntax is return type(*name of the pointer, fp is function pointer) (parameters type)


    // Pointer Initialization
    //fp = &display; // this will assign the address of the function to this pointer.
    fp = display; // This is allowed too

    // Function call
    //(*fp)(2);
    fp(2); // This is allowed too

    return 0;
}
```

**Function Overriding example to achieve runtime polymorphism**

```c++
#include <iostream>

using namespace std;


int max(int x, int y)
	{
		return x>y?x:y;
		}
		
int min(int x, int y)
	{
		return x<y?x:y;
		}
		
int main()
{
	int(*fp)(int, int); // Declaration 
	fp = &max; // Initialization
    //fp = max; // This is also valid as address of the function will be assigned but using & is better
	cout << (*fp)(10,5) << endl; // function call
	fp = &min; // Now the same pointer is initialized to min function
	cout << (*fp)(10,5) << endl; // now min function is called using the same name or function call. This is called as polymorphism.
	}
```

# Functions

* Function is a module which performs a specific task. Functions are used for procedural programming and modular programming. Collection of functions is called as library.
* Monolithic programming is when all the codes are written in single program without the use of functions.

```c++
int add (int x, int y)
{
    int z;
    z = x+y;
    return z;
}

void main()
{
    int a = 10, b=15, c;
    c = add(a,b);
    cout << c << endl;
    return 0;
}
```

- **The variables for both the main function and add function will be created inside the stack. This is called as activation record.** Now when the function is called and after the completion of the function the memory of the function inside the stack is removed automatically. hence its activation record is deleted.
- Note that this is not the case with heap. If the function has allocated some memory in heap then that will not get de-allocated automatically. FUNCTION SHOULD RELEASE IT BY SAYING DELETE.
- Now once the function ends then its activation record that is all the variables from the memory will also 
  be cleared.

## Function Overloading 

* You can write the same function with different arguments list. If More than one functions can have same name, but different parameter list, then they are overloaded functions. This is called as function overloading.
* **Return type is not considered in overloading**.
* **Function overloading is used for achieving compile time polymorphism**.

**Program to Demonstrate Function Overloading using Sum function**

```c++
int add(int x, int y)// 2 arguments
{
	return x+y;
}

int add(int x, int y, int z)// 3 arguments
{
	return x+y+z;
}

float add (float x, float y)
{
	return x+y;
}


void main()
{
int a=10, b=5, c, d;
c = add(a,b);
d = add(a,b,c);


int i=2.5f, j=3.5f, k; // here it is COMPULSARY to write f or else the data will be considered as default "DOUBLE" and function overloading will fail.
k=add(i,j); // here 1st and 3rd functions are also diff as they have different argument datatype though the same number of the arguments.
}

```

**FUNCTION CANNOT BE DIFFERENTIATED BASED ON RETURN TYPE**

```c++
int max (int, int)
float max (int, int) 
```

These two functions are not different and hence will give "NAME CONFLICT".

Two functions are different only based on the type of the input argument or the number of arguments
BUT NOT THE RETURN TYPE.

## Parameter Passing

### 1. Pass by Value

* Pass by value - **values** of Actual parameters are passed to formal parameters. **Actual 
  parameters cannot be modified by function**
* Value of actual parameters are copied in formal parameters.
* **If any changes done to formal parameters in function, they will not modify actual** 
  **parameters.**

```c++
int swap (int a, int b) // formal parameters
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int main()
{
    int x =10, y=20; // actual parameters
    swap(x,y);
    cout << x << " " << y;
}
```

- The function swap and all the variables a and b gets deleted once the function is completed. Here the value of x and y will still be the same but a and b will get swapped. 
- **Call by value is used when you have the function which works on the parameters and RETURN the result.**
- In our example the swap function is not returning anything hence call by value cannot be used for the
  operations like swap.

### 2. Pass by address

- Pass by address - **Address** of Actual Parameters are passed to a function, formal 
  parameters must be pointers. **Function can indirectly access actual parameters.**
- Address of actual parameters are passed.
- Formal parameters must be pointers. Formal parameters can indirectly access actual parameters.
- Changes done using formal parameters will reflect in actual parameters

```c++
int swap (int *a, int *b) // formal parameters are pointers
{
int temp;
temp = *a; // pointer dereferencing 
*a = *b; // actual data is accessed and the values are swapped.
*b = temp;
}


int main()
{
int x =10, y=20; // actual parameters are address of variables
swap(&x,&y); // addresses are sent instead of values
cout << x << " " << y;
}
```

- Hence accessing variables of one function through another function is not possible but it is made possible through the use of pointers

- **Pointers thus gives the power to the function to access the parameters of the calling function**

### 3. Pass by Reference - ONLY AVAILABLE WITH C++

* Pass by reference - Actual parameters are passed as **reference** to formal parameters, 
  **Function can modify actual parameters.** // not available in C language.
* Actual parameters are passed as reference. Formal parameters can directly access actual parameters
* Function call is converted into inline function, if not possible it will become call by 
  address
* Reference don’t take extra memory
* Syntax is same as Call by Value except, formal parameters are reference

```c++
int swap (int &a, int &b) // formal parameters // NOTICE THE &
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}


int main()
{
    int x =10, y=20; // actual parameters
    swap(x,y);
    cout << x << " " << y;
}
```

- But we have studies that reference are nothing but the aliases. hence x=a and y=b
- But then how it is possible that the function swap can directly access the variables of main. We have studied that it is not possible.
- Answer is when the machine code is generated then in the machine code of main function swap function is copied.
- **Call by reference thus will NOT CREATE SEPARATE PIECE OF MACHINE CODE like call by value and call by address. machine code will not have two different pieces of modules or functions.**
- swap here is not a separate function but the part of main function only. 
- Same part of main function is calling x as a and y as b. 
- **HENCE THERE IS NO ACTIVATION RECORD CREATED. HENCE THE FUNCTION IS NOT CALLED IN THE MACHINE CODE. We just wrote it separate in the source code.**

**NOTE THAT IT IS POSSIBLE THAT IN THE SAME FUNCTION ONE VALUE IS CALLED BY VALUE , OTHER BY CALL BY ADDRESS AND OTHER BY CALL BY REFERENCE**

**Inline Functions**

- When the piece of the machine code of the function is copied at the place of function call then such functions are called as INLINE FUNCTIONS.

## Parameter Returning

Similar to Passing a value there are three ways of returning a value :

1. Return by value
2. Return by address
3. Return by Reference

### 1. Return by value

- Known way of returning the calculated value from a function

### 2. Return by Address

- A function can return address of memory
- **It should not return address of local variables, which will be disposed after function ends**
- It can return address of memory allocated in heap

```c++
#include <iostream>

using namespace std;

int* fun(int size) // return type is pointer of type integer
{
	int* p = new int[size];  // creates a new array in the heap. pointer gets the address of the array.

	for (int i=0; i<size; i++)
		p[i] = i+1; 

	return p;

} // This function creates array in the heap. fills the elements in the array and then returning the address of the pointer.


int main() {
	int *ptr = fun(5); // This is allowed only because the function is not deleting the memory in heap.
	for(int i=0; i<5; i++)
		cout << ptr[i] << endl;
		
	delete[] ptr;	// Free the memory allocated in fun
	return 0;
} // the pointer of the main function ptr is now pointing at the address of the array.
```

**ADDRESS OF THE LOCAL VARIABLE CANNOT BE RETURNED BACAUSE ONCE THE FUNCTION ENDS VARIABLES ARE DEALLOCATED FROM THE MEMORY int * fun()**

```c++
{
	int x=10;
	return &x;	//Will get warning Address of stack memory associated with local variable 'x' returned
	}
```

**ADDRESSES OF THE HEAP MEMORY CAN ONLY BE RETURNED**

### 3. Return By Reference

```c++
int & fun(int &a) // --> call by reference (int &a) and return by reference & fun
    {
        cout << a;
        return a; // here reference of x is returned which is x only. hence the fun(x) is equal to x
    }

int main()
    {
    int x=10;
    //y = fun(x); // we always take return result of a function in a variable in call by value. 
    // function always comes on the right side of the assignment.

    //fun(x); // here now fun(x) = x only, as reference to a is x
    fun(x) = 25;  //hence now function is written on the LEFT SIDE and FUNCTION IS acting as a reference of variable x

    cout << x;
    }

// Here a and x are the value at the same memory location
```

## Global Variables Access & Scope Resolution Operator

Global Variables:

- These are the variables declared outside all the function and can be accessed by all the functions.

Local Variables:

- These are the functions declared inside the function and gets de-allocated once the function gets executed.

```C++
#include <iostream>

using namespace std;

int g=0;

int fun()
    {
        int a=5;
        g=g+a;
        cout << g << endl;
		return 0;
    }

int main()
    { 
        g=15;
        fun();
        g++;
        cout << g << endl;
		return 0;
    }
```



- Local variables remains in the memory as long as the function is running. 
- Global variables remains in the memory as long as the program is running.
- **Global variables are allocated in the code section and not in stack.**
- **Global variables will get the memory at the loading time of the program itself**.

- **Program always looks for the declaration of the variable in the nearest scope. **
- **If we have local and global variable of the same name then the local variable will be accessed first.**
- **Variables in C++ have block level scope**

**TO ACCESS THE GLOBAL g WE SHOULD USE SCOPE RESOLUTION :: e.g. cout<<::g<<endl;**

In C++, scope resolution refers to the ability to access a variable or function in a particular scope, even if there is another variable or function with the same name in a different scope. The scope resolution operator is the double colon `::` and it is used to specify the scope of a variable or function.

Here are some examples of how to use the scope resolution operator in C++:

```C++
#include <iostream>
using namespace std;

int globalVar = 10; // global variable

int main() {
    int globalVar = 5; // local variable
    cout << "The global variable is: " << ::globalVar << endl; // using scope resolution operator to access global variable
    cout << "The local variable is: " << globalVar << endl;
    return 0;
}
```

## Static Variable

* In C++, a static variable is a variable that retains its value between function calls and has a lifetime that lasts for the entire program execution. It is declared with the keyword "static" and can be either a local variable or a global variable.
* They have local scope but remain in memory thru out the execution of program.
* They are created in code section. They are history-sensitive.
* Static variables are Global variables but with the scope limited only to the function in which they are declared. Similar to the global variables these static variables are also assigned in the code section during the program loading.

```c++
// Example 1:

#include <iostream>

using namespace std;

int globalVariable = 0; // Global Variable

void myFunction()
{
	static int staticVariable = 0;
	int localVariable = 0;
	staticVariable++;
	globalVariable++;
	cout << localVariable << " " << staticVariable << " " << globalVariable << endl;
}

main()
{
	myFunction(); 
	myFunction(); 
	myFunction(); 
	// cout << staticVariable << " " << globalVariable << endl; // Notice here that unlike globalVariable, staticVariable can be accessed only in the function
}
```

* In this example  staticVariable will always remain in the memory during the execution of the program like staticVariable **BUT IT CAN BE ACCESSED ONLY BY FUNCTION myFunction().**
* staticVariable is not created each time myFunction() is called but is created only first time.

# ---------Less Important Topic------------

# Operators and Assignments

## Enum and Type Def

## 1) Enum

- Many times in programming it is required to assign a code to the variable. This can be assigned as follows:

```c++
const int CS = 0;
const int ECE = 1;
const int IT = 2;
const int civil = 3;
```

- Instead of doing this we can assign constants using the enum. This will also declare a user defined datatype. Let us define a new datatype named dept

```C++
enum dept {cs, ece, it, civil}; // by doing this cs = 0, ece = 1... will be assigned automatically
```

- We can also define the constants the way we want

```c++
enum dept {cs=1, ece, it, civil}; // ece will be assigned 2 automatically
```

- Also now we can use these names in the code as a new user defined datatype

```c++
int main()
	{
		dept d;
		d = cs;
		d = ece
	}
```

- You can also do this :

```c++
enum day {mon=1, tue, wed=5, thur, fri, sat=9, sun} // notice that thur=6, fri=7 will be assigned automatically
```

- now we can use : 

```c++
int main()
	{
		day d;
		d=mon;
		d=fri;
		// d=0; // This is not allowed
    	// mon++; // This is not allowed
		}
```

- **Note that constants assigned using enum cannot be modified. you cannot do something like d = mon++**

**Program Demonstrating the use of enum**

```C++
#include <iostream>

using namespace std;

enum day{mon, tue, wed}; // day is a user-defined datatype which will take the values from mon to wed i.e. 0 to 3

int main()
{
    day d; //d ia a variable of type day
    d=tue;
    d = wed;
    // d = 1; This is not allowed
    // mon++;
    cout<<d<<endl;

}

```

- In C++, an `enum` is a user-defined data type that consists of a set of named constants, or "enumerators". Each enumerator is assigned an integer value, which can be used to represent the constant in the code. The `enum` keyword is used to define an enumeration type.
- Here's an example of how to define and use an `enum` in C++:

```c++
#include <iostream>

enum Color {
    RED,
    GREEN,
    BLUE
};

int main() {
    Color favoriteColor = GREEN;
    std::cout << "My favorite color is: ";
    switch (favoriteColor) {
        case RED:
            std::cout << "red";
            break;
        case GREEN:
            std::cout << "green";
            break;
        case BLUE:
            std::cout << "blue";
            break;
    }
    std::cout << std::endl;
    return 0;
}

```

## 2) TypeDef

- Typedef is used to address the readability issue.

- In C++, `typedef` is a keyword that allows you to create a new name for an existing data type. The syntax for `typedef` is as follows:

  ```c++
  typedef existing_data_type new_name;
  ```

- Here, `existing_data_type` is the data type for which we want to create a new name, and `new_name` is the new name that we want to give to the data type. Once we create a new name using `typedef`, we can use the new name in our code instead of the existing data type.

- We can use datatype to know what does the variable mean.

  ```C++
  int main()
  	{
  	int m1, m2, m3, r1, r2, r3;
  	}
  ```

- Here m are marks and r are roll  numbers

- We can define m's and r's as datatype to make it more readable

  ```C++
  typedef int marks;
  typedef int rollno;
  
  int main()
  	{
  		marks m1, m2, m3;
  		roll no r1, r2, r3;
  	}
  ```

- Here if we forgot what are m1, m2, etc we can know from the typedef
  that it is marks datatype with int datatype.

# Conditional Statements

## Dynamic Declaration - Special if statement

- Note that if you define a variable in a function then the memory for that function is allocated dynamically during the function only and removed from the memory once you exit the function

```C++
if ()
{
	int k;
}
```

- Now k will be allocated memory in heap and will removed from heap once you exit the if() function.
- Consider this situation:

```C++
int main()
{

int a,b,c;
int k = exp;

if (k<a)
	{				// now we want the scope of this variable inside the if only
	}

if (int k=exp; k<a) // hence C++17 onwards provides this function to declare the scope just inside this if
	{
	}

}
```

- If you want to limit the scope of any variable then enclose it inside the dummy block { }

```c++
{
int d=a-b;
if(true)
	{
 cout<<d<<endl;
     }
 }
 cout<<d<<endl; // here d won't be accessible here as it's scope has ended in the last bracket

 
```

## Nested Switch

- Switch statement inside a switch statement.

- Switch is used for menu-driven programs like file option in notepad will have New, Save, Save as, etc

  **Menu Driven Program using Switch Case**

```c++
#include <iostream>
using namespacestd;
int main()
{
    cout<<"Menu"<<endl;
    cout<<"1. Add\n"<<"2. Sub\n"<<"3. Mul\n"<<"4. Div\n";
    int option;
    cout<<"Enter your choice no."<<endl;
    cin>>option;
    int a,b,c;
    cout<<"Enter two numbers"<<endl;
    cin>>a>>b;
    switch(option)
    {
        case 1: c=a+b;
        break;
        case 2: c=a-b;
        break;
        case 3: c=a*b;
        break;
        case 4: c=a/b;
        break;
    }
    cout<<c<<endl;
    return 0;
}
```

# Pointers

## Problems with pointers

### 1. **Uninitialized pointer**

- In C++, uninitialized pointers are pointers that have not been initialized with a valid memory address. An uninitialized pointer can contain any random value that happened to be stored in the memory location it points to, which may or may not be a valid memory address.
- Here is an example of an uninitialized pointer:

```C++
int* ptr;
  *p = 25; // Now if we assign a value to the location where pointer is pointing than this data is stored in some unknown garbage location.
```

- In this example, "ptr" is an uninitialized pointer to an integer. It doesn't point to any valid memory address yet, and trying to access the value it points to will result in undefined behavior. If we try to dereference this pointer before assigning it a valid address, **we will likely get a segmentation fault error:**

```C++
int x = *ptr;  // undefined behavior: ptr is uninitialized and does not point to a valid memory address
```

- To avoid uninitialized pointers, it's important to always initialize pointers with a valid memory address before using them to store or access values. We can initialize a pointer 
  1. with the address of a variable using the address-of operator (&), 
  2. or by allocating memory for it on the heap using the new operator

```C++
int x = 10;
int* ptr1 = &x;          // initialize ptr1 with the address of x
int* ptr2 = new int(20); // initialize ptr2 with a dynamically allocated memory location on the heap
```

**Example of Segmentation Fault**

```c++
#include <iostream>

using namespace std;

int main()
{
    int *ptr = new int(5);
    //int *ptr = new int;
    //*ptr = 5;
    cout << ptr << endl;
    cout << *ptr << endl;

    delete ptr;
    ptr = nullptr;

    cout << *ptr << endl; // Will throw Segmentation Fault Error

    return 0;
}
```

### 2. Memory Leak

- If we don't de-allocate the memory declared in the heap then we say that memory is leaked in the heap.

```c++
int *p = new int[5];

delete []p;
p = NULL; //we should never do this unless we have remove the memory from heap using the stamement above
```

### 3. Dangling Pointers

- In C++, a dangling pointer is a pointer that points to a memory location that has been deallocated or otherwise freed. Dangling pointers can be dangerous because they can cause unexpected behavior or crashes when accessed.

 Here's an example of a dangling pointer:

```c++
int* ptr = new int;  // allocate memory for an integer on the heap
*ptr = 10;           // store a value in the allocated memory
delete ptr;          // free the memory pointed to by ptr
ptr = nullptr;       // set ptr to nullptr to avoid accessing freed memory
```

- After the memory has been deallocated using the "delete" operator, the pointer "ptr" becomes a dangling pointer because it still points to the memory location that has been freed. If we were to try to access the value pointed to by "ptr" at this point, we could get unexpected behavior or a crash:

```c++
int x = *ptr;  // undefined behavior: accessing freed memory through a dangling pointer
```

- To avoid dangling pointers, it's important to always set pointers to nullptr after freeing their memory, and to avoid accessing memory through pointers that may have become invalid due to deallocation or other operations.
- Another common source of dangling pointers is when a pointer is used to point to a local variable that goes out of scope. For example:

```c++
#include <iostream>

using namespace std;

int* get_pointer() {
    int x = 10;
    return &x;  // return a pointer to the local variable x
}

int main()
{
    int* ptr = get_pointer();  // ptr points to the memory location of x
    int y = *ptr;              // undefined behavior: x has gone out of scope, ptr is now a dangling pointer. Segmentation Fault will occur as we're trying to access undefined location.
    }


```

- In this example, the pointer "ptr" points to the memory location of the local variable "x" inside the "get_pointer()" function. When "get_pointer()" returns, the memory allocated for "x" goes out of scope and is no longer valid. If we try to access the value pointed to by "ptr" at this point, we could get unexpected behavior or a crash.

- To avoid this kind of dangling pointer, it's important to ensure that pointers are not used to point to local variables that may go out of scope. If we need to return a pointer to a value, we can allocate memory for the value on the heap instead, and return a pointer to that memory location:

  ```c++
  #include <iostream>
  
  using namespace std;
  
  int* get_pointer() {
      int* ptr = new int(10);
      return ptr;
  }
  
  int main()
  {
      int* ptr = get_pointer();  // ptr points to dynamically allocated integer on heap
      int y = *ptr;              // y is now equal to 10
      cout << y << endl;
      delete ptr;  // free the memory allocated for the integer
      ptr = nullptr;
  }   
  ```

- In this example, we allocate memory for an integer on the heap using the "new" operator, and return a pointer to that memory location. The pointer is not dangling because the memory has been dynamically allocated and will not be deallocated until we explicitly free it using the "delete" operator.

# Functions

## Function Template

- A function template in C++ is a way to define a generic function that can work with different data types. It allows programmers to write a single function that can handle multiple types of input parameters.
- Function templates are used for defining generic functions. They work for multiple data types
- Data type is decided based on the type of value passed
- Data type is a template variable
- Function can have multiple template variables
- **TEMPLATE WORKS FOR ANY DATATYPES. EVEN FOR THE OBJECTS OF YOUR CLASSES.**

Let's say we have 2 functions (overloading)

```c++
int max (int x, int y)
{
    if (x>y)
    return x;
    else
    return y;
}

float max (float x, float y)
{
    if (x>y)
    return x;
    else
    return y;
}
```

- Here body of the two functions is the same hence is it possible that we have only one function which 
  can take the arguments of any datatype. This is called as function template.

```c++
#include <iostream>
using namespace std;

template <class T> // here T is class of type template.
// template <typename T> // This is true as well
T max (T x, T y)
{
    if (x > y) return x;
    else return y;
}

main()
{
    int c = max(9,5) ; // This will now print the answer in int using the same function
    float d = max(10.5f, 6.9f); // This will now print the answer in float using the same function
    max(2.3f,5.6); // This will give an error because both the datatype has to be of same template T.
    // compiler here is unable to decide the datatype thus causing ambiguity.
}
```

## Recursive Function

- A recursive function in C++ is a function that calls itself repeatedly until a certain condition is met. This can be useful when you need to solve a problem that can be broken down into smaller sub-problems that are similar in nature.

```c++
#include <iostream>
using namespace std;

int factorial(int n) {
   if(n == 0) {
      return 1;
   } else {
      return n * factorial(n-1);
   }
}

int main() {
   int n;
   cout << "Enter a number: ";
   cin >> n;
   cout << "Factorial of " << n << " is " << factorial(n) << endl;
   return 0;
}

```

- Note that recursive functions can be inefficient and may lead to stack overflow errors if they recurse too deeply. Therefore, it's important to make sure that the recursion has a clear termination condition and that the function doesn't recurse too deeply.