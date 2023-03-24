# [11] Object Oriented Programming

## [11.1] Introduction

**What are objects ?**

- Lets say government has different departments like banks, electricity, water, transportation, etc.
- Now each departments like banks may have its own functions like open account, check balance, deposit, etc
- These individual departments are known as OBJECTS.
- These objects contains functions as well as data related to that functions.

## [11.2] Principles of OOP

1. Abstraction - hiding the details of functions

2. Encapsulation - hiding the details of data as well as function
	
	- Data hiding
	
3. Inheritance

4. Polymorphism

   

### 1. Abstraction

- Through the process of abstraction, a programmer hides all but the relevant data about an object in 
order to reduce complexity and increase efficiency.
- In Programs we just want to know the name of the function and not the details inside it. This is called 
  abstraction.

### 2. Encapsulation

- In OOP using C++ we achieve the abstraction using class. class contains DATA and FUNCTIONS. This is called Encapsulation.

- In C++ functions are grouped together using class.

**Precise difference between abstraction and Encapsulation.**

* Encapsulation is the packing of data and functions operating on that data into a single component and restricting the access to some of the object's components. Encapsulation means that the internal representation of an object is generally hidden from view outside of the object's definition.

* Abstraction is a mechanism which represent the essential features without including implementation details.

Encapsulation:-- Information hiding.
Abstraction:-- Implementation hiding.

```c++
Class My
{

private:
Data

public:
function()
   
}
```

### 3. Inheritance

- Borrowing the feature in the derived class from the base class.

### 4. Polymorphism

- The word polymorphism means having many forms. In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form.

- Eg if you know to drive a car you can drive any car.

## [11.3] Class Vs Object

- Class is determined by Classification. Class share specific common properties.
- Eg. Car is class. Camry, Civic are the objects.
- **Class is a definition. Object is an instance.**
- **Design of a room (blueprint) is a class and the actual rooms made with the help of that class are objects.**
- Design of a chip is class while actual chips made out of it are objects.

- Class in programming consists of two things data and functions.
- Data is called as properties and function is called behavior

```c++
Class Rectangle
{

	float lenght; // data
	float breadth; // data
	
	float area(); // function
	float perimeter(); // function
	float diagonal(); // function
	};
```

* Now objects of the classes are say r1, r2, r3, etc

- These objects will have all the functions like area

## [11.4] Class Object Syntax

* Let us define class rectangle.

```c++
Class Rectangle
{

int length; // attributes
int breadth;

int area()
{
return length * breadth;
}

int perimeter()
{
return (2*length + 2*breadth)
}

}; // here semicolon is mandatory.

// Now how to use the class

int main()
{
//rectangle r1, r2; // here r1 and r2 are objects.
// Note here that objects can also be created like this:     
    rectangle (r1);
    rectangle (r2);
}

// r1 and r2 are datatypes/ variables of class rectangle
// r1 and r2 will occupy memory in the stack
// so now r1 and r2 will take 4 bytes of memory in stack
// 2 bytes for length and 2 bytes for breadth
// class and function won't take any memory in stack.

// assigning values to the attributes of the objects

int main()
{
rectangle r1, r2; 

r1.length = 10;
r1.breadth = 5;
// Now we can calculate area and other functions.
cout << r1.area();
r2.length = 15;
r2.breadth = 10;
cout << r2.area();
}

// These length and breadth cannot be accessed by user because by default it becomes PRIVATE.

// Hence we have to go back to the class and define everything explicitly as PUBLIC.


Class Rectangle
{
public:

int length; // attributes
int breadth;

int area()
{
return length * breadth;
}

int perimeter()
{
return (2*length + 2*breadth)
}

};
```

**Notice that function of class will be in memory but not variables.**

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[12] Object Oriented Programming\[5] Notice that functions of the class will be in memory but not variables.PNG)

## [11.5] Pointer to an Object

### 1. Creating Pointer in Stack

