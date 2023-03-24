#include <iostream>

using namespace std;

// HOW TO WRITE A COMPLETE PERFECT CLASS

class rectangle

{
private:
    int length;
    int breadth;

public:
    rectangle (); // Constructors
    rectangle (int l, int b);
    rectangle (rectangle &r); // Constructors
    void setLength(); // Accessors
    void setBreadth(); // Accessors
    int getLength(); // Mutators
    int getBreadth(); // Mutators
    int area(); // Facilitators
    int perimeter(); // Facilitators
    int isSquare(); // enquiry / Inspector // will check whether it is a square or not. Can be int or bool
    ~rectangle(); // Destructor

};

// Note that we never write the functions inside. We just write header or prototype.
// Functions are written outside the class by using SCOPE RESOLUTION OPERATOR





int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
