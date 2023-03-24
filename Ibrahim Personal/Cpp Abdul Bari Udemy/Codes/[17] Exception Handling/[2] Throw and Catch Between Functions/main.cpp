#include <iostream>

using namespace std;

int division (int a, int b)
{
    if (b == 0)
        throw 1;
    return a/b;
}

int main()
{
    int x=10, z;
    int y=2; // Try changing the value of y and executing the program again to see the difference
    //int y=0;

    try
    {
        z = division(x, y); // Note that exception is thrown here and then it goes to catch
        cout << z << endl;
    }

    catch (int e)
    {
        cout << "Division by zero " << e << endl;
    }

    cout << "Program Ended" << endl;

    return 0;
}
