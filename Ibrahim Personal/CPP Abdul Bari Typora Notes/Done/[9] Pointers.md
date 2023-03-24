# [9] Pointers

## [9.1] Introduction

- Pointers are the variables which is used to store the address of the data:
- Based on this variables are classified into two types:
	1. Data Variables
	2. Address Variables
- Data variable - int x = 10, meaning x is stored in location 200/ 201
- Address variable - int *P; P = &x. This means P is stored in location say 300/301 and
it contains the address of x which is 200/ 201.
- **[Ibrahim] int *P = &x. This also means that P contains the address of a variable whose data type is int**
- 

How to display all these numbers:

- cout << x; Displays 10
- cout << &x --> 200
- cout << p --> 200
- cout << &p --> 300
- cout << *p --> 10: // This will show the data of the address where p is pointing. This is called "Dereferencing".

```c++
#include <iostream>

using namespace std;

int main()
{
    int a=10;
    int *p=&a;

    int A[]={1,2,3,4,5};
    int *q = A; // here we have not written &A because when we write A, &A[0] is automatically assigned to q
    // int *q = &A[3] // this is also allowed as we are storing address of integer at A[3]

    cout << a << endl;
    cout << &a << endl;
    cout << p << endl;
    cout << &p << endl;
    cout << *p << endl;

    q = q+1;
    cout <<"Elements of A: " << *q << endl;

    q = q+3;
    cout <<"Elements of A: " << *q << endl;

    cout <<"Elements of A: " << q[-4] << endl;

    return 0;
}
```



## [9.2] Definition

Declaration - int *p;
Initialization p = &x;
Dereferencing cout << *p

## [9.3] Why Pointers

1. 
- Main programs can directly access code section and stack ONLY but NOT HEAP.
- Directly means it can take address directly go there and take the data.
- But it can access heap memory indirectly. The pointer in stack can have the address
of the data in heap thus allowing the program to access the data in heap.

2. The files in the Disk are accessed using only FILE pointers
3. Network connections are accessed by the program using pointers
4. Keyboard/ Monitors/ Printers are accessed indirectly accessed using pointers.

## [9.2] Pointers - Important Facts

* **LANGUAGES LIKE JAVA AND C# DOES NOT HAVE POINTERS HENCE WE CANNOT ACCESS THESE DEVICES THROUGH THE PROGRAM AT ALL.YOU CAN ACCESS THESE ONLY USING JVM OR COMMON LANGUAGE RUNTIME IN C# OR .NET**
* **Hence System level programming cannot be done using Java or C#. Operating systems and device drivers are thus programmed using C++.**

* **POINTERS OF ANY TYPE TAKES THE SAME SIZE.**

  * int *p;
  * double *q;
  * then sizeof(p) will be equal to sizeof(q)

## [9.4] Heap Memory Access using pointers 

* Heap memory is accessed dynamically. Meaning memory is allocated dynamically.
* **The size of the memory required in the heap is decided at run time not at compile time.**
* Mostly we allocate the arrays in the heap and not just float or int.

**Array created in stack:**

```c++
int A[5] = {1,2,3,4,5}
```

**Array created in heap:**

```c++
int *p; // This creates p in stack which stores the address of array in heap.
p = new int[5];// This new means memory is allocated in heap. whenever you create an array in heap then you need to take its address and assign it to a pointer.
```

* Note that the variable p is stored in stack.
* **IBRAHIM: Note here that pointer *p and array in heap new int[5] should always be of same data type**
* The same thing is written in single line

```c++
int *p = new int[5];
```

## [9.5] Heap Memory De-allocation

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

## [9.6] Accessing array in heap memory

- Similar to regular array the array in heap can be accessed using same syntax P[2] = 15;
- Here note that pointer to an array P is treated the same way as name of an array.

## [9.7] Dynamically changing the size of memory in heap

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

## [9.8] Pointer Arithmetic

```c++
int A[5] = {1,2,3,4,5}

int *p = A; here lets say 1 is stored in mem location 200,201 then p stores 200
```

There are five operations allowed on pointers.

### 1. p++;

- This means that p will now contain address 202 and not 201
- The value of the pointer incremented depends on the datatype of the pointer
- If the datatype is float then the pointer will be incremented by +4
- If it is char the pointer will be incremented by +1.

### 2. p--;

- Same as how p++ works

### 3. p = p + 2;

- if pointer is pointing at 202 then now it will point at 206.

### 4. p = p - 2;

- same as p + 2

### 5. d = q - p; 

* Distance between two pointers or the number of elements between 2 pointers

consider this 

```c++
int A[5] = {1,2,3,4,5}

int *p = A;
int *q = &A[3]
```

* Hence q-p here will give 206-200 = 6 and 6/2 (as datatype is int) = 3. Meaning there are 3 elements between pointers p and q

