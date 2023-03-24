#include <iostream>

using namespace std;
// class Parent final
class Parent
{
    virtual void show() final
    {

    }

};

class Child: public Parent
{
    void show() // function overloading not allowed if the function in the base class is final
    {

    }

};

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
