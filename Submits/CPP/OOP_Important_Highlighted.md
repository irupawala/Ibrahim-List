 # Principles of Object Oriented Programming 

Object-oriented programming (OOP) is a programming paradigm that focuses on organizing code into objects that can interact with each other. C++ is a programming language that supports OOP features such as encapsulation, inheritance, and polymorphism.

Here are some key concepts of OOP in C++:

1. **Classes**: Classes are user-defined data types that encapsulate data and behavior. They can have data members (variables) and member functions (methods) that manipulate the data.
2. **Encapsulation**: Encapsulation is the principle of hiding the implementation details of a class and exposing only the necessary interface to the outside world. This protects the internal data from unintended modifications.
3. **Inheritance**: Inheritance is a mechanism that allows a class to inherit properties from another class. The derived class inherits the data and behavior of the base class and can also override or extend it.
4. **Polymorphism**: Polymorphism is the ability of objects to take on different forms or behaviors depending on the context. C++ supports two types of polymorphism: compile-time (static) polymorphism, which is achieved through function overloading and templates, and runtime (dynamic) polymorphism, which is achieved through virtual functions and inheritance.

## Class Vs Object

* Class is a Clarification. Class is Definition
* Object is an instance. 
* Examples:
  * Car is class. Camry, Civic are the objects.
  * Design of a room (blueprint) is a class and the actual rooms made with the help of that class are objects.
  * Design of a chip is class while actual chips made out of it are objects.
* Class can have data members/attributes (variables) and member functions (methods) that manipulate the data. Data members is called as properties and member function is called behavior.
* All the data members and member functions by default are declared as `PRIVATE` in C++ and cannot be accessed outside class definition hence we have to explicitly declare then as `PUBLIC`.

Example of a simple class

```c++
#include <iostream>

using namespace std;

class Rectangle {
public: // Attributes cannot be accessed by user because by default it is PRIVATE, hence we have to explicity define them as PUBLIC
    int length; // attributes
    int breadth;

    int area()
        {
            return length * breadth;
        }

    int perimeter()
        {
            return (2*length + 2*breadth);
        }

    }; // here semicolon is mandatory.


int main() {
    Rectangle r1, r2; 
    r1.length = 10;
    r1.breadth = 5;
    // Now we can calculate area and other functions.
    cout << r1.area() << endl;
    cout << r1.perimeter() << endl;
}
```

## Class & Object Storage Location

* The class definition itself is stored in the **program's executable code** or in a shared library if the class is defined in a separate source file. When the program is compiled, the class definition is translated into machine code and stored in memory along with the rest of the program.

In C++, **objects of a class are stored in the memory allocated from the runtime stack or heap** depending on how they are created.

If an object is created as a local variable inside a function, it will be stored on the stack. When the function exits, the memory allocated for the object is automatically freed. For example:

```c++
void someFunction() {
    Person john;
    // ...
}
```

Here, the object `john` of type `Person` is created as a local variable inside the function `someFunction()` and is stored on the stack.

If an object is created with the `new` operator, it will be stored on the heap. Memory for the object is allocated dynamically and must be explicitly deallocated using the `delete` operator when it is no longer needed. For example:

```c++
void someFunction() {
    Person* john = new Person();
    // ...
    delete john;
}
```

# Pointer to an Object

## Creating Pointer in a stack

```c++
#include <iostream>

using namespace std;

class Rectangle
{
public:
    int length, breadth;
    int area()
    {
        return length*breadth;
    }

};

int main()
{

Rectangle r;
Rectangle *p = &r;

// . operator is used for accessing the members of an object using object name
r.length = 10; 
r.breadth = 5; 
cout << "Accessing the object using object name = " << r.area() << endl;	

p->length = 10; // -> operator is used for accessing  members of an object using pointer 
p->breadth = 5;
cout << "Accessing the object using pointer(objects address) = " << p->area() << endl;	

}
```

## Creating Objects in Heap using Pointer

```c++
#include <iostream>

using namespace std;

class Rectangle
{
public:
    int length, breadth;
    int area()
    {
        return length*breadth;
    }

};

int main() {
    
    Rectangle *p = new Rectangle; // This rectangle is defined in heap and p which is stored in stack is pointing to it.
    //Rectangle *p = new Rectangle(); // allowed as well

    p->length = 10; // -> operator is used for accessing members of object using pointer 
    p->breadth = 5;
    cout << p->area() << endl;	

}
```

```c++
Rectangle r; // Object created in stack
Rectangle *p = new rectangle(); // object created in heap

//Pointer assignment for object in heap because objects in heap can only be accessed using pointers(in stack)
```

# Encapsulation

Encapsulation is one of the fundamental concepts of object-oriented programming (OOP) that helps in achieving data abstraction and information hiding. It refers to the bundling of data members and member functions (methods) into a single unit called a class, and restricting access to the data from outside the class.

## Access Specifiers

In C++, encapsulation can be achieved through the use of access specifiers, which are keywords that define the scope and visibility of class members. There are three access specifiers in C++:

1. Private: Accessible only inside a class
2. Protected: Accessible inside a class and inside derived classes
3. Public: Accessible inside class, inside derived class and upon object

- Derived class can access the protected and public but not private
- Base class can access all its members private, protected and public

```C++
#include <iostream>
using namespace std;

class Base
{
private: 
    int a;
protected: 
    int b;
public: 
    int c;

    void funBase() {
        a=10; // private member not accessible by derived class/object but only in base class
        b=20;
        c=30;
    }
};

class Derived: Base{
public:
	funDerived() {
        // a=1; 
        b=2; // protected member accessible by derived class
        c=3;
	}
};

int main() {
	Base x;
	x.c = 90; //a (private) and b (protected) CANNOT be accessed but public object c CAN be accessed on object upon class
}
```

## Property Functions (Data Hiding)

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
};
```

- Note that in this class we have made the data as public. This is a problem if the users mishandles the data. What if user gives length as -ve then the area will be -ve. This is called Data Mishandling and hence data hiding becomes crucial. Hence we have to make the data as PRIVATE. Also note that by default it is private even if you don't mention anything.

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
};
 
```

