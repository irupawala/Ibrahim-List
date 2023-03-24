#include <iostream>

using namespace std;

int main()
{
    int a=10;
    int *p=&a;

    int A[]={1,2,3,4,5};
    int *q = A; // here we have not written &A because when we write A
    // &A[0] is automatically assigned to q
    // int *q = &A[3] // this is also allowed as we are storing address of integer at A[3]

    cout << a << endl;
    cout << &a << endl;
    cout << p << endl;
    cout << &p << endl;
    cout << *p << endl;

    q = q+1;
    cout <<"Elements of A: " << *q << endl;

    q = q+3;
    cout <<"Elements of A: " << *q << endl;

    cout <<"Elements of A: " << q[-4] << endl;

    return 0;
}
