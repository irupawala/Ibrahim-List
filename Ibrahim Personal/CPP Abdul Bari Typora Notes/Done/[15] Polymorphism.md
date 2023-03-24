# [15] Polymorphism

## [15.1] Function Overriding

* Function overriding is nothing but overriding the function defined in the base class from the derived class.
* Consider the example below:

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

class Derived: public Base
{
public:
    void display() { // By giving the same name to the function you have overrided the function display.
        cout << "Display of Derived" << endl;
    }
};

class Derived_Parameteized : public Base // FUNCTION OVERLOADING
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
    dp.display(10);
    return 0;
}
```

## [15.2] Virtual Function

- Here note that when we call a overridden function of the derived class using the pointer of the base class then the functions of the BASE CLASS IS CALLED.

- If we take real world example then let us say we have derived class advanced car which is pointed by the pointer of the base class basic car. But the object here is actually advanced car hence will it run as a basic car or advanced car ?. it will run like advanced car though we are calling it a basic car.

- Hence Similarly in the programming if the function is present in the base class as well as derived class then the function of the DERIVED CLASS MUST BE CALLED that is the function should be called based on object AND NOT BASED ON POINTER. Because if the function of the base class is called then that is logically wrong.

- Hence to call the overridden function in the derived class we have to make the function in the base class VIRTUAL

* Hence C++ allows two things:

1. Don't make it virtual - function of the base class will be called.
2. Make it virtual - function of the derived class will be called

* Note the series of situations here:

1. Base class pointer having a function which is virtual.
2. Derived class having the function which is over-ridden in the base class
3. Base class pointer.
4. Derived class object
5. you are calling the overridden function of the derived class using the pointer of the base class

```c++
#include <iostream>

using namespace std;


class BasicCar
{
public:
    virtual void start() // virtual function
    {
        cout << "Basic Car started" << endl;
    }
};

class AdvanceCar: public BasicCar
{
public:
    void start() // over-rided function
    {
        cout << "Advance Car started" << endl;
    }
    
    void stop()
    {
        cout << "Advance Car stopped" << endl;
    }

};
int main()
{
	//AdvanceCar A;
    //BasicCar *p = &A;
    BasicCar *p = new AdvanceCar(); // This means p contains the address of a variable whose data type is BasicCar
    
    //p->stop(); // Any attempt to use the parent class pointer to call the member function of the subclass that does not override the parent class will be regarded as illegal by the compiler, so such a program cannot be compiled at all.
    p->start();
    
    return 0;
}

```

## [15.3] Polymorphism

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
    void start()
    {
        cout << "Innova Started" << endl;
    }

    void stop()
    {
        cout <<"Innova Stopped" << endl;

    }

};

class Swift: public Car
{

public:
    void start()
    {
        cout << "Shift Started" << endl;
    }

    void stop()
    {
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
- Hence the pointer is the same but the objects are different and hence as we are using virtual function. different functions are called depending upon the object pointed by the pointer. Here the lines c->start is the same that is pointer is calling the same function but of different objects. 
- This is nothing but POLYMORPHISM. And in the example below we are achieving RUN TIME POLYMORPHISM. The same Mechanism in JAVA is called DYNAMIC METHOD DISPATCH.
- Function in the base class has to be virtual because we know that whenever the function of the derived class is called using the base class pointer then the function of the derived class object only must be called.
- Also note that the derived class like Innova, Swift are defined first and then base class is defined to achieve generalization CAR in this case. And generalization is done to achieve polymorphism. so that we can call Innova and swift using the same base class pointer car.
- Here there is no use of the base class functions even though derived class is inheriting from it, because the functions inherited from the base class are already overridden in the derived class. Hence we can remove the function code in the base class because the objects of the base class will never be created. But we wrote those functions in the base class to just achieve polymorphism and we want those functions to be implemented by the derived class. Also, we want to force overriding of the functions present in the base class in the derived class. To make this COMPULSARY we have to assign virtual base function ZERO. This is called **PURE VIRTUAL FUNCTION**.
- **DERIVED CLASS FUNCTION MUST OVERRIDE PURE VIRTUAL FUNCTION OF THE BASE CLASS OTHERWISE THE FUNCTIONS OF THE DERIVED CLASS WILL BECOME ABSTRACT. HENCE THE PURPOSE OF THE PURE VIRTUAL FUNCTION IS TO ACHIEVE POLYMORPHISM**
- **YOU CANNOT CREATE THE OBJECT OF BASE CLASS HERE BUT YOU CAN HAVE A POINTER OF THE CAR CLASS.**

## [15.4] Abstract Class

- The class which has pure virtual function is called as **abstract class.**
- **The object of this abstract class cannot be created only POINTERS of this abstract class can be created.**
- **Hence the purpose of the abstract class is just to achieve POLYMORPHISM.**

Based on the types of the functions the classes are bifurcated in to three types:

1. Base class having only concrete functions which are used only for Inheritance.
2. Base class having some concrete functions + pure virtual functions. These are used for reusability + polymorphism.
3. Base class having only pure virtual functions. These are used only to achieve polymorphism and are called **INTERFACE**

