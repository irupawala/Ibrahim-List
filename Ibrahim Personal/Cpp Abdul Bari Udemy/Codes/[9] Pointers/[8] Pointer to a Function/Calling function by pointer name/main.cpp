#include <iostream>

using namespace std;

void display(int x)
{
    cout << "Value" << endl;
    cout << x << endl;
}

int main()
{
    /*Call by Function Name*/
    display(2);

    /*Call by Pointer Name*/

    // Function Declaration
    void (*fp) (int); // Declaration syntax is (return type)(name of the pointer, fp is function pointer) (parameters)


    // Pointer Initialization
    //fp = &display; // this will assign the address of the function to this pointer.
    fp = display; // This is allowed too

    // Function call
    //(*fp)(2);
    fp(2); // This is allowed too

    return 0;
}
