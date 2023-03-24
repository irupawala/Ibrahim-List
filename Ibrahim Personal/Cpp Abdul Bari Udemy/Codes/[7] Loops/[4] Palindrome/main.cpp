#include <iostream>

using namespace std;

int main()
{
    int num, r, sum = 0, original_num;
    cout << "Enter a number: " ;
    cin >> num;
    original_num = num;

    while (num != 0)
    {
        r = num%10;
        num = num/10;
        sum = sum * 10 + r;
    }

    if(sum == original_num)
    {
         cout << "Number is Palindrome" << endl;
    }
    else
    {
        cout << "Not a Palindrome" << endl;
    }

}
