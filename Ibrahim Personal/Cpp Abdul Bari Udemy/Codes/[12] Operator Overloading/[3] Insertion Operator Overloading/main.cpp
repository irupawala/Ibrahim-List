/*
#include <iostream>

using namespace std;

class complex{
private:

int real;
int img;

public:

    complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }


 friend ostream & operator<< (ostream &out, complex &c1);
};


ostream & operator<< (ostream &out, complex &c1)
{
out << c1.real << "+i" << c1.img << endl;
return out;
}

int main()
{
    complex c1(3,7);
    cout << c1<< endl;
    operator<<(cout, c1) << endl;
    // function is called something like this operator<<(cout, c);
    return 0;
}

*/










// SAME OPERATOR OVERLOADING WORKS IF RETURN TYPE IS VOID BUT THEN WE CAN JUST WRITE cout << c1; and not cout << c1<< endl;
// or cout << c1 << c2 << endl; because cout << c1<< endl; with return type as ostream is just like cout << endl;
// as cout is return type again while with void nothing is returned so cout << endl does not get executed

#include <iostream>

using namespace std;

class complex{
private:

int real;
int img;

public:

    complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }


 friend void operator<< (ostream &out, complex &c1);
};


void  operator<< (ostream &out, complex &c1)
{
out << c1.real << "+i" << c1.img << endl;
//return out;
}

int main()
{
    complex c1(3,7);
    cout << c1;
    //cout << c1<< endl; // This  won't work
    // cout << c1 << c2 << endl; // This  won't work

    return 0;
}
