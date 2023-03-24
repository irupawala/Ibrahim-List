#include <iostream>

using namespace std;

int main()
{
    int num, r, sum=0;
    cout << "Enter a number: " << endl;
    cin >> num;

    while (num != 0)
    {
        r = num % 10;
        num = num/ 10;
        sum = sum*10 + r;

    }

    //cout << "Reverse of a num is: " << sum << endl;

    cout << "Number is spelled as: ";

    while (sum != 0)
    {
        r = sum % 10;
        sum = sum/ 10;

        switch(r)
        {
            case 0:
                cout << "zero";
                break;

            case 1:
                cout << "one";
                break;

            case 2:
                cout << "two";
                break;

            case 3:
                cout << "three";
                break;

            case 4:
                cout << "four";
                break;

            case 5:
                cout << "five";
                break;

            case 6:
                cout << "six";
                break;

            case 7:
                cout << "seven";
                break;

            case 8:
                cout << "eight";
                break;

            case 9:
                cout << "nine";
                break;
        }
    }


}
