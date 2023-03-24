#include <iostream>

using namespace std;


class Test
{
    int a;
    int *p;

    Test (int x)
    {
        a = x;
        p = new int[a];
    }

    Test (Test &t)
    {
        a = t.a;
        p = t.p;

    }

};

int main()
{

    Test t(5);
    Test t2(t);
    return 0;
}
