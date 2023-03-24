#include <iostream>

using namespace std;


class rectangle
{
    private:
    int length;
    int breadth;

	public:
	    /*
    rectangle()
    {
        length=1;
        breadth=1;
    } */


    rectangle(int l =1, int b =1) // parameterized constructor // we can make this constructor default by having default arguments
    {
       setLength(l); // here to avoid setting the l and b to negative values
       setBreadth(b); // and hence mishandling of the data
    }


    rectangle(rectangle &r)
    {
    length = r.length; // passing the length and breadth of the rectangle into itself
    breadth = r.breadth;

    }

	void setLength(int l)
	{
    if(l>=0)
		length=l;
	else
    {
        cout << "length cannot be -ve, default =0" << endl;
		length=0; // Making default length to 0
    }
	}

	void setBreadth(int b)
	{
    if(b>=0)
		breadth=b;
	else
    {
        cout << "breadth cannot be -ve, default =0" << endl;
		breadth=0; // Making default length to 0
    }

	}

	int getLength()
	{

	return length;
	}

	int getBreadth()
	{

	return breadth;
	}


    int area()
    {
        return length*breadth;
    }

    int perimeter()
    {
        return 2*(length+breadth);
    }
};

//- Hence Now we have to call these functions to set length and breadth


int main()
{

rectangle r; // Note that if we call the constructor without defining any, then the built-in default constructor will be called

//cout << r.length << endl; // Notice that all the constructors will have length and breadth as private as defined hence to
//cout << r.breadth << endl; // access it we  need to accessors and mutators


cout << r.area()<<endl; // The area should be zero as the default constructor defines the default length and breadth to 0

// Now when we define our own non-parametrized default constructor then that will be called if we give parameters


rectangle r1(5, 10);
cout << r1.area() << endl;

// creating the copy of r1
rectangle r2(r1);
cout << r2.area() << endl;




    return 0;
}
