#include <iostream>

using namespace std;

class rectangle
{
private:

    int length;
    int breadth;

public:

    rectangle(); // constructor
    rectangle(int l, int b);
    rectangle(rectangle &r);
    int getLength() {return length;} // Accessors
    int getBreadth() {return breadth;}
    void setLength(int l); // Mutators
    void setBreadth(int b);
    int area(); // Facilitators
    int perimeter();
    bool isSquare(); // Inspector
    ~rectangle(); // Deallocation of an object // Destructor


};

    rectangle::rectangle()
    {

        length=1;
        breadth=1;
    }

    rectangle::rectangle(int l, int b)
    {

        setLength(l);
        setBreadth(b);
    }

    rectangle::rectangle(rectangle &r)
    {

        length = r.length;
        breadth = r.breadth;
    }

    void rectangle::setLength(int l)
    {

        length = l;
    }

    void rectangle::setBreadth(int b)
    {

        breadth = b;
    }

    int rectangle::area()
    {

        return length*breadth;
    }

    int rectangle::perimeter()
    {

        return 2*(length+breadth);
    }

    bool rectangle::isSquare()
    {

        return length == breadth;
    }

    rectangle::~rectangle()
    {
        cout << "Rectangle Destroyed";
    }



int main()
{

    rectangle r1 (10, 10);
    cout <<"Area "<< r1.area() << endl;

    if(r1.isSquare())
        cout<<"Yes"<<endl;

    return 0;
}


