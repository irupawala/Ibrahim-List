#include <iostream>

using namespace std;

int main()
{
    int *p = new int[20];



    delete []p; // Always delete the older array in heap before declaring the
    // new array pointed by the same pointer p or else it will result in memory leak.


    p = new int[40]; // here now using the same pointer we have
    // created a new array of larger size 40.
    // This is the advantage of having a heap or dynamically creating a memory


    return 0;
}
