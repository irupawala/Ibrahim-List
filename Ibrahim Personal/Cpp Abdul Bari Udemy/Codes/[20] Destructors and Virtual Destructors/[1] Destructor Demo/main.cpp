#include <iostream>

using namespace std;


class Demo
{
    int *p;
public:
    Demo()
    {
        p = new int[5];
        cout << "Constructor of Demo" << endl;
    }

    ~Demo()
    {
        delete []p; // Deleting the memory in the destructor to avoid memory leak problems
        cout << "Destructor of Demo" << endl;
    }
};

void fun()
{
    // Object created in the stack. Note that destructor will be called automatically after the function ends
    //Demo d;

    // Object created in heap.
    Demo *p = new Demo();
    delete p; // Notice here that object won't be deleted automatically
}
int main()
{

   // Demo d;
    fun ();
    //cout << "Hello world!" << endl;
    return 0;
}
