#include <iostream>

using namespace std;

int main()
{
    int m, n;
    cout << "Enter the two input numbers: " << endl;
    cin >> m >> n;

    while (m != n)
    {
        if (m>n)
            m = m-n;
        else if (n>m)
            n = n-m;
    }

    cout << "GCD of a num is: " << n;
}
