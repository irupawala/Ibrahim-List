#include <iostream>

using namespace std;

int main()
{
    int num, r, sum = 0;
    cout << "Enter a number: " ;
    cin >> num;

    while (num != 0)
    {
        r = num%10;
        num = num/10;
        sum = sum * 10 + r;
    }

    cout << "reverse of a num is: " << sum << endl;
}
