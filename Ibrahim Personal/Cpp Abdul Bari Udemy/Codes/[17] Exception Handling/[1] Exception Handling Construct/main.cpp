#include <iostream>

using namespace std;

int main()
{
    int x=10, z;
    //int y=2, // Try changing the value of y and executing the program again to see the difference
    int y=0;

    try
    {
        if (y==0)
            throw 1; // Note that this is like if else statement if condition is met int will be thrown
        z = x/y;
        cout << z << endl;
    }

    catch (int e) // here we have written int because we are throwing an integer
    {
        cout << "Division by zero " << e << endl;
    }

    cout << "Program Ended" << endl; // This will always be executed

    return 0;
}
