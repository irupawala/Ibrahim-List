# [20] Destructor and Virtual Destructors

## [20.1] Destructor 

- Let us define a constructor first. The destructor will have the same name as the 
constructor but with ~ before it

e.g. 1:

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

e.g. 2:

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

* Constructors are used for initialization purpose there is also one more use of constructors
* CONSTRUCTORS ARE USED FOR ALLOCATING THE RESOURCES THEN DESTRUCTORS ARE USED FOR DEALLOCATING RESOURCES.
* These resources include external things like heap memory, file, etc anything the class is acquiring

e.g.

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

* DIFFERENCE BETWEEN CONSTRUCTORS AND DESTRUCTORS:
  * Constructors can be over-loaded while destructors cannot be
  * Both constructors and destructors cannot return anything
  * All the rules of constructors are also followed by destructors 
  * Destructors can also be virtual like constructors

## [20.2] Destructor Properties

Consider the example below :

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
- For Destructor, DESTRUCTOR OF THE DERIVED CLASS IS CALLED FIRST AND THEN THE DESTRUCTOR OF THE BASE CLASS IS CALLED

## [20.3] Virtual Destructor 

```c++
int main() {
Base *p = new Derived();
delete p;
}
```

* Consider a base class pointer pointing to an object of the derived class created dynamically in heap.

* Now here when we do delete p then the base class Destructor is called as in C++ functions
are called depending on the pointer BUT THE OBJECT IS OF THE DERIVED CLASS.

* Hence the destructor of derived class should be called first and then destructor of the base class should be called but unfortunately this doesn't happen in C++ as in C++ the functions are called based
on pointer. Here the compiler thinks that the object is of the base class. It will not see what object
is attached.

* Hence to call the destructor in the order of derived first and then base we have to write a virtual destructor

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

* Note here if we don't use the virtual destructor then the resources acquired by base class will
only get released but the resources acquired by derived class will not be released and hence
the problem of memory leak will occur.

* Hence if **IN THE PROGRAM YOU ARE USING BASE CLASS POINTER AND DERIVED CLASS OBJECT THEN VIRTUAL BASE DESTRUCTOR IS A MUST.**

* Hence base class pointer and derived class object is used for achieving runtime polymorphism. Hence 
if we want to achieve runtime polymorphism then we have to make runtime functions as virtual and similarly destructor should also be made virtual

