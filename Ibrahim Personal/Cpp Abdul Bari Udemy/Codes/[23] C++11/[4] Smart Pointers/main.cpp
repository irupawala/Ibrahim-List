#include <iostream>
#include <memory>


using namespace std;


class Rectangle
{
    int length;
    int breadth;

public:

    Rectangle(int l, int b)
    {

        length = l;
        breadth = b;
    }

    int area()
    {
        return length * breadth;
    }
};

int main()
{

    cout << "------------ unique_ptr ---------------" << endl;

    unique_ptr <Rectangle> ptr (new Rectangle(10, 5));
    cout << ptr->area() << endl;

    // unique_ptr <Rectangle> ptr = ptr2 ; // notice here that another pointer cannot be pointed to the object

    unique_ptr <Rectangle> ptr2;
    ptr2=move(ptr);
    cout << "ptr2 " << ptr2-> area() << endl;
    //cout << ptr->area() << endl; // notice how this doesn't prints anything as the pointer is null


    cout << "------------ shared_ptr ---------------" << endl;

    shared_ptr <Rectangle> ptr3 (new Rectangle(10, 5));
    cout << ptr3->area() << endl;

    shared_ptr <Rectangle> ptr4;


    ptr4=ptr3;
    cout << "ptr4 " << ptr4-> area() << endl;
    cout << "ptr3 " << ptr3->area() << endl;

    cout << ptr3.use_count()<< endl;
    return 0;




}
