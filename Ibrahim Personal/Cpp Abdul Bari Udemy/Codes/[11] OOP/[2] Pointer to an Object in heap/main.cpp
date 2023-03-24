#include <iostream>

using namespace std;

class rectangle


{
    public:
    int length ;
    int breadth ;

    int perimeter()
    {
        return 2*(length + breadth);

    }

    int area()
    {
        return length * breadth;

    }

};

int main()
{

    // Object r1 created in stack and pointer q in stack pointing to its address.
    rectangle r1;
    rectangle *q = &r1;
    q->length=2;
    q->breadth=5;
    cout << q->area() << endl;


    // Object rectangle (no name given to it like the r1 rectangle object in stack) created in heap and pointer p in stack pointing to its address
    rectangle *p = new rectangle;
    p->length=2;
    p->breadth=18;
    cout << p->area() << endl;


   // cout << r1.length << endl;
   // cout << p->length << endl;
    return 0;
}
