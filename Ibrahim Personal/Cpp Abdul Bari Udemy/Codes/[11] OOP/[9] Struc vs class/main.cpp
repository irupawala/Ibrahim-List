#include <iostream>

using namespace std;

struct Demo
{
    int x;
    int y;

    void Display()
    {
        cout << x <<" "<< y << endl;

    }



};


int main()
{
    Demo D;
    D.x = 10;
    D.y = 15;
    D.Display();

    return 0;
}

// Difference between struc and class

/*
- In C the struc can only have data while in C++ the struc can have class as well as data.
- In C++ the struc looks exactly similar to class

1. In Struc by default everything is PUBLIC while in class by default everything is PRIVATE.


