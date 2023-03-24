#include <iostream>

using namespace std;


class Base
{
public:
    void fun1()
    {
        cout << "fun1 of Base" << endl;
    }
};

class Derived: public Base{

public:
    void fun2()
    {
        cout << "fun2 of Derived" << endl;
    }


};

int main()
{
   Derived d;
   Base *ptr = &d;
   ptr->fun1();
   //ptr->fun2(); // here note that the pointer of base class cannot call the function of the derived class
   // It can only call the function of the base class

   /*
   Base b;
   Derived *ptr = &b; // here this won't work as the pointer of derived class cannot point to the object of base class
   */
   return 0;
}
