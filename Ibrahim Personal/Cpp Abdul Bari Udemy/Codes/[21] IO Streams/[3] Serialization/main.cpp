#include <iostream>
#include <fstream>

using namespace std;

class Student
{
public:
    string name;
    int roll;
    string branch;


    Student() {}
    Student(string n, int r, string b)
    {
        name = n;
        roll = r;
        branch = b;
    }

    friend ofstream & operator<<(ofstream &ofs, Student &s);
    friend ifstream & operator>>(ofstream &ifs, Student &s);

};



ofstream & operator<<(ofstream &ofs, Student &s)
{
    ofs<<s.name<<endl;
    ofs<<s.roll<< endl;
    ofs<<s.branch<<endl;
    return ofs;
}

ifstream & operator>>(ifstream &ifs, Student &s) //note that data of the file will get read to student object reference &s
{
    ifs >> s.name >> s.roll >> s.branch;
    return ifs;
}



int main()
{
    Student s;

    ifstream ifs("Student.txt");
    ifs >> s;

    cout << "Name " << s.name << endl;
    cout << "Roll " << s.roll << endl;
    cout << "Branch " << s.branch << endl;
    ifs.close();


    return 0;
}
