#include <iostream>

using namespace std;

int main()
{
    int A[5]{1,2,3,4,5};
    int *p = A;



    for (int i=0; i<5; i++)
    {
        //cout << A[i] << endl;
        //cout << i[A] << endl;
        cout << p+i << endl;
        cout << (i+A) << endl;
        cout << *(i+p) << endl;
        cout << *(i+A) << endl;


    }

        cout << "Starting address ";
        cout << p << endl;


        for (int i=0; i<5; i++)
    {

        cout << *p << endl;
        p++;

    }
        cout << "Ending address ";
        cout << p << endl;


    return 0;
}