But now we can not write and even read the variables like this:

```c++
r.length = 10;
cout << r.length;
```

Hence now we have to write functions to read and write data as functions are public

```c++
#include <iostream>

using namespace std;

class Rectangle
{
private:
    int length;
    int breadth;
	
public:
	void setLength(int l) { // Mutators (Setters)
        if (l >= 0) {
            length = l;
        }
        else {
            cout << "length cannot be -ve, default = 0" << endl;
            length = 0; // Making default length to 0           
        }
        }
	
	void setBreadth(int b) { // Mutators (Setters)
        if (b >= 0) {
            breadth = b;
        }
        else {
            cout << "breadth cannot be -ve, default = 0" << endl;
            breadth = 0; // Making default length to 0           
        }
        }
	
	int getLength () const // Accessors (Getters)
    // int getLength () // This is allowed too
        {
            return length;
        }
	
	int getBreadth() const // Accessors (Getters)
    // int getBreadth() // This is allowed too
	{
        return breadth;
	}
	
    int area() { // Facilitators
        return length*breadth;
        }	
};

int main() {
    Rectangle r;
    r.setLength(10);
    r.setBreadth(-5);
    cout << r.area() << endl; // hence now the area will be 0

    cout << "length is " << r.getLength() << endl;

}
```

- Hence Now we have to call these functions to set length and breadth

```c++
int main() {
    Rectangle r;
    r.setLength(10);
    r.setBreadth(-5);
    cout << r.area() << endl; // hence now the area will be 0
    cout << "length is " << r.getLength() << endl;

}
```

In C++, property functions are a way to provide controlled access to private member variables of a class. They are also known as getter and setter functions, which allow you to get or set the value of a private member variable through public member functions.

1. **Accessors (Getters) getXXX:** Accessors are member functions of a class that allow us to retrieve the value of a private or protected data member. They are typically declared with the `const` qualifier to indicate that they do not modify the state of the object. Accessors are commonly named with the prefix `get` followed by the name of the data member they retrieve.
2. **Mutators (Setters) setXXX:** Mutators are member functions of a class that allow us to modify the value of a private or protected data member. They are commonly named with the prefix `set` followed by the name of the data member they modify. Mutators can be used to enforce constraints or validation rules on the input data before modifying the object's state.
3. **Facilitators:** Facilitators are member functions of a class that do not directly access or modify the state of an object but provide some useful functionality related to the object. Facilitators can be used to perform calculations, comparisons, or other operations on the object's data. 

# Constructors

- Now when we declare an object `rectangle r;` Then the object is created in stack. Who created this object ?. Some function created this object. This function is provided by the compiler not visible to the user but present in the machine code and this constructor will create an object. Hence EVERY CLASS WILL HAVE SOME CONTRUCTOR. This is called as Default Constructor.
- Constructors are special member functions in C++ that are used to initialize the objects of a class. They are called automatically when an object is created and are used to set the initial values of the object's member variables.
- **In C++, constructors have same name as class and do not have a return type, not even void.**
- Types of Constructors:
  - Default Constructor - Also called built-in constructor
  - Non-Parameterized Constructor - This is also called default sometime
  - Parameterized Constructor
  - Copy Constructor

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
    // Rectangle (const & rect)  // advisable to define like this
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

* Note that all the constructor have same name but different parameters. Hence this is nothing but CONSTRUCTOR OVER-LOADING.

# Scope Resolution Operator

There are two methods of writing functions inside the class. 

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

**Difference between two methods of writing member functions**

- When the function is written inside the class then in the machine code that function is created inside 
  the main function where it is called. Such kind of functions are called as INLINE Functions. Eg. area() function above.
- When the function is written outside the class (like the perimeter function here) using 
  the SCOPE RESOLUTION OPERATOR then the machine code for the function will be SEPARATELY GENERATED. When these functions are called in the main function then it will go to these functions and return to main after the functions has been executed.
- **IT IS A GOOD PRACTICE IN C++ TO WRITE THE FUNCTION OUTSIDE THE CLASS**

# Complete Example - Constructor, Destructors and Property Functions

```c++
#include <iostream>

using namespace std;

class rectangle
{
private:
    int length, breadth;
    
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

# Inheritance

* Inheritance is deriving the class from the existing pre-defined class. It is a process of acquiring features of an existing class into a new class. It is used for achieving reusability.
* Features of base class will be available in derived class.

```c++
#include <iostream>

using namespace std;
class base
{
public:
    int x;
    void Display();
};

void base::Display() {
    cout << "Display of base " << x << endl;
    }

class derived:public base
{
public:
    int y;
    void Show() {
        cout << "Display of Derived " << y << endl;
    }
};

int main()
{
     //class base b1;
     class derived d1;
     d1.x = 100;
     d1.y = 50;
     d1.Display();
     d1.Show();
    return 0;
}
```

## Constructor in Inheritance

- Notice that whenever the derived class is called constructor of default class is called first.
- When the derived class is called it will CALL the base class and the base class will be EXECUTED FIRST and then derived class will be EXECUTED.
- CALLING HAPPENDS FROM BASE TO DERIVE BUT EXECUTION HAPPENDS FROM DERIVED TO BASE.

```c++
#include <iostream>

using namespace std;
class Base
{
public:
    Base(){
        cout << "Default of base " << endl; }

    Base(int x){
        cout << "Param of base " << x << endl; }
};

class Derived : public Base
{
public:
    Derived(){
        cout << "Default of Derived" << endl; }

    Derived(int a){
        cout << "Param of Derived " << a << endl; }

    Derived (int x, int a): Base(x) {
        cout << "Param of Derived " << a << endl; }
};

