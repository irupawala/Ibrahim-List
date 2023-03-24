#include <iostream>

using namespace std;


class student
{
public:
    int rollno;
    string name;
    static int addminNo;

    student(string n)
    {
        name = n;
        addminNo++;
        rollno = addminNo;

    }

    void display()
    {
        cout << "Name " << name << endl << "Roll " <<rollno << endl;
    }
};

int student::addminNo=0;

int main()
{
    student s1("Ibrahim");
    s1.display();
    student s2("Shawn");
    s2.display();
    student s3("Laidong");
    s3.display();

    cout << "Number of admissions " << student::addminNo << endl;
    //cout << "Hello world!" << endl;
    return 0;
}
