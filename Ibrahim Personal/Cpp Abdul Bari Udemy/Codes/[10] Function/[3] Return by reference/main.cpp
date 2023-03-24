#include <iostream>

using namespace std;

int & fun(int & x)
{
   // int x=10;
   // return x; // returning reference of local variable not allowed as it will be deleted after function ends

    return x;


}

int main()
{
    int a = 10;
    fun(a); // here function becomes reference to a. hence we can assign value to fun(a)=25 and it will be stored in a
    fun(a)=25;
    cout<<a<<endl;
    return 0;
}