int main() {
    // Derived d;  // calling default constructor of base class from the default constructor of derived class
    // Derived d(10); // calling default constructor of base class from the parameterized constructor of derived class
    Derived d(20, 10); // // calling parameterized constructor of base class from the parameterized constructor of derived class
    return 0;
}
```

- Notice how the parameterized constructor of the base class is called from the derived `class Derived (int x, int a): Base(x)`

**Constructor in Inheritance Example**

```c++
#include <iostream>

using namespace std;

class rectangle
{
private:
    int length, breadth;

public:
    rectangle(); // constructor
    rectangle(int l, int b); // constructor
    int getLength() {return length;} // Accessors
    int getBreadth() {return breadth;} // Accessors
    void setBreadth(int b), setLength(int l) ; // Mutators
    ~rectangle(); // Deallocation of an object // Destructor
    int area(); // Facilitators
    bool isSquare(); // Inspector

}; // rectangle class ends here

    rectangle::rectangle() { // constructor
        cout << "Default Constructor" << endl;
        length=1; 
        breadth=1;
    }

    rectangle::rectangle(int l, int b) { // constructor 
        cout << "Param Default Constructor" << endl;
        setLength(l);
        setBreadth(b);
    }
    void rectangle::setLength(int l) { length = l;} // Mutators
    void rectangle::setBreadth(int b) { breadth = b;} // Mutators
    int rectangle::area() { return (length*breadth); } // Facilitators
    bool rectangle::isSquare() { return length == breadth; } // Inspector        
    rectangle::~rectangle() { cout << "Rectangle Destroyed"; } // Destructor


class cuboid: public rectangle
{
private:
    int height;

public:
    int getHeight() {return height;} // Accessors
    int setHeight(int h) {height = h;} // Mutators
    int volume () { return getLength() * getBreadth() * height; } // Facilitators
    /*
    cuboid (int l=0, int b=0, int h=0) { // constructor
        cout << "Derived Constructor calling default base class " << endl;
        setLength(l);
        setBreadth(b);
        height = h;
    } */
    
    cuboid (int l=0, int b=0, int h=0) : rectangle(l,b) { // constructor 
        cout << "Derived Constructor calling parameterized base class" << endl;
        height = h;
    }     

};

int main()
{
    cuboid c(10, 5, 3);
    // c.setLength(2);
    // c.setBreadth(2);
    cout << "Volume " << c.volume() << endl;
    return 0;
}
```

## IsA and HasA

- Here cuboid is Inherited from rectangle hence cuboid **IsA** Rectangle
- Here Table is having object of rectangle class. Hence table class **HasA** Rectangle
- There are two ways a class can be used:
  - Class can be derived: IsA
  - Object of a class can be used: HasA

## Types of Inheritance

Types of Inheritance:

1. Simple/ Single Inheritance
2. Hierarchical Inheritance
3. Multi-Level Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance - Mixture of two inheritance

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[14] Inheritence\[5] Types and Ways of Inheritence\[2] Types of Inheritence.PNG)

**Multipath Inheritance**

- The features of base class A will be available in D via B and C. Here the ambiguity is that the function D should get features of A via B or C ??
- To remove this ambiguity virtual base class is used. If we write VIRTUAL for class B and D then there will be no ambiguity.

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[14] Inheritence\[5] Types and Ways of Inheritence\[3] Virtual Base class.PNG)

In C++, a virtual base class is a base class that is declared as virtual in a derived class. When a base class is declared as virtual, it means that only one instance of the base class is shared among all the derived classes. This can be useful in situations where a class is inherited multiple times through a hierarchy of classes, which can result in multiple copies of the base class being created, leading to issues such as ambiguity and excessive memory usage.

To declare a virtual base class in C++, the base class should be preceded with the keyword `virtual` in the derived class definition. For Example:

```c++
class Base {
  // Base class definition
};

class Derived1 : virtual public Base {
  // Derived1 class definition
};

class Derived2 : virtual public Base {
  // Derived2 class definition
};

class FinalDerived : public Derived1, public Derived2 {
  // FinalDerived class definition
};

```

In the above example, `Derived1` and `Derived2` are both virtual base classes of `FinalDerived`. This means that only one instance of `Base` will be created and shared among `FinalDerived`, `Derived1`, and `Derived2`. This helps to prevent issues such as ambiguity and excessive memory usage that can arise when multiple instances of the same base class are created.

## Ways of Inheritance

A class can be inherited in flowing ways :

Publicly - All members of base will have same accessibility in derived class except private
Protectedly - All members of base will become protected in derived class 
Privately - All members of base will become private in derived class

Public Inheritance: 

- Public and protected members of the base class will become public for the child.
- Child will be able to access public and protected of the Base.
- Grandchild will be able to access public and protected of the child.
- Object will only be able to access public and not protected of the child.

Protected Inheritance:

- Public and protected members of the base class will become protected for the child.
- Child will be able to access public and protected of the Base.
- Grandchild will be able to access public and protected of the Child.
- Object will NOT be able to access public as well as protected of the child.

Private Inheritance:

- Public and protected members of the base class will become private for the child.
- Child will be able to access public and protected of the Base.
- Grandchild will NOT be able to access public as well as protected of the child.
- Object will NOT be able to access public as well as protected of the child.

```c++
class Parent
{
    private: int a;
    protected: int b;
    public: int c;

     void funParent()
     {
        a=10;
        b=5;
        c=15;
     }
};

class Child: private Parent
{
     void funChild()
     {
        //a=10;
        b=5;
        c=15;
     }
};

class GrandChild : public Child
{
public:
    void funGrandChild()
     {
     //a=10;
     //b=5;
     //c=20;
     }
};
```

# Polymorphism

Polymorphism is one of the key features of object-oriented programming (OOP) and it allows objects of different classes to be treated as if they were of the same class, providing a flexible and extensible code design.

In C++, polymorphism is achieved through two mechanisms: 

1. function overloading 
2. virtual functions.

Function overloading allows multiple functions to have the same name but with different parameters. This allows the programmer to call a function by the same name with different arguments, and the appropriate function is chosen based on the arguments passed.

Virtual functions, on the other hand, allow a function in a base class to be overridden in a derived class. When a virtual function is called through a pointer or reference to a base class object, the actual function that is called is determined at runtime based on the type of the object.

To enable polymorphism using virtual functions, the base class must have at least one virtual function, and the derived classes must override this function using the same signature. Additionally, the base class must be declared as a pointer or reference type, and the derived class objects must be instantiated and assigned to the base class pointer or reference.

## Base Class Pointer on Derived Class Object

```c++
#include <iostream>
using namespace std;

