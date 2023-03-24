#include <iostream>

using namespace std;

class Innova
{
public:
   static int price;

   Innova()
    {
        price++;
    }

   static int getPrice()
    {
        return price;
    }
};

int Innova::price=20;

int main()
{
    cout << Innova::getPrice() << endl; //getting price without creating an object (that is upon class). that is without buying a car
    Innova my;
    cout << my.getPrice(); // getting price upon object. That is purchasing a car and then knowing the price
    //cout << "Hello world!" << endl;
    return 0;
}
