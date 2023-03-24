#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //ifstream infile("My.txt");
    // This can also be written as this:

    ifstream infile;
    infile.open("My.txt");

    // Now the file must exist while reading a file
    // Hence we have to check whether the file is open or not


    // if(! infile)
    //     cout << "File cannot be opened" << endl;

    // There is other method of checking whether the file is open or not

    if(infile.is_open())
       cout << "File is open" << endl;



    string str1, str2;
    int x1, x2;
    infile >> str1 >> x1 >> str2 >> x2;

    if(infile.eof()) cout << "End of file is reached";
    infile.close();

    cout << str1 << " " << x1 << endl;
    cout << "Name: " << str2 << " " << "Always "<< x2 << endl;



    return 0;
}
