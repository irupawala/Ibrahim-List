#include <iostream>

using namespace std;

class BasicCar
{
    public:
        virtual void start ()
        {
            cout << "car starts" << endl;
        }

};



int main ()
{
    BasicCar b;
    // Call by function name
    //b.start();
    // Call by function pointer
    typedef void (*Fun) ();
    Fun pFun  = NULL;

    pFun = (Fun)*(int *)*(int *)&b;
    pFun();

    return 0;
}
