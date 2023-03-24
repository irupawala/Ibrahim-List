#include <iostream>

using namespace std;

// class MyException
class MyException: exception // also see that how we are able to inherit from the built in class exception
{

};

//int division (int a, int b)throw (MyException)
int division (int a, int b) throw (int)
//int division (int a, int b) throw () // Also notice that you can also mention if you are not throwing anything
{
    if (b == 0)
       // throw MyException();
        throw 10;
    return a/b;
}


int main()
{
    int x=10, z;
    //int y=2, // Try changing the value of y and executing the program again to see the difference
    int y=0;

    try
    {

        z = division(x, y);
        cout << z << endl;
    }

    catch (int e) // here we have written int because we are throwing an integer
   // catch (double e)
    // catch (MyException)
    // catch (MyException e)
    {
        cout << "Division by zero "  << endl;
    }

    cout << "Program Ended" << endl; // This will always be executed

    return 0;
}