```c++
#include <iostream>

using namespace std;

class Rectangle
{
    public:
    int length;
    int breadth;
    int area()
    {
        return length*breadth;
    }
    int perimeter()
    {
        return 2*(length+breadth);
    }
};

int main()
{

Rectangle r;
Rectangle *p;
p=&r;
r.length=10; // . operator is used for accessing the members of an object using object name
p->length=10; // -> operator is used for accessing the members of an object using pointer for an object.

p->breadth=5;
cout << p->area();	

}
```

### 2. Creating Objects in Heap using Pointer 

```c++
#include <iostream>

using namespace std;

class Rectangle
{
    public:
    int length;
    int breadth;
    
    int area()
    {
        return length*breadth;
    }
    
    int perimeter()
    {
        return 2*(length+breadth);
    }
};

void main()
{
Rectangle *p;
p = new Rectangle; // This rectangle is defined in heap and p which is stored in stack is pointing to it.

Rectangle *q = new Rectangle(); // writing it in a single line

p->length = 15;
p->breadth = 10;
cout << p->area();
```

```c++
Rectangle r; // Object created in stack
Rectangle *p = new rectangle(); // object created in heap

//Pointer assignment for object in heap because objects in heap can only be accessed using pointers(in stack)
```

* **IN JAVA OBJECTS ARE ONLY CREATED IN HEAP AND NOT IN STACK ALSO, LIKE C++**

## [11.6] Data Hiding

```c++
class Rectangle
{
    public:
    int length;
    int breadth;
    int area()
    {
        return length*breadth;
    }
    int perimeter()
    {
        return 2*(length+breadth);
    }
};
```

- Note that in this class we have made the data as public.
- This is a problem if the users mishandles the data.
- What if user gives length as -ve then the area will be -ve.
- This is called Data Mishandling and hence data hiding becomes crucial.
- hence we have to make the data as PRIVATE. Also note that by default it is private even if you don't mention anything.

consider this :

```c++
class Rectangle
{
    private:
    int length;
    int breadth;
	
	public:
    int area()
    {
        return length*breadth;
    }
    int perimeter()
    {
        return 2*(length+breadth);
    }
};
 
```

But now we can not write and even read the variables like this:

```c++
r.length = 10;
cout<<r.length;
```

- Hence now we have to write functions to read and write data as functions are public

```c++
class Rectangle
{
private:
    int length;
    int breadth;
	
public:
	void setLength(int l) { 
        length = l;}
	
	void setBreadth(int b) { 
        breadth = b;}
	
	int getLength()
	{
	if(l>=0) 
    	length=l;
	else 
		cout << "length cannot be -ve, default =0";
		length=0; // Making default length to 0
	return length;
	}
	
	int getBreadth()
	{
	if(b>=0)
		breadth=b;
	else
		cout << "breadth cannot be -ve, default =0";
		breadth=0; // Making default length to 0
	return breadth;
	}
	
	
    int area()
    { return length*breadth;}
	
    int perimeter()
    { return 2*(length+breadth);}
    
};
```

- Hence Now we have to call these functions to set length and breadth

```c++
void main()
{

rectangle r;
r.setLength(10);
r.setBreadth(-5);
cout<<r.area(); // hence now the area will be 0

cout << "length is" << r.getLength();
}
```

### **Property Functions**

- getXXX functions reads the value
- setXXX functions writes the value

- getXXX are called **Accessors**
- setXXX are called **Mutators**

- Also notice that the area and perimeter provides some facilities to the user hence
they are called **FACILITATORS**

## [11.7] Constructors

In this example:

```c++
int main()
{

rectangle r;
r.setLength(10);
r.setBreadth(-5);
cout<<r.area() << endl; // hence now the area will be 0

cout << "length is " << r.getLength() << endl;

    return 0;
}
```

