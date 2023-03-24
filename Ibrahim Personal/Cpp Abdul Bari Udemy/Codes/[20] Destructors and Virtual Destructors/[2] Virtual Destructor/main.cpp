#include <iostream>


using namespace std;

class Base
{

public:
	Base()
	{
	cout << "Base constructor" << endl;
	}

	virtual ~Base()
	{
	cout << "Base destructor" << endl;
	}
};

class Derived: public Base
{

public:
	Derived()
	{
	cout << "Derived constructor" << endl;
	}

	~Derived()
	{
	cout << "Derived Destructor" << endl;
	}

};


void fun()
{
    Base *p = new Derived();
    delete p;

}
int main()
{
    fun(); // note here that if we don't declare the constructor of the base class as virtual
    // then only the destructor of the base class will be called
    return 0;
}

