# [17] Exception Handling

## [17.1] Exception Handling Construct and Throw and Catch

* There are three types of errors which can occur in the programming:

1. Syntax Error - Compiler can resolve it, programmer is responsible
2. Logical Error - Debugger can help with it, programmer is responsible
3. Runtime Error - Programmers can help giving a warning, user is responsible

* There are some cause of error during runtime.

1. Bad Input:- eg integer needed but string given
2. Lack of resources:- lack of files, printer, lack of ink, etc

* Runtime error is called as Exception. Programmer must give warnings to the user for not facing runtime error. e.g if there is low fuel in a car or air pressure, warning will be given.

* C++ Compiler does not have capability to throw the exception like java. Hence programmer has to throw the error themselves
* Note here that for throw int in the code, value of int does not have meaning but it can be used to show error code to the user informing the user which type of error it is.

```c++
#include <iostream>

using namespace std;

int main()
{
    int x=10, z;
    //int y=2, // Try changing the value of y and executing the program again to see the difference
    int y=0;

    try
    {
        if (y==0)
            throw 1; // Note that this is like if else statement if condition is met int will be thrown
        z = x/y;
        cout << z << endl;
    }

    catch (int e) // here we have written int because we are throwing an integer
    {
        cout << "Division by zero " << e << endl;
    }

    cout << "Program Ended" << endl; // This will always be executed

    return 0;
}

```

## [17.2] Throw and Catch between functions

-  Now note that the same job could also have been done by if-else statement then what 
is the use of throw and catch ??
- These are used for the functions as functions should either perform the operation in a right way and return the result or else it should throw some errors. consider the code below. Here function division either returns the right answer or else throws an exception.

```c++
#include <iostream>

using namespace std;

int division (int a, int b)
{
    if (b == 0)
        throw 1;
    return a/b;
}

int main()
{
    int x=10, z;
    int y=2; // Try changing the value of y and executing the program again to see the difference
    //int y=0;

    try
    {
        z = division(x, y); // Note that exception is thrown here and then it goes to catch
        cout << z << endl;
    }

    catch (int e)
    {
        cout << "Division by zero " << e << endl;
    }

    cout << "Program Ended" << endl;

    return 0;
}
```

## [17.3] All about throw

```c++
int division (int a, int b)
{
    if (b == 0)
        throw 1;
    return a/b;
}
```

* Note that you can throw int, double, float, string and also object of the class
* Notice though that for throwing string you should write keyword string("MyString") for the throwing
* In the example below also notice how we have thrown unnamed object of the class MyException()

```c++
#include <iostream>

using namespace std;

//class MyException
class MyException: exception // also see that how we are able to inherit from the built in class exception
{

};


int main()
{
    int x=10, z;
    //int y=2; // Try changing the value of y and executing the program again to see the difference
    int y=0;

    try
    {
        if (y==0)
           // throw 1;
           // throw 1.4;
           // throw string ("Div by 0"); // NOTE THE KEYWORD STRING HERE
            //throw MyException();
            throw MyException();

        z = x/y;
        cout << z << endl;
    }

    //catch (int e) // here we have written int because we are throwing an integer
   // catch (double e)
  // catch(string e)
     catch (MyException e)
    {
        cout << "Division by zero "  << endl;
    }

    cout << "Program Ended" << endl; // This will always be executed

    return 0;
}

```

```c++
class MyException
{
};
```

Also note that if you are throwing your own class exception then it is possible  that you can also inherit your class from the buit-in class in C++ called exception

```C++
class MyException: public exception
{
	public:
	char *what() // what is a method. Here you can also over-write this method to return "MyException" as per your need
	{
	return "MyException";
	}

};

```

* ALSO NOTE THAT IF A FUNCTION IS THROWING SOMETHING YOU CAN DECLARE THAT FUNCTION IS THROWING SOMETHING IF YOU LIKE

- For this you have to write throw keyword in the function definition

```c++
int division (int a, int b) throw (MyException)
{
    if (b == 0)
        throw MyException;
    return a/b;
}
```

* If you are throwing int then you should write int, if you are throwing class then you should write built-in
class name in the definition.

```c++
int division (int a, int b) throw (int)
{
    if (b == 0)
        throw 1;
    return a/b;
}
```

* If you are not throwing anything then you can also indicate that by having an empty bracket in the definition followed by throw

```c++
int division (int a, int b) throw ()
{
    return a/b;
}
```

## [17.4] All about Catch

* If there is an exception of type int and float in one TRY block then we can have MULTIPLE CATCH BLOCKS which can take the thrown values as per the datatype

```c++
try
{

}

catch(int e)
{
}

catch(float e)
{
}

catch(MyException e)
{
}
```



* If we don't know what type of exception it is then we can have a CATCH ALL BLOCK WHICH IS ALSO CALLED ELLIPSE

```c++
// Ellipse is defined as below

catch(...) // three dots
{
}
```

* Hence for the datatype for which the catch block is defined the thrown values will go to the corresponding catch blocks. For all other datatypes thrown CATCH ALL will catch it.

* If we are using CATCH ALL block then we are not giving proper message to the user

* ALSO NOTE THAT CATCH ALL BLOCKS MUST BE WRITTEN LAST AFTER ALL THE CATCH BLOCKS

* If Catch All block is written first then all the exception will be handled by it only and no other catch
block after it will be executed

## [17.5] More details about Try Catch

```c++
Try
	{

	Try
		{
		}
	
	catch()
		{
		}
}

catch()
{
}
```

```c++
class MyException1
{
};

class MyException2: public MyException1
{
};

Try{
}

catch(MyException2 e) 	// writing the parent class first is a mistake. Child class should only be first

{
}

catch(MyException1 e)
{
}
```