- Notice that we have set the length and breadth of the rectangle using mutators and accessors but philosophically this is wrong.
- Consider that if you purchase a car then you should be able to order a car with some default color. In the same way when you create an object then you should be  able to set properties of the object while creating it only using some statement like this: `rectangle r (length, breadth).`
- This is done with the help of constructors.
- Now when we declare an object `rectangle r;`
- Then the object is created in stack. Who created this object ?. Some function created this object. 
  This function is provided by the compiler not visible to the user but present in the machine code and
  this constructor will create an object. Hence EVERY CLASS WILL HAVE SOME CONTRUCTOR. This is called as Default Constructor.

User can also write their own constructor. If we don't write any compiler will provide its default constructor.

### Types of Constructor

1. Default Constructor - Also called built-in constructor
2. Non-Parameterized Constructor - This is also called default sometime
3. Parameterized Constructor
4. Copy Constructor

```c++
#include <iostream>

using namespace std;

class Rectangle
{
private:
    int length;
    int breadth;
	
public:
	Rectangle () // Non-Parameterized
	{
        length = 0;
        breadth = 0;
	}
	
	Rectangle (int l, int b) // Parameterized
	{
        length = l;
        breadth = b;
	}
	
	Rectangle (Rectangle& rect)  // COPY CONSTRUCTOR  - same name as class should be given
	{
        length = rect.length;
        breadth = rect.breadth;
	}
	
};

int main() {
    Rectangle r1; // built-in
    Rectangle r2(); // non-parameterized
    Rectangle r3(10,5); // parameterized
    Rectangle copied_r(r3); // copy contructor

}
```

* Note that all the constructor have same name but different parameters. Hence this is nothing but **CONSTRUCTOR OVER-LOADING.**
* Hence we can avoid the non - parameterized constructor by giving default arguments to parameterized constructor

```C++
	rectangle() // Non-Parameterized
	{
	length=0;
	breadth=0;
	}
	
	rectangle(int l, int b); // Parameterized
	{
	setLength(l);
	setBreadth(b);
	}
```

- Is equivalent to:

```c++
	rectangle(int l=0, int b=0); // Parameterized
	{
	setLength(l);
	setBreadth(b);
	}
```

### Deep Copy Constructor

Shallow Constructors are the ones which only copy the values. In Contrast Deep Copy constructors are the 
constructors which not only copies the values but also allocates the same memory.

```c++
#include <iostream>

using namespace std;
class Test
{
public:
    int a;
    int *p;

    Test (int x)
    {
        a = x;
        p = new int[a];
    }

    Test (Test &t)
    {
        a = t.a;
        p = t.p;
    }

};

int main()
{   
    Test t(5);
    Test t2(t); 
    return 0;
}
```

* Over here the copy constructor will create a variable a = 5 just like original constructor however the pointer created by this copy constructor will also point to the same array of size 5 which was created by the original constructor.

* This is completely wrong and hence DEEP COPY CONTRUCTORS are used which takes care of such issues. **Meaning the copy constructor will create a new array in the heap and its pointer will point to that new array**

* For this we have to write code to create new array in the heap in the copy constructor 

```c++
Test (Test &t)
{
	a = t.a;
	p = new int[a]; // now this will point to a new array created in heap
	}
```

**If you are careful about these things then your constructor is a deep copy constructor.**

## [11.8] Scope Resolution Operator

There are two methods of writing functions inside the class. These functions are called member functions.

```c++
class rectangle
{

public:    
    int length;
    int breadth;

    int area() // This is one way of writing the function inside the class
    {
        return length*breadth;
    }

    int perimeter(); // This is another way where you just write the function name inside the class

};


int rectangle :: perimeter() // return type nameoftheclass :: nameOfFunction
    {
        return 2*(length+breadth);
    }


int main()
{

    rectangle r;
    r.length = 5;
    r.breadth = 10;
    cout << r.area() << endl;
    cout << r.perimeter() << endl;
    return 0;
}
```

### **Difference between two methods of writing member functions**

