#include <iostream>

using namespace std;

class complex
{
public:

    int real;
    int img;


    complex(int r=0, int i=0)
        {

        real = r;
        img = i;

        }


   // complex add(complex c)
   complex operator+(complex c)
    {
        complex temp;
        temp.real = real + c.real;
        temp.img = img + c.img;
        return temp;
    }
};

int main()
{

   // complex c1, c2, c3;
   // c1.real=5; c1.img=3;
   // c2.real=10; c2.img=5;

   complex c1 (5, 3);
   complex c2 (10, 5);
   complex c3;

    //c3=c1.add(c2);
    //c3=c2.add(c1);
    c3=c1.operator+(c2);
    //c3 = c1+c2;
    cout << c3.real<<"+i"<<c3.img<<endl;
    //cout << "Hello world!" << endl;
    return 0;
}
