#include <iostream> // library header file

using namespace std; // some built-in function in the header file are grouped under name std. for using that we
                       // have to say using namespace std

int main() // int is return type hence we have to write return 0 in the end
{

    //std::cout << "Hello world!"; // :: is known as scope resolution operator. If we are going to use cout frequently
                                 // it is better to use nampespace

   cout << "Hello world!" ; // cout and cin stands for console operation. << is called insertion operator

   // cout << "Hello world!" ; // Notice that including endl makes the program faster
    return 0;
}
