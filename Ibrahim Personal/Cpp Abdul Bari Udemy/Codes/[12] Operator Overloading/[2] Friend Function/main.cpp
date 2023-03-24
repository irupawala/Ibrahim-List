#include <iostream>

using namespace std;

class complex
{

private:

    int real;
    int img;


public:

    complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }

    void Display()
    {

        cout << real << " +i" << img << endl;
    }

    friend complex operator+(complex c1, complex c2);

};

   complex operator+(complex c1, complex c2)
    {
        complex temp;
        temp.real = c1.real + c2.real;
        temp.img = c1.img + c2.img;
        return temp;
    }

int main()
{

    complex c1(5,3), c2(10,5), c3;
    //c3=c1.add(c2);
    //c3=c2.add(c1);
    c3 = c1+c2;
    c3.Display();
    //cout << c3.real<<"+i"<<c3.img<<endl;
    //cout << "Hello world!" << endl;
    return 0;
}
