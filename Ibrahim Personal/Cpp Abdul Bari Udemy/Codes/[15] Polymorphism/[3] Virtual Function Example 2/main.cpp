#include <iostream>

using namespace std;


class BasicCar
{
public:
    virtual void start()
    {
        cout << "Basic Car started" << endl;
    }
};

class AdvanceCar: public BasicCar
{
public:
    void start()
    {
        cout << "Advance Car started" << endl;
    }

    void stop()
    {
        cout << "Advance Car stopped" << endl;
    }

};
int main()
{

    //BasicCar *p = new AdvanceCar();
    //p->stop(); // Any attempt to use the parent class pointer to call the member function of the subclass that does not override the parent class will be regarded as illegal by the compiler, so such a program cannot be compiled at all.
    //p->start();
    AdvanceCar A;
    BasicCar *bc = &A;
    cout << bc << endl;
    int *b = (int*)(&A);
    cout << b << endl;
    //b->start();

    //cout << "Hello world!" << endl;
    return 0;
}
