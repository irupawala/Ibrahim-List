#include <iostream>

using namespace std;

//class MyException
class MyException: exception // also see that how we are able to inherit from the built in class exception
{

};


int main()
{
    int x=10, z;
    //int y=2; // Try changing the value of y and executing the program again to see the difference
    int y=0;

    try
    {
        if (y==0)
           // throw 1;
           // throw 1.4;
            throw string ("Div by 0"); // NOTE THE KEYWORD STRING HERE
            //throw MyException();
            throw MyException();

        z = x/y;
        cout << z << endl;
    }

    //catch (int e) // here we have written int because we are throwing an integer
   // catch (double e)
   catch(string e)
   //  catch (MyException e)
    {
        cout << "Division by zero "  << endl;
    }

    cout << "Program Ended" << endl; // This will always be executed

    return 0;
}
