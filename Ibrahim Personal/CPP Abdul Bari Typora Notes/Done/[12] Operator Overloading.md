## [12] Operator Overloading

## [12.1] Introduction

- There are various operators available in C++ like +, ++, (), new, delete.

- All this operators except some can also be used for user defined classes. This property is known as operators overloading.

- Let us look an example where we will write a function to add complex numbers using + overloading

  ```c++
  #include <iostream>
  
  using namespace std;
  
  class complex
  {
  public:
      
      int real;
      int img;
      
      complex (int r=0, int i=0)
      {
          real = r;
          img = i;
      }
      
      // complex add(complex& x)
      complex operator+(complex& x) // return type and argument type is both complex
      {
          complex temp;
          temp.real = real + x.real; // The real here represents the real of class complex itself
          temp.img = img + x.img; // here the function is called on class c1 hence real and img represents the real and img of class c1
          return temp;
      }
      
  };
  
  
  int main()
  {
  
     complex c1 (5, 3);
     complex c2 (10, 5);
     //complex c3 = c1.add(c2); Conceptually we want to call add member function on c1 class, but instead of add we can have to write operator+, but then the function name will also get changed to operator+ 
     //complex c3 = c1.operator+(c2);
  
     // We can also add it just like we add the two int 
     complex c3 = c1 + c2;
     cout << "Result of the object addition = " << c3.real << " " << c3.img << " " << endl;
     return 0;
  }
  
  ```

## [12.2] Friend Operator Overloading

- In friend operator overloading neither c1 will add nor c2 will as shown in the previous example of operator overloading


- Instead over here 3rd friend function will add the numbers. Hence this function will take the parameters from both the complex numbers c1 and c2

- Notice that this operation is like I am having some money and friend is having some money and a third friend of us is adding the money taking money from each of us individually.

```c++
#include <iostream>

using namespace std;

class complex
{

private:

    int real;
    int img;


public:

    complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }

    void Display()
    {

        cout << real << " +i" << img << endl;
    }

    friend complex operator+(complex c1, complex c2);

};

   complex operator+(complex c1, complex c2)
    {
        complex temp;
        temp.real = c1.real + c2.real;
        temp.img = c1.img + c2.img;
        return temp;
    }

int main()
{

    complex c1(5,3), c2(10,5), c3;
    //c3=c1.add(c2);
    //c3=c2.add(c1);
    c3 = c1+c2;
    c3.Display();
    //cout << c3.real<<"+i"<<c3.img<<endl;
    //cout << "Hello world!" << endl;
    return 0;
}

```

**NOTICE THAT FRIEND FUNCTION IS WRITTEN OUTSIDE THE CLASS HENCE WITHOUT USING SCOPE RESOLUTION OPERATOR**

* This is because it is completely a independent function which is not a member of the class but a 
  " FRIEND OF THE CLASS". Also note that the way we have overloaded the operator in the previous 
  examples is called as overloading using "MEMBER FUNCTION".

- Hence there are two ways of overloading a function.

1. Member function - function defined inside a class
2. Friend function - function defined outside a class

## [12.3] Insertion and Extraction Operator Overloading [UnImportant]

- Insertion operator is cin and extraction operator is cout. We can also overload these operators

- C++ know how to display int, chars and floats. But it doesn't know how to display user defined objects
like complex objects. Hence we have to write a function for that.

```c++
class complex{

private:

int real;
int img;

public:

void display()
{
cout << real << "+i" << img;
}

complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }
    
};
    
int main()
{
complex c1(3,7);

c1. display(); // This will diplay the complex number 3+i7
    return  0;
}
```

- But we don't want to use display function like this but use it exactly like int, float, etc.

`cout << c1;`

* Hence now we have to overload the insertion operator the same way we have overloaded + operator 
* Hence now we will write the display function something like this

```c++
 friend ostream & operator<< (ostream &o, complex &c1)
 
 // friend because it is taking two arguments
 // cout << c1, insertion operator << takes in two arguments cout (which is ostream) and c1
 // here cout is an argument and not class itself like c1.operator+(c2). also when we write C3 = C1 + C2 then
 // both the C1 and C2 are arguments and + is operator in the same way cout and c1 are arguments
 // here after displaying we want to return back cout so that it can be used in the same line
     
{
o << c1.real << "+i" << c1.img;
}
```

* Writing the complete program again

```c++
class complex{
    
private:

int real;
int img;

public:
    
  complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }  
    
 friend ostream & operator<< (ostream &o, complex &c1);
};


 ostream & operator<< (ostream &o, complex &c1)
{
	o << c1.real << "+i" << c1.img << endl;
     return o;
}



int main()
{
	complex c1(3,7);

	cout << c1 << endl;
	operator<<(cout, c1) << endl; // we can also write something like this
    return 0;
    
}
```



* Same Operator Overloading works if the return type is void but then we can just write `cout << c1; and not cout << c1<< endl;`or `cout << c1 << c2 << endl;` 
* Because `cout << c1<< endl;` with return type as ostream is just like `cout << endl;`as `cout` is return type again while with void nothing is returned so `cout << endl` does not get executed

```c++
#include <iostream>

using namespace std;

class complex{
private:

int real;
int img;

public:

    complex (int real=0, int img = 0)
    {
        this->real = real;
        this->img = img;
    }


 friend void operator<< (ostream &out, complex &c1);
};


void  operator<< (ostream &out, complex &c1)
{
out << c1.real << "+i" << c1.img << endl;
//return out;
}

int main()
{
    complex c1(3,7);
    cout << c1;
    //cout << c1<< endl; // This  won't work
    // cout << c1 << c2 << endl; // This  won't work

    return 0;
}

```

