# [5] Skeleton of a Program, Primitive Data Types & Operators and Assignments

## [5.1] Skeleton of a Program

### [5.1.1] Hello World

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

### [5.1.2] Add two numbers - Explain taking in two numbers

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

### [5.1.3] Getline - Input a string

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

## [5.2] Primitive Data Types

### [5.2.1] Int Data Types

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[1] Int.PNG)

### [5.2.2] Char Data Types

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[2] Char.PNG)

### [5.2.3] Modifiers

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[3] Modifiers.PNG)

### [5.2.4] Variables

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[5] Primitive Data Types\[4]Variables.PNG)

## [5.3] Operators and Assignments

### [5.3.1] Operators and Expressions

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[1] Operators.PNG)

### [5.3.2] Type Casting

**Notice in this figure that Modulo Operator % is allowed on int and char but not float **



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[2] Type Casting, Mod is allowed on int and char but not float.PNG)



### [5.3.3] Operators Precedence

**Notice the header file #include<cmath> or <math.h> to be included for using the functions like sqrt() and pow() **

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[3] Operator Precedences, function for sqrt, pow, include cmath.PNG)



### [5.3.4] Compound Assignment

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[4] Compund Assignment.PNG)



### [5.3.5] Pre-Post Increment Operator

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[5] Pre-Post Increment Operator.PNG)


### [5.3.6] Multiple Increment Operator not allowed in a single line

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[6] Multiple Increment Operator is not allowed in a single line.PNG)

### [5.3.7] Overflow and Underflow condition

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[7] Overflow.PNG)



### [5.3.8] Program to demonstrate Overflow

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

### [5.3.9] Bitwise Operator

**Notice the NOT of 5 is -6**



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[9] Bitwise Operator, NOT of 5 is -6.PNG)



### [5.3.10] Left shift by one position is multiply by 2 and right shift by one position is divide by 2

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[6] Operators and Assignments\[10] Bitwise Operator, left shift multiply.PNG)



### [5.3.11]  Enum and Type Def

#### 1) Enum: 

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

* In C++, an `enum` is a user-defined data type that consists of a set of named constants, or "enumerators". Each enumerator is assigned an integer value, which can be used to represent the constant in the code. The `enum` keyword is used to define an enumeration type.
* Here's an example of how to define and use an `enum` in C++:

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

#### 2) TypeDef:



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

* Here if we forgot what are m1, m2, etc we can know from the typedef
  that it is marks datatype with int datatype.

