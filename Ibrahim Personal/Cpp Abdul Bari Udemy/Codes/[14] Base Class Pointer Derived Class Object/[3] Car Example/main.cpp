#include <iostream>

using namespace std;

class BasicCar
{
public:
    void start()
    {

        cout << "Car Started";
    }
};

class AdvanceCar: public BasicCar
{
public:
    void playMusic()
    {

        cout << "Music Playing" << endl;
    }
};


int main()
{
    AdvanceCar a;
    BasicCar *p = &a;
//    p->playMusic();
    p->start();

    /*
    BasicCar b;
    AdvanceCar *q=&b;
    */

    //cout << "Hello world!" << endl;
    return 0;
}
