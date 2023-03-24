## [14] Base Class Pointer Derived Class Object

**Consider the example below**

```c++
Class Base
{

public:

	void fun1();
	void fun2();
	void fun3();

};


Class Derived: public Base
{

public:

	void fun4();
	void fun5();
};


int main()
{
Derived b;

b.fun1();
b.fun2();
b.fun3();
b.fun4();
b.fun5();
}
```

* Here we already know that from the derived class we can call both the function of the base class as well as derived class
* Now let us have a base class pointer point on derived class object.

## 1. Base Class pointer on derived class object

```c++
Base *p;
p = new Derived(); // note that here base class pointer is poiting on derived class object. Also note that here the Derived class is in a heap.
```

* Hence now as we know for the derived object we can call the functions of the derived class as well as base class.

- But the question is whose functions will be called base or derived class ?. Pointer is of base class but object is of derived class ?
Answer: BASE CLASS FUNCTION WILL BE CALLED.

* But then can we call the fun4 and fun5 of the derived class ?. 

* Answer is NO. Hence we can only call the functions of the base class and not the functions of the derived class though the object is derived class BECAUSE THE POINTER IS OF BASE CLASS.

  

* EXAMPLE 1:

  Let us say we have pointer of base class rectangle *p. Then we can have object of cuboid. and the pointer of base class p can point to the object of derived class cuboid.

  Hence over here we can only call the function of the base class rectangle like area and perimeter but not the function of the derived class cuboid like volume.



* EXAMPLE 2

  Let us say we have a basic car and then we have a advanced car hence we have a basic car class and then we also have advanced car derived class.

  Also we can have a basic class pointer and advanced class object

  ```c++
  BasicCar *p;
  p = AdvancedCar();
  ```

  Hence we can also say that basic car is an advanced car. Hence when we have a pointer of the base class, we can call all the functions inside the base class that is basic car but not the advanced functions inside the derived class because the pointer is BASE.

## 2. Derived Class object on base class pointer

* Now let us have Pointer of the derived class on the object of the base class 

* Is it possible to have this?. Answer: NO.

* EXAMPLE 1: 

  Can we say that the basic car is an advanced car ?. NO because the features of the advanced car is not present in the basic car.