class Base
{
public:
	void baseFunction() {
        cout << "This is base class function" << endl;
    }
};


class Derived: public Base
{
public:
    void derivedFunction() {
        cout << "This is derived class function" << endl;
    }
};


int main(){
    Base* Ptr; // Base class pointer
    Ptr = new Derived(); // Derived class object
    Ptr->baseFunction();
}
```

```c++
Base *Ptr;
Ptr = new Derived(); // note that here base class pointer is poiting on derived class object. Also note that here the Derived class is in a heap.
```

- As we know for the derived object we can call the functions of the derived class as well as base class.

- But the question is when using pointers whose functions will be called base or derived class ?. Pointer is of base class but object is of derived class ?
  Answer: BASE CLASS FUNCTION WILL BE CALLED.

- But then can we call the `derivedFunction)()` of the derived class ?. 

  Answer is NO. Hence we can only call the functions of the base class and not the functions of the derived class though the object is derived class BECAUSE THE POINTER IS OF BASE CLASS.


* **Notice also that it does not make any sense to have base class object and derived class pointer**
## Function Overloading and Overriding 

```c++
#include <iostream>
using namespace std;

class Base
{
public:
    void display() {
        cout << "Display of Base" << endl;
    }
};

class Derived: public Base // Function Overriding
{
public:
    void display() { // By giving the same name to the function you have overrided the function display.
        cout << "Display of Derived" << endl;
    }
};

class Derived_Parameteized : public Base // Function Overloading
{
public:
    void display(int x) { // By giving the same name but different parameters, we have created a new function which is Overloading of the previous one.
        cout << "Display of Parameterized Derived" << endl;
    }
};

int main()
{
    Derived d;
    Derived_Parameteized dp;
    d.display(); // Calling the overrided display of derived class
    d.Base::display(); // Calling the display of base
    dp.display(10); // Calling the overloaded function
    return 0;
}
```

## Virtual Function

- Here note that when we call a overridden function of the derived class using the pointer of the base class then the functions of the BASE CLASS IS CALLED.
- If we take real world example then let us say we have derived class advanced car which is pointed by the pointer of the base class basic car. But the object here is actually advanced car hence will it run as a basic car or advanced car ?. it will run like advanced car though we are calling it a basic car.
- Hence Similarly in the programming if the function is present in the base class as well as derived class then the function of the DERIVED CLASS MUST BE CALLED that is the function should be called based on object AND NOT BASED ON POINTER. Because if the function of the base class is called then that is logically wrong.
- Hence to call the overridden function in the derived class we have to make the function in the base class VIRTUAL

- Hence C++ allows two things:

1. Don't make it virtual - function of the base class will be called.
2. Make it virtual - function of the derived class will be called

- Note the series of situations here:

1. Base class pointer having a function which is virtual.
2. Derived class having the function which is over-ridden in the base class
3. Base class pointer.
4. Derived class object
5. You are calling the overridden function of the derived class using the pointer of the base class

```c++
#include <iostream>
using namespace std;

class BasicCar
{
public:
    virtual void start() { // virtual function
        cout << "Basic Car started" << endl;
    }
};

class AdvanceCar: public BasicCar
{
public:
    void start() { // over-rided function
        cout << "Advance Car started" << endl;
    }
    
    void stop(){
        cout << "Advance Car stopped" << endl;
    }

};

int main()
{
    BasicCar* p = new AdvanceCar(); // This means p contains the address of a variable whose data type is BasicCar
    
    //p->stop(); // Any attempt to use the parent class pointer to call the member function of the subclass that does not override the parent class will be regarded as illegal by the compiler, so such a program cannot be compiled at all.
    p->start();

    //AdvanceCar* adPtr = new AdvanceCar();
    //adPtr->stop();
    return 0;
}
```

## Polymorphism Example

```c++
#include <iostream>
using namespace std;

class Car // Abstract Class or Interface
{
public:
    virtual void start() = 0; // Pure Virtual Function
    virtual void stop() = 0; // Pure Virtual Function
};

class Innova: public Car
{

public:
    void start(){
        cout << "Innova Started" << endl;
    }

    void stop(){
        cout <<"Innova Stopped" << endl;
    }
};

class Swift: public Car
{

public:
    void start() {
        cout << "Shift Started" << endl;
    }

