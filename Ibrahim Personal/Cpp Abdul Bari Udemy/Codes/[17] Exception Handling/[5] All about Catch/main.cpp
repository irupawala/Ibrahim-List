#include <iostream>

using namespace std;

class MyException1: exception{
};

class MyException2: public MyException1
{

};

int main()
{

    try
    {
        throw (MyException1());

    }

    catch(MyException2 e) // Note here that MyException2 should be written before MyException1
    {                     // This is because if you write parent class first then it can handle child class itself
                          // Make MyException1 first and try it out
        cout << "Catch " << endl;
    }

    catch(MyException1 e)
    {
        cout << "Catch " << endl;
    }

    catch(int e)
    {
        cout << "Int Catch " << e << endl;
    }

    catch(double e)
    {
        cout << "Double Catch " << e << endl;
    }

    catch(...) // Ellipse. // Catch all handler must come last
    {
        cout << "All Catch" << endl;
    }
    return 0;
}
