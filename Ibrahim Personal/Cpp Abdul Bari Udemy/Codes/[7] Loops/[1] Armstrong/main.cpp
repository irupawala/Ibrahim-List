# include <iostream>
# include <cmath>

using namespace std;

int main()
{
    int num, rem, sum=0;
    cout << "Enter a number: " ;
    cin >> num;


    while(num != 0)
    {
        rem = num%10;
        num /= 10;
        sum += (rem*rem*rem);
        cout << rem << endl;
    }
    cout << "sum is " << sum << endl;




    return 0;
}