    void stop() {
        cout <<"Shift Stopped" << endl;
    }

};
int main()
{
    Car *c = new Innova();
    c -> start(); // here the innova function start will be called
    c = new Swift();
    c -> start(); // here the swift function start will be called
    return 0;
}
```

- Now here when Innova object is pointed by the base class pointer then the Innova function start will be displayed and similarly when the swift object is pointed by the base class pointer then the swift function will be called.
- Hence the pointer is the same but the objects are different and hence as we are using virtual function. different functions are called depending upon the object pointed by the pointer. Here the lines c->start is the same that is pointer is calling the same function but of different objects. This is nothing but **Polymorphism**. And in the example below we are achieving **Run-time Polymorphism**. The same Mechanism in JAVA is called DYNAMIC METHOD DISPATCH.
- Function in the base class has to be virtual because we know that whenever the function of the derived class is called using the base class pointer then the function of the derived class object only must be called.
- Here there is no use of the base class functions even though derived class is inheriting from it, because the functions inherited from the base class are already overridden in the derived class. Hence we can remove the function code in the base class because the objects of the base class will never be created. But we wrote those functions in the base class to just achieve polymorphism and we want those functions to be implemented by the derived class. Also, we want to force overriding of the functions present in the base class in the derived class. To make this COMPULSARY we have to assign virtual base function ZERO. This is called **Pure Virtual Functions**.
- **DERIVED CLASS FUNCTION MUST OVERRIDE PURE VIRTUAL FUNCTION OF THE BASE CLASS OTHERWISE THE FUNCTIONS OF THE DERIVED CLASS WILL BECOME ABSTRACT. HENCE THE PURPOSE OF THE PURE VIRTUAL FUNCTION IS TO ACHIEVE POLYMORPHISM**
- **YOU CANNOT CREATE THE OBJECT OF BASE CLASS HERE BUT YOU CAN HAVE A POINTER OF THE CAR CLASS.**

## Abstract Class

- The class which has pure virtual function is called as **Abstract Class.**
- **The object of this abstract class cannot be created only POINTERS of this abstract class can be created.**
- **Hence the purpose of the abstract class is just to achieve POLYMORPHISM.**

Based on the types of the functions the classes are bifurcated in to three types:

1. Base class having only concrete functions which are used only for Inheritance.
2. Base class having some concrete functions + pure virtual functions. These are used for reusability + polymorphism.
3. Base class having only pure virtual functions. These are used only to achieve polymorphism and are called **INTERFACE**

# Destructor

* Let us define a constructor first. The destructor will have the same name as the 
  constructor but with ~ before it

**Example 1:**

```c++
#include <iostream>
using namespace std;

class Test
{

public:
	Test() {
	cout << "Test Created" << endl; // called automatically when the object is created
	}
	
	~Test() {// called automatically when object is destroyed.
	cout << "Test Destroyed" << endl;
    }
};
	
int main () {
	Test t; // constructor will be called here when object is created
	} // destrcutor will be called here that is when program ends all the objects used are destroyed.
```

**Example 2:**

Let us say that we have allocated memory dynamically in heap

```c++
class Test
{
public:
    int x = 10;
};
	
main() {
Test* ptr = new Test(); // contructor will be called
delete ptr; // destructor will be called
}
```

- Constructors are used for initialization purpose there is also one more use of constructors
- **Constructors are used for allocating the resources then destructors are used for de-allocating resources.**
- These resources include external things like heap memory, file, etc anything the class is acquiring

**Example 3:**

```c++
#include <iostream>
using namespace std;

class Test
{
public:
    int *p;

    Test() { // constructor allocating resources
    p = new int[10];
    }

    ~Test() { // destrcutor deallocating resources.
    delete[]p;
    }
};
```

* **Difference between Constructor and Destructor**
  - Constructors can be over-loaded while destructors cannot be
  - Both constructors and destructors cannot return anything
  - All the rules of constructors are also followed by destructors 
  - Destructors can also be virtual like constructors

## Destructor Properties

```c++
#include <iostream>
using namespace std;

class Base
{
public:
	Base() { cout << "Base constructor" << endl;}
	~Base() { cout << "Base destructor" << endl;}
};

class Derived: public Base 
{
public:
	Derived() { cout << "Derived constructor" << endl;}
	~Derived() { cout << "Derived destructor" << endl;}
};

int main(){
Derived d;
}
```

- Destructor is used for de-allocating resources like releasing memory, network connection.
- We know that when the derived class is called the constructor of the base class is called first
  and then the derived class constructor is called.
- For Destructor, Destructor is called when the object is destroyed, hence here the destructor will be
  called at the end of the program. 
- **Destructor of derived class is called first and then destructor of base class is called.**

## Virtual Destructor

```c++
int main() {
Base *p = new Derived();
delete p;
}
```

- Consider a base class pointer pointing to an object of the derived class created dynamically in heap.
- Now here when we do delete p then the base class Destructor is called as in C++ functions
  are called depending on the pointer **but the object is of the derived class.**
- Hence the destructor of derived class should be called first and then destructor of the base class should be called but unfortunately this doesn't happen in C++ as in C++ the functions are called based
  on pointer. Here the compiler thinks that the object is of the base class. It will not see what object
  is attached.
- Hence to call the destructor in the order of derived first and then base we have to write a `virtual` destructor.

```c++
#include <iostream>
using namespace std;

class Base
{
public:
    Base() { cout << "Base constructor" << endl;}
    virtual ~Base() { cout << "Base destructor" << endl;}
    // ~Base() { cout << "Base destructor" << endl;}
};

class Derived: public Base 
{
public:
	Derived() { cout << "Derived constructor" << endl;}
	~Derived() { cout << "Derived destructor" << endl;}
};

int main() {
Base *p = new Derived();
delete p;
}
```

- Note here if we don't use the virtual destructor then the resources acquired by base class will
  only get released but the resources acquired by derived class will not be released and hence
  the problem of memory leak will occur.
- Hence if **In the program you are using base class pointer and derived class object then virtual base destructor is a must.**
- Hence base class pointer and derived class object is used for achieving runtime polymorphism. Hence 
  if we want to achieve runtime polymorphism then we have to make runtime functions as virtual and similarly destructor should also be made virtual.





# ---------Less Important Topic------------

# Constructors

## Deep Copy Constructors

- Shallow Constructors are the ones which only copy the values. In Contrast Deep Copy constructors are the constructors which not only copies the values but also allocates the same memory.
- The copy constructor takes a single argument of the same class type as the object being copied, and it creates a new object with the same values as the argument object. By default, C++ provides a shallow copy, which means that the values of the object's member variables are copied one by one from the source object to the new object. **However, if the object contains pointers or other objects, a shallow copy may result in unexpected behavior or memory leaks. In such cases, a deep copy should be performed, which involves copying the contents of the pointed-to objects as well.**

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

- Over here the copy constructor will create a variable a = 5 just like original constructor however the pointer created by this copy constructor will also point to the same array of size 5 which was created by the original constructor.
- This is completely wrong and hence DEEP COPY CONTRUCTORS are used which takes care of such issues. **Meaning the copy constructor will create a new array in the heap and its pointer will point to that new array**
- For this we have to write code to create new array in the heap in the copy constructor 

```c++
Test (Test &t)
{
	a = t.a;
	p = new int[a]; // now this will point to a new array created in heap
	}
