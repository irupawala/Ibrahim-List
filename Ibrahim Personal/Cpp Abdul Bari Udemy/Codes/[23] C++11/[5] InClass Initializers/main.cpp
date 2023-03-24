#include <iostream>

using namespace std;

class Test
{
    int x=10; // notice how we are assigning values here directly to the members of the class
    int y=13;

public:

    Test(int a, int b)
    {
        x=a;
        y=b;
    }

    Test():Test(1,1) // This is Delegation of a constructor where one constructor can call another in the same class
    {}
};

int main()
{
   // cout << "Hello world!" << endl;
    return 0;
}
