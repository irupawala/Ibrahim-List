#include <iostream>

using namespace std;


class rectangle
{
    private:
    int length;
    int breadth;

	public:

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

rectangle r;
r.setLength(10);
r.setBreadth(-5);
cout<<r.area() << endl; // hence now the area will be 0

cout << "length is " << r.getLength() << endl;

    return 0;
}