```

**If you are careful about these things then your constructor is a deep copy constructor.**

# Inline Functions

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

# This Pointer

- In C++, the `this` pointer is a special keyword that refers to the object that the member function is called on. It is a pointer to the object itself, and it can be used inside the member functions to access the member variables and member functions of the object.
- In the cases when the parameter passed to the constructor of the class has same name to that of the data member of the class. The compiler gets confused because of the same name. 
- In this case the length of the class will get assigned to the length of the class and the length of the object (parameter passed) will not be accessed at all.
- This pointer is used to indicate the members of the class.

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

# Structures in C++

- In `struct` by default everything is PUBLIC while in class by default everything is PRIVATE.
- In C the `struct` can only have data while in C++ the `struct` can have class as well as data.
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

# Operator Overloading

Operator overloading in C++ allows operators to be given specific meanings when applied to user-defined data types. It allows you to define the behavior of an operator when used with a custom data type or class.

C++ allows the following operators to be overloaded:

- Unary operators: `+`, `-`, `++`, `--`, `*`, `&`, `!`, `~`
- Binary operators: `+`, `-`, `*`, `/`, `%`, `^`, `&`, `|`, `<<`, `>>`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `,`
- Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `^=`, `&=`, `|=`, `<<=`, `>>=`

Operator overloading is done by defining a special function called an operator function, which has the keyword "operator" followed by the operator symbol. 

There are two ways of overloading a function.

1. Member function Overloading 
   - Notice that operation above is like I am having some money and friend is having some money an 
     either of us is adding that money
2. Friend function Overloading
   - Notice that this operation is like I am having some money and friend is having some money and a third friend of us is adding the money taking money from each of us individually.

For example, to overload the `+` operator for a custom class, you can define a function like this:

## Member function Overloading

```c++
#include <iostream>

using namespace std;

class complex
{
public:
    
    int real;
    int img;
    
    complex (int r=0, int i=0)
    {
        real = r;
        img = i;
    }
    
    // complex add(complex& x)
    complex operator+(complex& x) // return type and argument type is both complex
    {
        complex temp;
        temp.real = real + x.real; // The real here represents the real of class complex itself
        temp.img = img + x.img; // here the function is called on class c1 hence real and img represents the real and img of class c1
        return temp;
    }
    
};


int main()
{

   complex c1 (5, 3);
   complex c2 (10, 5);
   //complex c3 = c1.add(c2); Conceptually we want to call add member function on c1 class, but instead of add we can have to write operator+, but then the function name will also get changed to operator+ 
   //complex c3 = c1.operator+(c2);

   // We can also add it just like we add the two int 
   complex c3 = c1 + c2;
   cout << "Result of the object addition = " << c3.real << " " << c3.img << " " << endl;
   return 0;
}
```

## Friend Operator Overloading 

- In friend operator overloading neither c1 will add nor c2 will as shown in the previous example of operator overloading Instead over here 3rd `friend` function will add the numbers. Hence this function will take the parameters from both the complex numbers c1 and c2.

```c++
#include <iostream>

using namespace std;
class complex
{

private:
    int real, img;
public:

    complex (int r=0, int i = 0)
    {
        real = r;
        img = i;
    }

    void Display() { cout << "Result of addition = " << real << " " << img << endl;}

    friend complex operator+(complex c1, complex c2);

};

   complex operator+(complex c1, complex c2)
    {
        complex temp;
        temp.real = c1.real + c2.real;
        temp.img = c1.img + c2.img;
        return temp;
    }

int main()
{
   complex c1 (5, 3);
   complex c2 (10, 5);
   complex c3 = c1 + c2;
   c3.Display();
   return 0;
}
```

# Friend and Static Members, Inner Classes

## Friend Function

In C++, a friend function is a function that is declared within a class but is not a member of that class. It is given access to the private and protected members of the class, allowing it to manipulate the data in the class.

To declare a friend function, the friend keyword is used in the class definition, followed by the function declaration. Here's an example:

```C++
#include <iostream>
using namespace std;

class MyClass {
private:
    int x;
protected:
    int y;
public:
    void setX(int x_value, int y_value);
    friend void friendFunction(MyClass obj);
};

void MyClass::setX(int x_value, int y_value) {
  x = x_value;
  y = y_value;
}

void friendFunction(MyClass obj) {
    cout << obj.x << " " << obj.y << endl;  // Outputs 5, 7    
    obj.x = 10;
    obj.y = 20;
    cout << obj.x << " " << obj.y << endl;  // Outputs 10, 20    
}

int main() {
  MyClass myObj;
  myObj.setX(5, 7);
  friendFunction(myObj);
  return 0;
}
```

Hence if we want to allow any function outside the class to access all its data members then **we have to declare that function as FRIEND function inside the class AND THE OUTSIDE FUNCTION SHOULD HAVE OBJECT OF THAT CLASS**

## Friend Class

In C++, a friend class is a class that is granted access to the private and protected members of another class. Like friend functions, friend classes can access and manipulate the private and protected members of the class they are friends with.

To declare a friend class, the friend keyword is used in the class definition, followed by the name of the friend class. Here's an example:

```c++
#include <iostream>
using namespace std;

class MyClass {
private:
  int x;
  friend class FriendClass;
};

class FriendClass {
public:
  void setX(MyClass obj, int value) {
    obj.x = value;
    cout << obj.x;  // Outputs 5
  }
};

int main() {
  MyClass myObj;
  FriendClass friendObj;
  friendObj.setX(myObj, 5);
  return 0;
}
```

## Static Members

In C++, a static member of a class is a member that belongs to the class itself rather than to individual objects of the class. This means that there is only one copy of the static member, which is shared by all objects of the class.

Static members can be either static data members or static member functions. A static data member is a variable that is shared by all objects of the class, while a static member function is a function that operates on static data members or other static member functions, and does not have access to the non-static members of the class.

To declare a static data member in a class, the static keyword is used before the member's declaration. Here's an example:

```c++
#include <iostream>
using namespace std;

