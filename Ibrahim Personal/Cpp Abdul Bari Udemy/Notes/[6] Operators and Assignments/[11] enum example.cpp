1#include <iostream>

using namespace std;

enum day{mon, tue, wed}; // day is a user-defined datatype which will take the values from
// mon to wed i.e. 0 to 3

int main()
{
    day d; //d ia a variable of type day
    d=tue;
    d = wed;
    // d = 1; This is not allowed
   // mon++;
    cout<<d<<endl;

}
