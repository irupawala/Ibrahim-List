# [21] IO Streams

## [21.1] Streams

- Stream is a flow of data or flow of character.
- Streams are used for accessing the data from outside the program like external sources to destination
- E.g. program accesses to keyboard, monitor, file, Network
- For input/ output stream there is build-in class available called **iostream**. From this the classes are 
coming out like **istream and ostream**.
- For file access there are classes like **ifstream(input file stream) and ofstream**
- cin and cout are objects of istream and ostream respectively.
- Also we can OVERLOAD insertion and extraction operator (<< and >>).
- We can use same insertion and extraction operator to access file in c++

## [21.2] Writing to a file

- We have to use fstream for files 
- If the file doesn't exist then new file will be created
- The contents will be truncated if the file already exists 
- If we want to append instead of truncating use `ofstream outfile("Mytxt", ios::app)`
- If we want to truncate then `ofstream outfile("Mytxt", ios::trunc)`
- By Default it is truncate, `ofstream outfile("Mytxt")`

- It is necessary to close the file, because when program is not running resources should be released.

```c++
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    ofstream outfile("My.txt");
    outfile << "Hello" << endl;
    outfile << 25 << endl;
    outfile.close();
    return 0;
}
```

## [21.3] Reading a file

- we are using ifstream here hence we are using the code for reading only
- Notice that for reading the file you have to know in which order the files are kept.
- Hence there are pre-defined way of writing the file like jpg, pdf, etc. These are called as **FILE FORMAT.**

- If we want to mention whether to read or write then there are flags/ modes available 
like ios::in, ios::out

```c++

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    // ifstream infile("My.txt");
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
```

* I/O Streams are used for input and output data to and from the program
* C++ provides class for accessing input output operations
* Iostream is a base class for all classes
* Istream is for input 
* Cin is the object of istream
* ostream is for output
* Cout is an object of ostream
* ifstream is a file input stream
* ofstream is a file output stream

```c++
//Writing in a File 
int main()
{
    ofstream of("Test.txt",ios::trunc);
    of<<"John"<<endl;
    of<<25<<endl;
    of<<"CS"<<endl;
    of.close();
}

//Reading from File
int main()
{
    ifstream ifs("Test.txt");
    string name;
    int roll;
    string branch;
    ifs>>name>>roll>>branch;
    cout<<name<<endl<<roll<<endl<<branch<<endl;
    ifs.close();
}
```

## [21.4] Serialization

Note that in this example the main objective is to overload the insertion and extraction operator.
This is because when we want to write the members of the objects of the class to a file we want that all the 
members of the object are written by calling extraction operator.

### [1] Storing state of object

* This program demonstrates storing the state of the object

```c++
#include <iostream>
#include <fstream>

using namespace std;

class Student
{
private:
    string name;
    int roll;
    string branch;

public:
    Student() {}
    Student(string n, int r, string b)
    {
        name = n;
        roll = r;
        branch = b;
    }
    friend ofstream & operator<<(ofstream &ofs, Student &s);
    
};


ofstream & operator<<(ofstream &ofs, Student &s)
{
    ofs<<s.name<<endl;
    ofs<<s.roll<< endl;
    ofs<<s.branch<<endl;
    return ofs;
}

int main()
{
    Student s ("John", 10, "cs");
    ofstream ofs("Student.txt");
    ofs << s1;
    ofs.close();

    /*
    ofs<<s.name<<endl;
    ofs<<s.roll<< endl;
    ofs<<s.branch<<endl;
    */

    // Instead of this can we write ofs << s1 and complete object is returned.
	// Hence it is possible to store the state of the object and retrieve the state of the object
    // To do this we have to overload the insertion operator << in the student class
    return 0;
}
```

### [2] Retrieving state of object

* This program demonstrates retrieving the state of the object

```c++

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
```

### [3] Storing and retrieving combined

* This program demonstrates complete storing and retrieving state of the object

```c++
class Student
{
private:
     string name;
     int roll;
     string branch;
public:
     Student(){}
     Student(string n,int r,string b)
     {
         name=n;
         roll=r;
         branch=b;
     }
     friend ofstream & operator<<(ofstream &ofs,Student s);
     friend ifstream & operator>>(ifstream &ifs,Student &s);
     friend ostream & operator<<(ostream &os,Student &s);
};

ofstream & operator<<(ofstream &ofs,Student s)
{
     ofs<<s.name<<endl;
     ofs<<s.roll<<endl;
     ofs<<s.branch<<endl;
     return ofs;
}

ifstream & operator>>(ifstream &ifs,Student &s)
{
     ifs>>s.name;
     ifs>>s.roll;
     ifs>>s.branch;
     return ifs;
}

ostream & operator<<(ostream &os,Student &s)
{
     os<<"Name "<<s.name<<endl;
     os<<"Roll "<<s.roll<<endl;
     os<<"Branch "<<s.branch<<endl;
     return os;
}

int main()
{
     ofstream ofs("Test.txt");
     Student s1("John",10,"CS");
     ofs<<s1;
     ofs.close();
     Student s2;
     ifstream ifs("Test.txt");
     ifs>>s1;
     cout<<s1;

} 
```

## [21.5] Text and Binary File

- When you open a text file in any program like notepad then the program first converts the binary 
numbers to ASCII codes and then displays the characters on screen

- To read the binary file in C++ you have to use the mode ios::binary. Also there are different functions like read() and write().

- Binary files are faster and takes less space then the text file

## [21.6] Manipulators

- Manipulators are used for manipulating or formatting streams.

E.g 1:

- `cout << endl;` // can also be written as cout << "\n";

- similarly we can also use the manipulators for int like hex, oct, dec

E.g 2:

* `cout << hex << 163` // hence A3 will be displayed

- We also have manipulators for float like fixed and scientific

E.g 3:

* There are other manipulators also like set() (sets some amount of space for displaying data)
* `cout << set(10) << "Hello"` // This reserves 10 spaces for hello even though it is only 4 alphabets long

E.g 4:

* There are also other manipulators like left, right, ws, etc. left and right are shift left and right

- ws is for white space
- `cout << 10 << ws << 20;` // 10 and 20 are shown with a space 

