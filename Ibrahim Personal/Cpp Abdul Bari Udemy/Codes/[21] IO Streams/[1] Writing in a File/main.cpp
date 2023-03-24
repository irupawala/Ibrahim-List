#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    //ofstream outfile("My.txt");
//ofstream outfile("My.txt", ios::trunc);
    ofstream outfile("My.txt", ios::app);
    outfile << "Hello" << endl;
    outfile << 25 << endl;
    outfile.close();
    return 0;
}
