#include <iostream>

using namespace std;

int main()
{
   // int A[2][3] = {2,3,4,6,3,5};
   int A[2][3] = {};

    for (auto &x:A)
    //* For (int &x:A) // Notice that we cannot use x of type int here because x must be of type "ROW"
    //* Also notice that x is "ROW" hence we have to take it as type reference using "&" or else it will
    // throw compilation error
    //* using reference here x is of type "ROW" of A and y is of type "COLUMN" of x
    //* Note that reference symbol here is a syntax. It won't create a new variable but use the same variable.


    {
        for(auto &y:x )
        {
           cin >> y;
        }

        cout << endl;
    }


    // printing each element of for-each loop

    for (auto &x:A)
    {
        for(auto &y:x )
        {
           cout << y << " ";
        }

        cout << endl;
    }

    return 0;
}
