# [13] Inheritance

## [13.1] Introduction

 - Inheritance is deriving the class from the existing pre-defined class.
 - It is a process of acquiring features of an existing class into a new class
 - It is used for achieving reusability
 - features of base class will be available in derived class

Look in to this example to how are classed derived.

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

## [13.2] Constructor in Inheritance

* Notice that whenever the derived class is called constructor of default class is called first.
* Remember the example of Table Manufacturer. For default table dimensions table manufacturer will give order of default table top.
*  When the derived class is called it will CALL the base class and the base class will be EXECUTED FIRST and then derived class will be EXECUTED
* CALLING HAPPENDS FROM BASE TO DERIVE BUT EXECUTION HAPPENDS FROM DERIVED TO BASE

```c++
#include <iostream>

using namespace std;

class Base
{
public:

    Base()
    {
        cout << "Default of base " << endl;
    }

    Base(int x)
    {

        cout << "Param of base " << x << endl;
    }

};

class Derived : public Base
{
    public:
    Derived()
    {
        cout << "Default of Derived" << endl;
    }

    Derived(int a)
    {
        cout << "Param of Derived " << a << endl;
    }

    Derived (int x, int a): Base(x)
    {
        cout << "Param of Derived " << a << endl;
    }
};



int main()
{
   // Derived d;  // calling default constructor of base class from the default constructor of derived class
   // Derived d(10); // calling default constructor of base class from the parameterized constructor of derived class
   Derived d(20, 10); // // calling parameterized constructor of base class from the parameterized constructor of derived class
    return 0;

}

```

* Notice how the parameterized constructor of the base class is called from the derived `class Derived (int x, int a): Base(x)`

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

## [13.3] IsA and HasA

Consider a class rectangle

```c++
class Rectangle
{

}

class cuboid: public rectangle
{

}


class Table
{
Rectangle top;
int legs;

}
```



* Here cuboid is Inherited from rectangle hence cuboid **IsA** Rectangle
* Here Table is having object of rectangle class. Hence table class **HasA** Rectangle

* There are two ways a class can be used:

1. Class can be derived: IsA
2. Object of a class can be used: HasA

* Now a class can be have 3 kinds of members.

1. private
2. protected
3. public

* Now the topic of discussion is which members is accessible in base class, which is accessible in derived class and which are accessible upon object. This is called as **Access Specifiers**.

## [13.4] Access Specifiers

* Data Hiding is one of the main features of OOP

Access Specifiers

* Private - Accessible only inside a class
* Protected - Accessible inside a class and inside derived classes
* Public - Accessible inside class, inside derived class and upon object

```c++
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
	x.c = 90; // public member accessible by object 
}
```

* a (private) and b (protected) CANNOT be accessed but public object c CAN be accessed on object upon class
* Derived class can access the protected and public but not private
* Base class can access all its members private, protected and public

## [13.5] Types and Ways of Inheritance

Types of Inheritance:

1. Simple/ Single Inheritance
2. Hierarchical Inheritance
3. Multi-Level Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance - Mixture of two inheritance


- Multipath Inheritance: The features of base class A will be available in D via B and C.
- Here the ambiguity is that the function D should get features of A via B or C ??
- To remove this ambiguity virtual base class is used. If we write VIRTUAL for class B and D then there will be no ambiguity.

- Virtual base class is used to remove the ambiguity of the derived class from the parent class which are coming through multiple classes.



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[14] Inheritence\[5] Types and Ways of Inheritence\[2] Types of Inheritence.PNG)



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[14] Inheritence\[5] Types and Ways of Inheritence\[3] Virtual Base class.PNG)



## [13.6] Ways of Inheritance

* Ways of inheritance

A class can be inherited in flowing ways :

Publicly - All members of base will have same accessibility in derived class except private
Protectedly - All members of base will become protected in derived class 
Privately - All members of base will become private in derived class

* Note :

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

## [13.7] Generalization Vs Specialization

* Consider the two examples. 

1. Cuboid Inherited from rectangle. OR fortuna inherited from Innova

2. Rectangle, circle, quadrilateral have a generalized term SHAPE. Shape is a virtual term which does not actually exist.

- Here 2. is generalization where the child classes already exists but to bring them to a common platform we have given a name shape.
- We can calculate area and perimeter of a rectangle, circle but not of shape but shape has those functions it just can't be calculated because shape does not have dimensions.

Hence there are two types of Inheritance.

1. Parent was existing and child was defined later hence child borrowed the features from parents. This is specialization.
Purpose here is to give something to child class.

2. Child classes were existing and then we defined the base class. This is generalization.
Purpose here is to group the child classes together. Hence purpose of Generalization is nothing but **POLYMORPHISM**.

