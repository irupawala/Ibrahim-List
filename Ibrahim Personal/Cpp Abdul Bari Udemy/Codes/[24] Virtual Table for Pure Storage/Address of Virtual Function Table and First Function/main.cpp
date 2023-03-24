#include <iostream>

using namespace std;

class Base
{
public:
    virtual void f()
    {
        cout << "f of Base " << endl;

    }

    virtual void g()
    {
        cout << "g of Base" << endl;
    }

    virtual void h()
    {
        cout << "h of Base" << endl;
    }

};


typedef void (*Fun)();
//void (*Fp)(void); // Function pointer syntax Return Type (*Name of pointer) (variables)

int main()
{
    Base b;
    //cout << "Address of virtual function table " << &b << endl;

    //Base *p1 = &b;
    //cout << "Address of virtual function table " << p1 << endl;

    int *p1 = (int *)(&b); // &b is address
    cout << "Address of virtual function table " << p1 << endl;

    int *p2 = (int *)*(p1);
    cout << "Virtual function table - address of the first function: " << p2 << endl;

    //cout << "Address of virtual function table " << (int *)(&b) << endl;
    //cout << "Virtual function table - address of the first function: " << (int *)*(int *)(&b) << endl;


    //Fun pFun = NULL;
    //pFun = (Fun)*(( int *)*( int *)(&b));
    //pFun();

    Fun fFun = NULL;
    //pFun = (Fun)*(p2);
    fFun = (Fun)*(( int *)*( int *)(&b)+0);
    fFun();

    Fun gFun = NULL;
    gFun = (Fun)*(( int *)*( int *)(&b)+1);
    gFun();

    Fun hFun = NULL;
    hFun = (Fun)*(( int *)*( int *)(&b)+2);
    hFun();

    return 0;
}
