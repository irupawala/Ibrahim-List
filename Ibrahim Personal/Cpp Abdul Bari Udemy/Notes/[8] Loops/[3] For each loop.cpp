#include <iostream>

using namespace std;

int main()

{

    int A[] = {8, 6, 3, 9, 7, 4};

    cout << "Displaying the incremented values and also storing it." << endl;


    for (int &x: A)
        {
        cout << ++x << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}


    cout << "Displaying the original values but storing incremented." << endl;

    for (int &x: A)
        {
        cout << x++ << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}

    // Displaying A

     cout << "Displaying A" << endl;

    for (int x: A)
        {
        cout << x << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}


    return 0;
}


