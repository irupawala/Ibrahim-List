[10] Functions

## [10.1] Introduction

- Function is a module which performs a specific task
- Functions are used for procedural programming and modular programming.
- Collection of functions is called as library.
- Monolithic programming is when all the codes are written in single program without the use of functions.
- Problems with Monolithic programming :
  1. Programmer has to memorize the entire program can't focus on just one function
  2. If there is an error entire program will crash
  3. Program development cannot be shared between multiple programmers
  4. Program cannot be accommodated by the machine of smaller memory.

- Programs written using function is called as modular programming. 

- Syntax:
	return_type function_name (parameter list)

- Function can take zero or more inputs.
- **Function may or may not return value but can return "ATMOST" one value.**
- Void function don’t return any value.
- Default return type is int.

* **AVOID using Cin and Cout in function. Not considered as good programming practice.**



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

- **The variables for both the main function and add function will be created inside the stack. This is called as activation record.**

- Now when the function is called and after the completion of the function the memory of the function inside the stack is removed automatically. hence its activation record is deleted.

- Note that this is not the case with heap. If the function has allocated some memory in heap then that will not get de-allocated automatically. FUNCTION SHOULD RELEASE IT BY SAYING DELETE.

- Now once the function ends then its activation record that is all the variables from the memory will also 
be cleared.

- Also notice the the machine code for the main function and other functions will also be different as
in the original function.

**Example of Simple Function**

```c++
#include <iostream>
using namespace std;
void display()
{
cout<<"Hello";
}
int main()
{
display();
return 0;
}
```

**Example of Function with Arguments**

```c++
#include<iostream>
using namespace std;
float add(float x,float y)
{
float z;
z=x+y;
return z;
}
int main()
{
float x=2.3,y=7.9,z;
z=add(x,y);
cout<<z<<endl;
return 0;
}
```

**Example of function to find Maximum of 3 number**

```c++
#include <iostream>
using namespace std;
int maxim(int a,int b,int c)
{
    if(a>b && a>c)
    return a;
    else if(b>c)
    return b;
    else
    return c;
}
int main()
{
    int a,b,c,d;
    cout<<"Enter three no.s ";
    cin>>a>>b>>c;
    d=maxim(a,b,c);
    cout<<"Maximum is "<<d<<endl;
    return 0;
}
```

## [10.2] Function Overloading 

- You can write the same function with different arguments list. If More than one functions can have same name, but different parameter list, then they are overloaded functions. This is called as function overloading.
- This feature is not available in c but c++ compiler is able to differentiate the functions with different arguments list
- The advantage is we can have the same name for same functionality.
- **Return type is not considered in overloading**
- **Function overloading is used for achieving compile time polymorphism**

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

**Program to Demonstrate Function Overloading using Sum function**

```c++
#include <iostream>
using namespace std;
int sum(int a,int b)
{
return a+b;
}
float sum(float a,float b)
{
return a+b;
}
int sum(int a,int b,int c)
{
return a,b,c;
}
int main()
{
cout<<sum(10,5)<<endl;
cout<<sum(12.5f,3.4f)<<endl;
cout<<sum(10,20,3)<<endl;
return 0;
}
```

## [10.3] Function Template

- Function templates are the functions which are "GENERIC". Generalized in terms of data type.
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
template <class T> // here T is class of type template.

T max (T x, T y)
{
    if (x>y)
    return x;
    else
    return y;
}

main()
{
    int c = max(9,5) ; // This will now print the answer in int using the same function
    float d = max(10.5f, 6.9f); // This will now print the answer in float using the same function

    max(2.3f,5.6); // This will give an error because both the datatype has to be of same template T.
    // compiler here is unable to decide the datatype thus causing ambiguity.
}
```

**Example of Function Template**

```c++
#include <iostream>
using namespacestd;
template<classT>
T maxim(T a,T b)
{
	returna>b?a:b;
}
int main()
{
    cout<<maxim(12,14)<<endl;
    cout<<maxim(2.3,1.4)<<endl;
    cout<<maxim(2.3f,5.6f)<<endl;
    return 0;
}
```

## [10.4] Default Arguments

• Parameters of a function can have default values
• If a parameter is default then , passing its value is options
• Function with default argument can be called with variable number of argument
• Default values to parameters must be given from right side parameter
• Default arguments are much useful in constructors
• Default arguments are useful for defining overloaded functions

```c++
int add (int x, int y)
{
return x+y;
}

int add (int x, int y, int z)
{
return x+y+z;
}