class MyClass {
public:
  int a, b;
  static int count;
  MyClass() {
    count++;
  }
};

int MyClass::count = 0; // count to be used only within the class test hence scope resolution is given. Also notice that the static members has to be defined outside the class ONLY and also notice how the datatype "int" is mentioned again.

int main() {
  MyClass obj1;
  MyClass obj2;
  MyClass obj3;
  cout << MyClass::count; // Outputs 3
  return 0;
}
```

- Here note that all the objects will have its own a and b, but count will be allocated in the memory only once and will be shared by all the objects.
- Hence Static variables or data members belong to class and not object and all the objects can use it. These are common for all objects and can be shared by all the members of the class.
- **Static Variable should also be defined outside the class just like global variables but we want it to be accessed by only MyClass class hence we have to use scope resolution operator.**

## Static Member Functions

```c++
#include <iostream>
using namespace std;

class MyClass {
private:
    int a, b;
    static int x;
public:
    static int getX() {
        return x;
  }
};

int MyClass::x = 5;

int main() {
    cout << MyClass::getX() << endl; // Outputs 5
    return 0;
}
```

- Notice `static int getX()` here which is static members function can only access count and not a, b. 
- Hence static member functions can only access static data members (an not non-static data members) and hence static member functions also belongs to a class and can be called similarly to static members using scope-resolution operator.

## Example of using Static Members

```c++
#include <iostream>
using namespace std;


class student
{
public:
    int rollno;
    string name;
    static int addminNo;

    student(string n)
    {
        name = n;
        addminNo++;
        rollno = addminNo;

    }

    void display()
    {
        cout << "Name " << name << " " << "Roll " <<rollno << endl;
    }
};

int student::addminNo=0;

int main()
{
    student s1("Ibrahim");
    s1.display();
    student s2("Shawn");
    s2.display();
    student s3("Laidong");
    s3.display();

    cout << "Number of admissions " << student::addminNo << endl;
    //cout << "Hello world!" << endl;
    return 0;
}
```

## Nested/ Inner Class

In C++, a nested class, also known as an inner class, is a class that is defined inside another class. 

A nested class can have access to the private and protected members of the enclosing class, just like any other member function of the enclosing class **given that they are declared as static**

There are two types of nested classes in C++: nested classes and local classes. A nested class is a class that is defined inside another class, while a local class is a class that is defined inside a function.

Here's an example of a nested class:

```c++
#include <iostream>
using namespace std;

class EnclosingClass {
public:
  static int x;
  class NestedClass {
  public:
    void print() {
      cout << "Hello from nested class!" << " " << EnclosingClass::x << endl; // Only static int of the outer class accessible inside the inner class
    }
  };
};

int EnclosingClass::x = 10;

int main() {
  EnclosingClass::NestedClass obj;
  obj.print(); // Outputs "Hello from nested class!"
  return 0;
}
```

Here note that inner class **CANNOT ACCESS ANY MEMBERS OF THE OUTER CLASS BUT ONLY STATIC MEMBERS**

Here's an example of a local class:

```c++
#include <iostream>
using namespace std;

void myFunction() {
  class LocalClass {
  public:
    void print() {
      cout << "Hello from local class!";
    }
  };
  
  LocalClass obj;
  obj.print(); // Outputs "Hello from local class!"
}

int main() {
  myFunction();
  return 0;
}
```

## Example of Nested Functions

```c++
#include <iostream>
using namespace std;

class outer
{
private: static int b;   
public:
    int a = 10;

    void fun() {
        i.show(); // accessing show function of the inner class
        cout << i.x << endl; // accessing x of the inner class
    }

    class inner
    {
    public:
        int x = 25;
        void show() {
            cout << b << endl;   // static int of the outer class accessible inside the inner class
        }
    };

    inner i; // creating an object of the inner class

};

int outer::b = 20;

int main() {
    outer::inner j; // creating instance of the inner nested class of the outer class
    j.show();

    outer o;
    o.fun();
    return 0;
}
```

# Constants, Preprocessor Directives and Namespace

## Constant Qualifiers

**1. Used as a constant identifier inside a function or class**

If we write `const int x = 10;`  then it becomes constant identifiers and this constant identifier cannot be modified.

The properties of constant identifiers are as follows:

1. Constant Identifier is a also an identifier like variable albeit this identifier cannot be modified.
2. This will consume memory as per the datatype declared
3. Constants are the part of the compiler.
4. Used for declaring constants inside the class or function

- In contrast `#define x 10` is also a constant but it is a preprocessor directive and it is executed before compilation process starts.

**Pre-Processor Directives**

The properties of preprocessor directive are as follows:

1. x also cannot be modified.
2. preprocessor directives does not hold space in memory. It is just like a symbol.
3. This is not part of a language. It is outside compiler meaning pre-compiler
4. These are used for declaring constants if it is used by the entire program just like a global variable.

**2. Used as a pointer of type constant integer**

```c++
#include <iostream>
using namespace std;

int main()
{
    //const int x = 10;	// notice that here we cannot simply write const int x=10 and expect that pointer can point to it
    int x = 10; // Also note that after making the pointer of type integer constant we can also define int x as const and it will work as expected. Also we can directly make pointer of type int constant without defining x as const explicitly
    const int* ptr = &x;
    // int const *ptr=&x; // This can also be written this way
    //(*ptr)++;
    //++*ptr;
    cout << *ptr << endl;
}
```

- Note that in this case CONSTANT TO AN INTEGER POINTER cannot modify x when we write `++*ptr` because data is locked.
- Also note that `cout << *ptr` can access the value of x but cannot modify it as it will treat the data as constant.
- Notice that here we cannot simply write `const int x=10` and expect that pointer can point to it
- Address of constant identifier cannot be stored to the pointer hence we have to make a constant pointer
- This can be read from right to left as pointer of type integer constant.
- Also note that after making the pointer of type integer constant we can also define `int x` as `const` and it will work as expected. Also we can directly make pointer of type int constant without defining x as const explicitly.

