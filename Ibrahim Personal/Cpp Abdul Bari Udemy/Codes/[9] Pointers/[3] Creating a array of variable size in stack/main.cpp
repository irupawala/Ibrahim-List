#include <iostream>

using namespace std;

int main()
{
    int size;
    cout << "Enter number of elements";
    cin >> size;
    int A[size];

    cout << sizeof(A) << endl;
    // This array A is created inside stack
    // Now if we want to change the size of this array using the command
    // below then it is not possible, there is no such syntax in c++

    //size = 35; This cannot be done
    //A[size];

    // But this can be done using heap by creating a dynamic array in heap
    return 0;
}
