# [16] Friend and Static Members, Inner Classes

## [16.1] Friend Function

- Static data members are members of a class
- Only one instance of static members is created and shared by all objects
- They can be accessed directly using class name
- Static members functions are functions of a class, they can be called using class name, without 
  creating object of a class.
- They can access only static data members of a class, they cannot access non-static members 
  of a class.
- We know that any function outside the class can only access the public data members of the base class.

```c++
class test
{

private:
	int a;
protected:
	int b;
public:
	int c;
	
friend void fun();
	
};

void fun()
{
Test t;
t.a = 5;
t.b = 10;
t.c = 15;
}
```

* Hence if we want to allow any function outside the class to access all its data members then **we have to declare 
  that function as FRIEND function inside the class AND THE OUTSIDE FUNCTION SHOULD HAVE OBJECT OF THAT CLASS**

* Now this fun() can access all the private, public and protected function of the class **UPON OBJECT**.
  **This is useful in operator overloading.**

  

## [16.2] Friend Class

* Similarly to friend function we have friend class

```c++
class your;

class my
  {
  private:
  int a = 10;

  **friend your;
  };

  class your
  {
  public:
  my m;
  void fun()
  {
  cout << m.a;
  }
  };
```

* Here the class "your" has an object of the class "my" hence it has a "HasA" relationship. Now we want to access the private variable in the "your" class which we cannot access as we know but we can define the "your" class as friend class similarly like friend function and can access the private members of the "your" class **UPON OBJECT.**
* But in C++ the compiler processes each line of code in a sequence. Hence the compiler won't recognize "your" class in the "my" class as "your" class is defined after it.
* Due to this we have to define the your class (JUST DECLARATION AND NOT BODY OF THE CLASS) above My class using the statement `class your;` 
* Also here the your class is a container of the object of the My class hence we call it **CONTAINER CLASS.**

## [16.3] Static Members

- Consider the Class test with a constructor test

```c++
class Test
{

public:
int a;
int b;
static int count; // static member

Test()
{
a=10; 
b=10;
count ++;
}
};

int test::count =0; // count to be used only within the class test hence scope resolution is given. Also notice that the static members has to be defined outside the class ONLY and also notice how the datatype "int" is mentioned again.


main ()
{

Test t1;
Test t2;
cout << t1.count; // accessed using object
cout << t2.count;
cout << Test::count; // accessed using class name
}
```

* Here note that both of these classes will have its own a and b
- But Count will be allocated in the memory only once and will be 
shared by both t1 and t2.
- **HENCE STATIC VARIABLES OR DATA MEMBERS BELONG TO CLASS AND NOT OBJECT
AND ALL THE OBJECTS CAN USE IT. THESE ARE COMMON FOR ALL OBJECTS AND CAN BE SHARED BY ALL THE MEMBERS OF THE CLASS.**
- **Static Variable should also be defined outside the class just like global variables**
**but we want it to be accessed by only test class hence we have to use** 
**scope resolution operator.**
* **In the example above count to be used only within the class test hence scope resolution is given. Also notice that the static member function has to be defined outside the class ONLY and also notice how the datatype "int" is mentioned again.**
- But note here that the count will be incremented both the times the object T1 and T2 are created
hence the final value of count will be 2.

* Also note that the static data members can be accessed using object also
  and can be accessed also using CLASS NAME if they are public as shown below.

`cout << Test::count;`



## [16.4] Static Member Functions

```c++
class Test
{
private:
int a;
int b;


public:
static int count; // static member

Test()
{
a=10; 
b=10;
count++;
}

static int getcount()
{
a++; // Not accessible
return count; // accessible
};

int test::count =0; // count to be used only within the class test hence scope resolution is given

```

* Notice the static int getcount() here which is static members function can only access
  count and not a++. 
* **HENCE STATIC MEMBERS FUNCTIONS CAN ONLY ACCESS STATIC DATA MEMBERS (AND NOT NON STATIC DATA MEMBERS) AND HENCE STATIC MEMBERS FUNCTIONS BELONGS TO A CLASS AND CAN BE CALLED SIMILARLY TO STATIC MEMBERS USING SCOPE RESOLUTION OPERATOR**

```c++
main()
{

cout << test::getcount(); // accessed using class name
Test t1;
cout<<t1.getcount(); // accessed using object
}
```

* These kind of static data members are used when a particular number is to be used over and over again without modifying its value. Consider the example below:

```c++
#include <iostream>

using namespace std;


class student
{
public:
    int rollno;
    string name;
    static int addminNo;

    student(string n)
    {
        name = n;
        addminNo++;
        rollno = addminNo;

    }

    void display()
    {
        cout << "Name " << name << endl << "Roll " <<rollno << endl;
    }
};

int student::addminNo=0;

int main()
{
    student s1("Ibrahim");
    s1.display();
    student s2("Shawn");
    s2.display();
    student s3("Laidong");
    s3.display();

    cout << "Number of admissions " << student::addminNo << endl;
    //cout << "Hello world!" << endl;
    return 0;
}

```

## [16.5] Nested /Inner Class

- Nested Class/ Inner Class is writing a class within another class so that it can be used ONLY within that class.
- This is to reduce the complexity of the big classes.

```c++
#include <iostream>

using namespace std;

class outer
{

public:
    int a=10;
    static int b;

    void fun()
    {
    i.show(); // accessing show function of the inner class
    cout << i.x; // accessing x of the inner class
    }


class inner{
public:
    int x=25;
    void show()
    {
     cout << b << endl;   // static int of the outer class accessible inside the inner class
    }


    };

    inner i; // creating an object of the inner class

};

int outer::b=20;

int main()
{
    outer::inner j; // creating instance of the inner nested class of the outer class
    j.show();
    cout << j.x << endl;
    return 0;


}
```

- Here note that inner class **CANNOT ACCESS ANY MEMBERS OF THE OUTER CLASS BUT ONLY STATIC MEMBERS**
- Also Outer Class can create an object of the inner class and access all the members of the inner class which are declared as public.