### 6. d = p-q;

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

## [9.9] Problems with pointers

Problems with the pointer gives runtime errors which can be very dangerous

* Problems with the pointers

1. Uninitialized pointer
2. Memory leak
3. Dangling pointer

### 1. Uninitialized pointer:

int *p; // This pointer is not pointing anywhere hence it will take any garbage address

*p = 25 // Now if we assign a value to the location where pointer is pointing than this data is stored in some unknown garbage location.

There are 3 ways if initializing pointer

(i). Assignment to the address of the existing variable: p = &x

(ii). Assignment to the known address: p = (int *)0x5638 // This is never recommended 

(iii). Assignment to the heap memory: p = new int(5)

After this if we write cout << *p then the data stored at the location where memory is pointing will be available

### 2. Memory Leak

- If we don't de-allocate the memory declared in the heap then we say that memory is leaked in the heap.

```c++
int *p = new int[5];

delete []p;
p = NULL; //we should never do this unless we have remove the memory from heap using the stamement above
```



- we can also write these statements in place of NULL

```c++
p = 0;
p = nullptr; //nullptr is a stored literal in modern C++
```



### 3. Dangling pointers

- Consider the situation where the pointer in the function deletes the memory in the heap 
which the pointer in the main is pointing. hence now the pointer in the main function is pointing to 
undeclared memory location this is called as Dangling pointer

```c++
void main()

int *p = new int[5]; 

func(p);

void func(int *q)

{

delete []q; // here func is deleting the memory using pointer q which was shared by the main memory

}
```



- When the control comes back to main program the pointer p is pointing to the memory which doesn't exists. hence if we try to access it using cout << *p then we will get a runtime error. Here p is now dangling pointer.

**To remove these kinds of error languages like java and .net has removed the pointers and these languages are managed language. Hence JVM will take care of these things like not allowing dangling pointers, removing the memory when not in use.**

## [9.10] Reference

```c++
{

int x=10; // let us say x is stored in memory location 200/ 201
int &y = x; // here y is alias or nickname of the x. you can acess the same memory location using both x and y name

x++; y++; // will both increment the value stored in 200 by 1
cout << x << y << endl; // this both will print the value at 200

}
```

#### 1. R-Value Vs L-Value

```c++
int a;
a = x; // x is called r value, 12 will be stored in a. hence here x is "data", literal, constant value.
x = 25; // here x is called l value. Here we want 25 to be stored in the location (200) where x is pointing. the data at this location (200) gets overwrtitten by 25. So In this case x is "address of x"
```

* **Variable written on right hand side r-value means "DATA"**

* **Variable written on left hand side l-value means "ADDRESS"**

#### 2. Case when L-Value is assigned to the variable on left hand side

``` c++
int &y = x; // here though x is written on right but what is given to the name of y ?. The same address which x is poiting to. 
// This means the x here is l-value of x;
```

#### 3. Reference does not occupy any memory

Here x is occupying 2 bytes of memory (Integer). Then what amount of memory y is occupying ?. Answer is y is not occupying any memory. hence "REFERENCE DOES NOT OCCUPY ANY MEMORY".

#### 4. Reference  name cannot be used for any other variable

Once the Alias or reference y is created. The name "y" cannot be used as a reference for any other variable.
int &y = a; // This cannot be written in the same function at all.

#### 5. Creating alias of a pointer

```c++
int x = 10;
int *y = &x; // y is a pointer to x
int *&z = y; // z is an alias of y. note that how for creating alias pointer we have to add * just like declaring normal pointer
```

## [9.11] Pointer to a function

Syntax is (return type) (name of the pointer, fp is function pointer) (parameters)

### 1. Introductory Example - Calling function by pointer name

```c++
void display()
{
	cout << "Hello";
	}
	
int main()
	{
	display(); // this will simply call the function display Instead of directly calling it by name call it using the pointer to a function
	
	void (*fp) (); // declaration syntax is (return type)(name of the pointer, fp is function pointer) (parameters)
    
// pointer to a function (fp) must be inside the bracket or else it won't be a function.
	
	fp = display; // this will assign the address of the function to this pointer. This is Initialization of a pointer
	
	// Call a function this way using pointer
	(*fp)(); // function call
	
	}
```

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
    void (*fp) (int); // Declaration syntax is (return type)(name of the pointer, fp is function pointer) (parameters)


    // Pointer Initialization
    //fp = &display; // this will assign the address of the function to this pointer.
    fp = display; // This is allowed too

    // Function call
    //(*fp)(2);
    fp(2); // This is allowed too

    return 0;
}

```

### 2. Function Overriding example to achieve runtime polymorphism

``` c++
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

* **In function overriding internally function pointers are used for achieving runtime polymorphism**
* **function pointer can point to any function having same signature.**

