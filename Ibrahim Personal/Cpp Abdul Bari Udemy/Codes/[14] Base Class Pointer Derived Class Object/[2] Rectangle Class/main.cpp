#include <iostream>

using namespace std;


class Rectangle
{
    public:
    void area()
    {
        cout << "Area of rectangle" << endl;

    }

};

class cuboid: public Rectangle{
    public:
    void volume()
    {

    cout << "Volume of rectangle" << endl;
    }
};
int main()


{

    Rectangle *p;
    cuboid d;
    p = &d;
    p->area();
   // p->volume();

    return 0;
}
