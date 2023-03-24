#include <iostream>

using namespace std;

int main()
{
    int A[5]= {1,2,3,4,5};
    int *p=A;

    cout << *p << endl;
    p++;
    cout << *p << endl;
    p--;
    cout << *p << endl;


    // observing the addresses

    cout << p << endl;
    p = p+2;
    cout << p[-2] << endl; // This is because c standard defines [] operator as a[b] = *(a+b)
    return 0;
}
