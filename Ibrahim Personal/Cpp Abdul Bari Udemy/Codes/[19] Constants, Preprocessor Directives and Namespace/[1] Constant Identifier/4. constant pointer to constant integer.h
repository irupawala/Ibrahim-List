#include <iostream>

using namespace std;

int main()
{
int x = 10;
const int * const ptr = &x;

int y=20;
//ptr=&y; // now pointer itself is constant hence now it cannot be moved to some other variable

//++ *ptr; // note how the integer even can't be modified now


cout << * ptr << endl;
}
