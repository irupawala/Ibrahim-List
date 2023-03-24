#include <iostream>

using namespace std;

int main()
{
    string name;

    cout << "Please enter your name ";
    //cin >> name; // This will display only one word and not the contents after the space
    getline(cin, name);
    cout << "Welcome to C++ " << name;

    return 0;
}
