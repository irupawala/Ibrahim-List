#include <iostream>

using namespace std;


class Base
{
public:
    void display()
    {
        cout << "Display of Base" << endl;
    }
};

class Derived: public Base
{
public:
    void display() // By giving the same name to the function you have overrided the function display.
    {
        cout << "Display of Derived" << endl;
    }
};
class Derived_Parameteized: public Base // FUNCTION OVERLOADING
{
public:
    void display(int x) // By giving the same name to the function you have overrided the function display.
    {
        cout << "Display of Parameterized Derived" << endl;
    }


};
int main()
{
    Derived d;
    Derived_Parameteized dp;
    //d.display(); // Calling the overrided display of derived class
    d.Base::display(); // Calling the display of base
    //dp.display(10);
    return 0;
}
