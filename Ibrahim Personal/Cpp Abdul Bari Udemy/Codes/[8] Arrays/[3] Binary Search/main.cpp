/*

- Binary Search are faster then Linear search because it involves less number of reads.
- Binary search can be used only if numbers are in ascending or descending order
- Look for this video: https://www.udemy.com/cpp-deep-dive/learn/lecture/13851246
- Linear search takes time of order N: O(N)
- Binary search takes less time then linear of order logN. N: O(logN)

*/


#include <iostream>

using namespace std;

int main()
{
    int n, i, key, l, m, h;
    cout << "Enter the number of elements: " ;
    cin >> n ;

    // Enter the Array
    int A[n];
    cout << "Enter the elements in an Array: " << endl;
    for (i=0; i<n; i++)
        cin >> A[i];

    // Enter the key
    cout << "Enter Key: ";
    cin >> key;

    // Binary search

    l = 0;
    h = n;

    while (l <= h)
    {
        m = (l + h)/2;


        if (A[m] < key)
        {
            l = m+1;
        }
        else
        {
            h = m-1;
        }

        if (A[m] == key)
        {
            cout << "Key Found: " << A[m] << endl;
            return 0;

        }



    }

        cout << "Key Not found" << endl;

}
