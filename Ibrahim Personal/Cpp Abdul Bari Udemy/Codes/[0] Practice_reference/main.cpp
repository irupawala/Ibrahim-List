# include <iostream>

using namespace std;

class car
{
public:
    virtual void start() = 0;
    virtual void stop() = 0;
};

class Innova: public car
{
public:
    void start()
    {
        cout << "Innova Started" << endl;
    }
    void stop()
    {
        cout << "Innova Stopped" << endl;
    }
};

class Swift: public car
{
public:
    void start()
    {
        cout << "Swift Started" << endl;
    }
    void stop()
    {
        cout << "Swift Stopped" << endl;
    }
};

int main()
{
    Car *c = new Innova();
    c -> start();

    c = new Swift();
    c -> start();

    return 0;
}
int main()
{
   return 0;
}

