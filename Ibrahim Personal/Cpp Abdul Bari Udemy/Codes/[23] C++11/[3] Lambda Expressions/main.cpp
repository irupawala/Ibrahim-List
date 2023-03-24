#include <iostream>

using namespace std;

template <typename T>
void fun (T p)
{
    cout << "Value returned from a function" << endl;
    p();
}

int main()
{
    /////////////////////////////////////////////////////////////////////////
    [](){cout<<"Hello" << endl;}(); // The () in the end is for calling this function

    /////////////////////////////////////////////////////////////////////////
    [](int x, int y){cout << "Sum: " << x+y << endl;}(10,5);

    /////////////////////////////////////////////////////////////////////////
    int x = [](int x, int y){return x+y;} (10, 5);
    cout << x << endl;

    /////////////////////////////////////////////////////////////////////////
    auto f = [](){cout << "Hello" << endl;};
    f();

    /////////////////////////////////////////////////////////////////////////
    int s=[](int x, int y) -> int{return x+y;}(10, 5);
    cout << s << endl;

    /////////////////////////////////////////////////////////////////////////
    int a = 320;
    int b = 5;
    [a, b] () {cout << a << " " << b << endl;}(); // notice a and b in capture list

//    [a, b] () {cout << ++a << " " << ++b;}(); // This cannot be done as captured variables cannot be modified.

    [&a, &b] () {cout << ++a << " " << ++b << endl;}(); // By creating a reference now we can modify the values

    /////////////////////////////////////////////////////////////////////////
    // Unnamed function can also be passed to other function as an argument

    int k=10;
    auto fk = [&k](){cout << ++k << endl;}; //
    fun(fk);
    fun(fk);
    fun(fk);

    return 0;
}