int main()
{
int a = add(2,5);
int b = add(2,5,8);
int c = add(2, 5, 0); 
    
return 0;
}
```

- here the result of a and c will be the same. Hence we can have a single function if the value of the third 
argument by default is 0.
- This can be done by assigning the default value of the third argument as 0.

```c++
int add (int x, int y, int z=0) // This is called as default argument. And using default argument you can combine the overloaded function and write them as a single function.
{
return x+y+z;
}
```

**YOU MUST DEFINE DEFAULT ARGUMENTS FROM RIGHT TO LEFT.**

- Note that if you write default arguments like this `int func (int a=0; int b; int c=0; int d=0).`
then the compiler will get confused. you cannot skip one argument in between default arguments

## [10.5] Parameter Passing

* What are the methods by which function can take parameters ?.

1. Pass by value - **values** of Actual parameters are passed to formal parameters. **Actual 
   parameters cannot be modified by function**
2. Pass by address - **Address** of Actual Parameters are passed to a function, formal 
   parameters must be pointers. **Function can indirectly access actual parameters.**
3. Pass by reference - Actual parameters are passed as **reference** to formal parameters, 
   **Function can modify actual parameters.** // not available in C language

**NOTE THAT IT IS POSSIBLE THAT IN THE SAME FUNCTION ONE VALUE IS CALLED BY VALUE , OTHER BY CALL BY ADDRESS AND OTHER BY CALL BY REFERENCE**

### 1. Pass by value

* Value of actual parameters are copied in formal parameters
* If any changes done to formal parameters in function, they will not modify actual 
  parameters

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

- The function swap and all the variables a and b gets deleted once the function is completed

- Here the value of x and y will still be the same but a and b will get swapped. 
- **Hence call by value method cannot modify the actual parameters by the change in formal parameters.**
- **Call by value is used when you have the function which works on the parameters and RETURN the result.**
- In our example the swap function is not returning anything hence call by value cannot be used for the
operations like swap.

### 2. Pass by address

* Address of actual parameters are passed.
* Formal parameters must be pointers
* Formal parameters can indirectly access actual parameters.
* Changes done using formal parameters will reflect in actual parameters



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

* Hence accessing variables of one function through another function is not possible but it is made possible through the use of pointers

- **Pointers thus gives the power to the function to access the parameters of the calling function**

### 3. Pass by Reference - ONLY AVAILABLE WITH C++

* Actual parameters are passed as reference
* Formal parameters can directly access actual parameters
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
- Also temp is created temporarily in the activation record of main only until the swap code is executed.
- ALWAYS USE CALL BY REFERENCE FOR SIMPLE FUNCTIONS OR ELSE THE COMPILER WILL AUTOMATICALLY CHANGE IT TO CALL BY VALUE.
  - e.g. if we write a for loop inside the function it will be changed to CALL by VALUE

#### Inline Functions

- When the piece of the machine code of the function is copied at the place of function call then such functions are called as INLINE FUNCTIONS.

## [10.6] Parameter Returning

Similar to Passing a value there are three ways of returning a value :

1. Return by value
2. Return by address
3. Return by Reference

### 1. Return by value

- Known way of returning the calculated value from a function

### 2. Return by Address

* A function can return address of memory
* It should not return address of local variables, which will be disposed after function ends
* It can return address of memory allocated in heap

```c++
int * fun(int size) // return type is pointer of type integer

{
int *p = new int[size];  // creates a new array in the heap. pointer gets the address of the array.

for (int i=0; i<size; i++)
	p[i] = i++; // fill the elements with i+1

return p;

}// This function creates array in the heap. fills the elements in the array and then returning the address of the pointer.


int main()
{
int *ptr=fun(5); // This is allowed only because the function is not deleting the memory in heap.
for(int i=0; i<5; i++)
	cout << ptr[i] << endl;
    
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

## [10.7] Global Variables Access & Scope Resolution Operator

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

* **Program always looks for the declaration of the variable in the nearest scope. **
* **If we have local and global variable of the same name then the local variable will be accessed first.**
* **Variables in C++ have block level scope**

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



## [10.8] Static Variables

* They have local scope but remain in memory thru out the execution of program.
* They are created in code section. They are history-sensitive
* Static variables are Global variables but with the scope limited only to the function in which they are declared.

- Similar to the global variables these static variables are also assigned in the code section during the program loading.

```c++
// Example 1:

int v=0;

void fun()
{
int a=5;
v++;
cout << a << " " << v << endl;
}

main()
{
fun(); // 5, 1
fun(); // 5, 2
fun(); // 5, 3
}
```

* here variable v can be accessed by both main and fun
* a here is a local variable created and destroyed each time the function is called.
* v is global variable allocated in the code section and remaining there throughout the program
  and accessible by both the functions.

```c++
// Example 2:

void fun()
{
static int v=0;
int a=5;
v++;
cout<<a<<" "<<v;
}

main()
{
fun(); -- 5, 1
fun(); -- 5, 2
fun(); -- 5, 3
}
```

* In Example 2 v will always remain in the memory during the execution of the program like global variable **BUT IT CAN BE ACCESSED ONLY BY FUNCTION fun. This is called as static variable.**
* The result of the second program will also be the same but now v cannot be accessed by main
  **v is not created each time fun() is called but is created only first time.**

* STATIC Variables are available in C/C++ but not in java

## [10.9] Recursive Function

- Recursive function is nothing but the function calling itself.

```c++
Ex 1:

void fun(int n)
{
if(n>0)
{
cout <<n<<endl;
fun(n-1);
}
}

int main()
{

int x=5;
fun(x);

}
```

- here fun will get executed as far as n>0 hence it will print 5 4 3 2 1

```c++
void fun(int n)
{
if(n>0)
{

fun(n-1);
cout <<n<<endl;

}
}

int main()
{

int x=5;
fun(x);

}
```



* Here fun will print 1 2 3 4 5 to get deeper insights look here =: https://stackoverflow.com/questions/57155715/why-does-this-function-print-1-2-3-4-5-in-ascending-order/57155922#57155922