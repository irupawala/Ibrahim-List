#include <iostream>

using namespace std;

class base
{
public:
    int x;
    void Display();

};

class derived:public base
{
public:
    int y;
    void Show()
    {
        cout << "Display of Derived " << y << endl;

    }

};


void base::Display()
{

    cout << "Display of base " << x << endl;
}

int main()
{
     //class base b1;
     class derived d1;
     d1.x = 100;
     d1.y = 50;
     d1.Display();
     d1.Show();



    return 0;
}
