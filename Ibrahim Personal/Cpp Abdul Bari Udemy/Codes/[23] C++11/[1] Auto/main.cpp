#include <iostream>

using namespace std;

float fun()
{
    return 2.34f;
}

int main()
{
    // auto is used when we don't know the type of the data
    auto x  = 2*4.59 + 'a';
    auto y = fun();
    cout << x << endl;
    cout << "Value returned from func " << y << endl;

    // decltype is used in c++ to capture the datatype of one variable and give it to other.

    decltype(y) z = 12.3;

    return 0;
}
