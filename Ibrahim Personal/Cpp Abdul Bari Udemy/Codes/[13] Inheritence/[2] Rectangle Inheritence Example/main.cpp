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

class cuboid: public rectangle
{
private:
    int height;
public:
    int getHeight() {return height;}
    int setHeight(int h) {height = h;}


   // cuboid (int l=0, int b=0, int h=0) : rectangle(l,b)
    cuboid (int l=0, int b=0, int h=0)
    {
        cout << "Derived Constructor" << endl;
        setLength(l);
        setBreadth(b);
        height = h;
    }

        int volume ()
    {

        return getLength() * getBreadth() * h;

    }

};


    rectangle::rectangle()
    {
        cout << "Default Constructor" << endl;
        length=1;
        breadth=1;
    }

    rectangle::rectangle(int l, int b)
    {
        cout << "Param Default Constructor" << endl;
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
    cuboid c(10, 5, 3);
   // c.setLength(2);
   // c.setBreadth(2);

 cout << "Volume " << c.volume() << endl;



    return 0;
}


