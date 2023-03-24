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
   // Derived d;
   // Derived d(10);
   Derived d(20, 10);
    return 0;


}
