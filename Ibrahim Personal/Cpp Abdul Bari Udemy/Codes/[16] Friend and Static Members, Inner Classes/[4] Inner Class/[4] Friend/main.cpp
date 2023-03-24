#include <iostream>

using namespace std;

class outer
{

public:
    int a=10;
    static int b;

    void fun()
    {
    i.show(); // accessing show function of the inner class
    cout << i.x; // accessing x of the inner class
    }


class inner{
public:
    int x=25;
    void show()
    {
     cout << b << endl;   // static int of the outer class accessible inside the inner class
    }


    };

    inner i; // creating an object of the inner class

};

int outer::b=20;

int main()
{
    outer::inner j; // creating instance of the inner nested class of the outer class
    j.show();
    cout << j.x << endl;
    return 0;


}