* When the function is written inside the class then in the machine code that function is created inside 
the main function where it is called. Such kind of functions are called as INLINE Functions. Eg. area() function above.
* When the function is written outside the class (like the perimeter function here) using 
the SCOPE RESOLUTION OPERATOR then the machine code for the function will be SEPARATELY GENERATED. When these functions are called in the main function then it will go to these functions and return to main after the functions has been executed.
* **IT IS A GOOD PRACTICE IN C++ TO WRITE THE FUNCTION OUTSIDE THE CLASS**

## [11.9] All Methods

```c++
#include <iostream>

using namespace std;

class rectangle
{
private:

    int length;
    int breadth;

public:

    rectangle(); // constructor
    rectangle(int l, int b);
    rectangle(rectangle &r);
    int getLength() {return length;} // Accessors
    int getBreadth() {return breadth;}
    void setLength(int l); // Mutators
    void setBreadth(int b);
    int area(); // Facilitators
    int perimeter();
    bool isSquare(); // Inspector
    ~rectangle(); // Deallocation of an object // Destructor

};

    rectangle::rectangle() {
        length=1;
        breadth=1;
    }

    rectangle::rectangle(int l, int b) {
        setLength(l);
        setBreadth(b);
    }

    rectangle::rectangle(rectangle &r) {
        length = r.length;
        breadth = r.breadth;
    }

    void rectangle::setLength(int l) {
        length = l;
    }

    void rectangle::setBreadth(int b) {
        breadth = b;
    }

    int rectangle::area() {
        return length*breadth;
    }

    int rectangle::perimeter(){
        return 2*(length+breadth);
    }

    bool rectangle::isSquare(){
        return length == breadth;
    }

    rectangle::~rectangle(){
        cout << "Rectangle Destroyed";
    }

int main()
{
    rectangle r1 (10, 10);
    cout <<"Area "<< r1.area() << endl;

    if(r1.isSquare())
        cout<<"Yes"<<endl;

    return 0;
}
```

## [11.10] Inline Functions

We already know that the inline functions are copied inside the main functions where they are called.

Hence now there are two methods of writing inline functions.

1. write the function within the class itself.
2. write the suffix "inline" before the function name inside the class and then define the class outside 
   exactly similar to non-inline functions.

```c++
class test
{
public:
    void fun1(){
    	cout << "Inline function Inside the class" << endl;
    }

	inline void fun2();
};

void test::fun2(){
	cout << "Inline function Outside the class" << endl;
}

int main() {
    test t;
    t.fun1();
    t.fun2();
    return 0;
}
```

## [11.11] This pointer

* In the cases when the parameter passed to the constructor of the class has same name to that of the data member of the class. The compiler gets confused because of the same name. 
* In this case the length of the class will get assigned to the length of the class and the length of the object (parameter passed) will not be accessed at all.
* This pointer is used to indicate the members of the class.

```c++
#include <iostream>

using namespace std;

class rectangle
{
private:
    int length, breadth;

public:

    rectangle (int length, int breadth)
    {
        // length = length; // Here note that if we assign length argument to the length of the current object
        // then the compiler will get confused because of the same name. hence here the local member length will get assigned to
        // itself and will never access the length of the object. To refer to the data member of the same class
        // or same object this pointer is used. This pointer removes the name ambiguity.

        this->length = length; // this->length refers to data member of the class of the current object
        this->breadth = breadth; // this means r1's length and breadth
    }

    int area() {
        return length*breadth;
    }

};

int main()
{

    rectangle r1 (10, 10);
    cout <<"Area "<< r1.area() << endl;
    return 0;
}
```

## [11.12] Struct vs Class

* In `struct` by default everything is PUBLIC while in class by default everything is PRIVATE.
* In C the `struct` can only have data while in C++ the `struct` can have class as well as data.
- In C++ the `struct` looks exactly similar to class

```c++
#include <iostream>

using namespace std;

struct Demo
{
    int x, y;

    void Display() {
        cout << x <<" "<< y << endl;
    }
};


int main()
{
    Demo D;
    D.x = 10;
    D.y = 15;
    D.Display();
    return 0;
}

```

