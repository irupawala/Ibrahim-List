#include <iostream>

using namespace std;

int main()
{
//const int x =10;
int x =10;

const int * ptr = &x;

//++*ptr;

cout << * ptr << endl;
}
