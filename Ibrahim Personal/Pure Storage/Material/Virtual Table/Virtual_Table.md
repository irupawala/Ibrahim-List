

## 1. Address of Virtual Function Table and First Function

Notes from https://blog.csdn.net/haoel/article/details/1948051

* An instance of a class with virtual functions, Virtual table is allocated in the memory of this instance.
* The C++ compiler should ensure that the pointer to the virtual function table exists in the frontmost position of the object instance. This means that we get this virtual function table through the address of the object instance, and then we can traverse the function pointer and call the corresponding function.

```c++
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

```



## 2. Types of Inheritance 

1. General inheritance (no virtual function override)
2. General inheritance (with virtual function override)
3. Multiple inheritance (no virtual function override)
4. Multiple inheritance (with virtual function override)

## 3. Virtual function table access for multiple inheritance

```c++
#include <iostream>

using namespace std;

class Base1 {
public:
    virtual void f(){cout << "Base1::f" << endl;}
    virtual void g(){cout << "Base1::g" << endl;}
    virtual void h(){cout << "Base1::h" << endl;}
};

class Base2 {
public:
    virtual void f(){cout << "Base2::f" << endl;}
    virtual void g(){cout << "Base2::g" << endl;}
    virtual void h(){cout << "Base2::h" << endl;}
};

class Base3 {
public:
    virtual void f(){cout << "Base3::f" << endl;}
    virtual void g(){cout << "Base3::g" << endl;}
    virtual void h(){cout << "Base3::h" << endl;}
};

class Derive: public Base1, public Base2, public Base3 {
public:
    virtual void f(){cout << "Derive::f" << endl;}
    virtual void g1(){cout << "Derive::g1" << endl;}
};

typedef void (*Fun) (void); // Syntax return type, *function name, variable of the function

int main()
{
    Fun pFun = NULL;

    Derive d;
    int ** pVtab = (int **)&d;
    //pFun = (Fun)*((int*)*((int*)&d+0)+0);
    //pFun = (Fun)*((int*)*((int**)&d+0)+0);
    //pFun = (Fun)pVtab[0][0];
    //pFun();

    //Base1's vtable
    //pFun = (Fun)*((int*)*(int*)((int*)&d+0)+0);
    pFun = (Fun)pVtab[ 0 ][ 0 ];
    pFun();
    //pFun = (Fun)*((int*)*(int*)((int*)&d+0)+1);
    pFun = (Fun)pVtab[ 0 ][ 1 ];
    pFun();
    //pFun = (Fun)*((int*)*(int*)((int*)&d+0)+2);
    pFun = (Fun)pVtab[ 0 ][ 2 ];
    pFun();
    //Derive's vtable
    //pFun = (Fun)*((int*)*(int*)((int*)&d+0)+3);
    pFun = (Fun)pVtab[ 0 ][ 3 ];
    pFun();
    //The tail of the vtable
    pFun = (Fun)pVtab[ 0 ][ 4 ];
    cout<<pFun<<endl;


    //Base2's vtable

    //pFun = (Fun)*((int*)*(int*)((int*)&d+1)+0);
    pFun = (Fun)pVtab[ 1 ][ 0 ];
    pFun();
    //pFun = (Fun)*((int*)*(int*)((int*)&d+1)+1);
    pFun = (Fun)pVtab[ 1 ][ 1 ];
    pFun();
    pFun = (Fun)pVtab[ 1 ][ 2 ];
    pFun();
    //The tail of the vtable
    pFun = (Fun)pVtab[ 1 ][ 3 ];
    cout<<pFun<<endl;

    //Base3's vtable

    //pFun = (Fun)*((int*)*(int*)((int*)&d+1)+0);
    pFun = (Fun)pVtab[ 2 ][ 0 ];
    pFun();
    //pFun = (Fun)*((int*)*(int*)((int*)&d+1)+1);
    pFun = (Fun)pVtab[ 2 ][ 1 ];
    pFun();
    pFun = (Fun)pVtab[ 2 ][ 2 ];
    pFun();
    //The tail of the vtable
    pFun = (Fun)pVtab[ 2 ][ 3 ];
    cout<<pFun<<endl;

    return 0;
    }

```

## 4. Disadvantages of Virtual Table

1. Access the virtual function of the subclass itself through the pointer of the supertype is not allowed.

* Any attempt to use the parent class pointer to call the member function of the subclass that does not override the parent class will be regarded as illegal by the compiler, so such a program cannot be compiled at all.

2. Access non-public virtual functions

* In addition, if the virtual function of the parent class is private or protected , but these non- public virtual functions will also exist in the virtual function table, so we can also use the method of accessing the virtual function table to access these non-public virtual functions virtual function, this is easy to do.

```c++
class Base {
    private :
            virtual void f() { cout << "Base::f" << endl; }
};

class Derive : public Base{
};

typedef void (*Fun)( void );

void main() {
    Derive d;
    Fun   pFun = (Fun)*(( int *)*( int *)(&d)+ 0 );
    pFun();
}
```

