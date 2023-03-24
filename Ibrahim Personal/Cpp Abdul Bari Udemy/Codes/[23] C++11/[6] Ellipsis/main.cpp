#include <iostream>
#include <stdarg.h>


using namespace std;


int sum(int n, ...)
{
    va_list list; // For taking list type of object
    va_start (list, n); // va_start is for getting variable number of arguments inside a variable list
                        // and also getting the total number of arguments

    int s=0;
    int x;
    for(int i=0; i<n; i++)
    {
        x=va_arg(list, int); // for getting an argument of defined type
        s+=x;
    }

    va_end(list);

    return s;
}
int main()
{
    //cout << "Hello world!" << endl;
    cout << sum(3, 10, 20, 30) << endl;
    cout << sum(5, 10, 20, 30, 1 , 2) << endl;
    return 0;
}