```C++
int main()
{
    int x = 10;
    const int* ptr=&x;
    // int const* ptr=&x; // This can also be written this way
    int y = 20;
    ptr = &y; // now we are pointing the same pointer to address of y
    ++ *ptr; // This cannot be modified as the integer is a constant.
    cout << *ptr;
}
```

- In this case now the pointer will point to the address of y but note that even now it won't be able
  to modify the value of y.

**3. Used as a constant pointer of type integer**

- Instead of `int const* ptr` if we write `int* const ptr` then instead of data, pointer becomes locked now and hence cannot be modified. This means that pointer can now point to only one address which cannot be changed.

```c++
int main()
{
    int x = 10;
    int* const ptr=&x; // This is now constant pointer of type integer
    int y = 20;
    ptr = &y; // This is not possible now as the pointer itself is constant
    ++ *ptr; 
    cout << *ptr;
}
```

**4. Used as a constant pointer to integer constant**

- If we write `const` before the constant pointer of type integer then it becomes constant pointer
  to integer constant. Hence now data is constant and also pointer is constant.

```c++
int main()
{
    int x = 10;
    const int* const ptr=&x; // This is now constant pointer to integer constant
    int y = 20;
    ptr = &y; // This is not possible now as the pointer itself is constant
    ++ *ptr; // Now this is also not possible as data cannot be modified.
    cout << *ptr;
}
```

**5. Constant Function**

```c++
#include <iostream>
using namespace std;

class Demo
{
public:
	int x=10;
	int y=20;
	
void Display() const
{
    cout << x << " " << y << endl;
    x++;
    y++;
    cout << x << " " << y << endl;
}
};
```

- In this example if we don't want the member function to modify the values of data members then
  we can write `const` at the end of the member function. These are helpful when we want the member function to avoid modifying the data members by mistake.

**6. Constant call by reference**

```c++
#include <iostream>
using namespace std;

void fun(int &x, int &y) // call by reference hence x and y are alias of a and b 
// void fun(const int &x, const int &y)
// also notice that for call by reference we know that the function fun will be copied at the place of function call hence it becomes inline function because as we know that it is not possible for the function to modify the values of another function unless being an inline function. 
{
    x++;
    y++;
    cout << x << " " << y << endl;
}

int main()
{
    int a = 10, b = 20;
    fun(a,b);
}
```

- One of the benefits of the inline functions is it makes the code simple as the function is copied to 
  the place of the function call but there is one big disadvantage. This is that lets say here in the 
  function x is being incremented but now x is an alias of a hence the function is modifying the original integer a. If we don't want to allow the function fun to modify the values of the original function we can define them as `const` as shown 

## Pre-processor Directives

- These are also called as macros. These are instructions to compiler so that before starting compilation it can follow those instructions.
- They are instructions to compiler. They are processed before compilation
- They are used for defining symbolic constant
- They are used for defining functions. They also support conditional definition
- Most famous of these are #define

1. **Defining variable as constant**

```c++
# define PI 3.1425

int main() {
    cout << PI;
}
```

- Here the value of PI will be replaced by 3.1425 before the compilation begins hence the compiler will 
  see 3.1425 in the program and not PI.
- These # define pi (value) are known as SYMBOLIC CONSTANTS

2. **Defining object name as constant** 

```c++
#include <iostream>
using namespace std;

# define c cout // hence now we can also change object name

int main() {
c << "Ibrahim";
}
```

3. **Defining functions as pre-processor directives**

```c++
# define SQR(x) (x * x) // NOTICE THAT EQUATION (x*x) HAS TO BE WRITTEN IN BRACKETS

int main(){
cout << SQR(5);
}
```

4. **Defining message to be displayed in double quotes**

```c++
#include <iostream>
using namespace std;

# define MSG(x) #x

int main() {
cout << MSG(Hello); // here MSG(Hello) will be replaced by "Hello" and Hello will be displayed on the screen
}
```

5. **If not defined**

```c++
Ifndef: // if not defined

# ifndef: 
	# define PI 3.142517
# endif
```

- Defining the value only if it is not defined because redefining will cause an error.

```c++
#include <iostream>
using namespace std;

#define max(x,y) (x>y?x:y)
#define msg(x) #x

#ifndef PI
	#define PI 3.1425
#endif

int main()
{
    cout<<PI;
    cout<<max(10,12)<<endl;
    cout<<msg(hello)<<endl;
}
```

## Namespace

- Namespaces are used for removing name conflicts
- If we require the functions or classes with the same name or signature or prototype then there will 
  be name conflicts
- Ibrahim: NAMESPACE ARE USED TO STRUCTURE A PROGRAM INTO LOGICAL UNITS

```c++
void fun(){
cout << "First";
}

void fun(){
cout << "Second";
}

int main(){
fun();
}
```

- Here the compiler will not compile the program at the first place because name conflict will happen.
- Using the namespace we can encapsulate the function inside the namespace and then we can call the functions separately using the scope resolution operator.

```c++
namespace First {					// these brackets are mandatory
	void fun() {
	cout << "First";
	}
}

namespace Second {
	void fun() {
		cout << "Second";
		}
}

int main() {
First::fun();
}
```

- Also note that in one namespace we can have many other things like all the related classes, functions
  and objects
- Also If we want to avoid using scope resolution operator all the time we can write **using namespace std**

```c++
using namespace first; // RECOMMENDED TO AVOID THESE KIND OF STATEMENTS
int main() {
fun();			// if you don't mention anything fun of first will be called
second::fun();  // if you explicitly mention namespace using scope resolution operator then second will be called
}
```

- NOW WE CAN UNDERTAND THAT INSTEAD OF NAMESPACE STD DECLARATION IN EVERY PROGRAM WE CAN ALSO WRITE

```c++
std::cout<<"kkk"<< endl;
```

# 

