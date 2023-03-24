#include <iostream>

using namespace std;

int main()
{
    int A[] = {6,7,1,2,5,9, 89} , max, i;
    //max = A[0]; // never take max no as 0 because what if all the numbers are negative
    //max = INT_MIN; // or else we can also take INT_MIN
    max = INT_MAX; // for getting the min number from an array

    for (i=1; i<= sizeof(A)/sizeof(A[0]); i++)
    {
        //if (A[i] > max)
        if (A[i] < max) // for finding the min number of an array
        max = A[i];

    }

    cout << "Max of an array is: " << max << endl;



}
