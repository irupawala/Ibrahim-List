#include <iostream>

using namespace std;

class Demo
{
public:
    int x = 10;
    int y = 20;
    void Display() const
    {
       // x++; // note how we are not able to modify the data members of the class
        cout << x <<" " << y << endl;
    }
};

int main()
{
Demo d;
d.Display();
}
