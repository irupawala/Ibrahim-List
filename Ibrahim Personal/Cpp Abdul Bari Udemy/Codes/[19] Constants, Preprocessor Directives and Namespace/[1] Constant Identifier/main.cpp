#include <iostream>

using namespace std;

void fun(int const &a, int const &b) // to avoid function modifying the value of integers in the function we can declare it constant
{

    cout << a << " " << b << endl;
    a++;
}

int main()
{

    int x=10;
    int y=20;

    fun(x, y);
    cout << "Main " << x << " " << y << endl; // note how x is modified by a which shouldn't happen
}
