#include <iostream>

using namespace std;

int main()
{
    int A[5]= {1,2,3,4,5};
    int *p=A, *q=&A[4];

    cout << *p << endl;
    p++;
    cout << *p << endl;
    p--;
    cout << *p << endl;


    // observing the addresses

    cout << p << endl;
    p = p+2;
    cout << p[-2] << endl; // This is because c standard defines [] operator as a[b] = *(a+b)

    cout << "Difference of pointers :" << p-q << endl; // 2 is the number of elements between p and q and -ve tells which elements comes first
    return 0;
}
