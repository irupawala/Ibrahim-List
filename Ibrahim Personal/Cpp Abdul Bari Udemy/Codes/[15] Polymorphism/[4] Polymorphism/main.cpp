#include <iostream>

using namespace std;


class Car
{

public:
    virtual void start() = 0;


    virtual void stop() = 0;

};

class Innova: public Car
{

public:
    void start()
    {
        cout << "Innova Started" << endl;
    }

    void stop()
    {
        cout <<"Innova Stopped" << endl;

    }

};

class Swift: public Car
{

public:
    void start()
    {
        cout << "Shift Started" << endl;
    }

    void stop()
    {
        cout <<"Shift Stopped" << endl;

    }



};
int main()
{
    Car *c = new Innova();
    c -> start(); // here the innova function start will be called
    c = new Swift();
    c -> start(); // here the swift function start will be called
    return 0;
}
