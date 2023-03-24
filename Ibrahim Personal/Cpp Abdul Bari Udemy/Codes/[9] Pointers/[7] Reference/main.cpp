#include <iostream>

using namespace std;

int main()
{
    int x=10;
    int &y=x; // you have to initialize the reference while declaring it. Or else it will give compilation error

    int b=10;
    //int &y=b; // Also same reference name cannot be reassigned

    cout <<x << endl;

    y++;
    x++;

    cout << x << endl;
    cout << &x << " " << &y << endl;
    return 0;
}
