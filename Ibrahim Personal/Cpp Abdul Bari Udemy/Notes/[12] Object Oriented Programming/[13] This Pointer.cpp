#include <iostream>

using namespace std;

class rectangle
{
private:

    int length;
    int breadth;

public:

    rectangle (int length, int breadth)
    {
       // length = length; // Here note that if we assign length argument to the length of the current object
// then the compiler will get confused because of the same name. hence here the local member length will get assigned to
// itself and will never access the length of the object. To refer to the data member of the same class
// or same object This pointer is used. This pointer removes the name ambiguity.

        this->length = length; // this->length refers to data member of the class of the current object
        this->breadth = breadth; // this means r1's length and breadth
    }

    int area()
    {
        return length*breadth;
    }

};

int main()
{

    rectangle r1 (10, 10);
    cout <<"Area "<< r1.area() << endl;

    return 0;
}


