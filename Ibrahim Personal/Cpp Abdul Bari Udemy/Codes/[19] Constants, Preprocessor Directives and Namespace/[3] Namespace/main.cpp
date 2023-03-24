#include <iostream>

using namespace std;

namespace First
{
  void fun()
{
    cout << "First" << endl;

}
}


namespace Second
{
  void fun()
{
    cout << "Second" << endl;
}
}

using namespace Second; // It is recommended to avoid these type of statements
int main()
{
    fun();
    First::fun();
    std::cout << "Hello" << endl;

    return 0;
}
