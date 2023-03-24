#include <iostream>

using namespace std;

int main()
{
    int n, i, key;
    cout << "Enter the number of elements: " ;
    cin >> n ;

    int A[n];
    cout << "Enter the elements in an Array: " << endl;
    for (i=0; i<n; i++)
        cin >> A[i];

    //for (i=0; i<n; i++)
     //   cout << A[i] << endl;

     cout << "Enter Key: ";
     cin >> key;

     for (i=0; i<n; i++)
     {
         if (key==A[i])
         {
            cout << "Key found " << key << endl;
            return 0;
         }

     }
            cout << "Key not found" << endl;


}
