# [18] Template functions and classes

## [18.1] Template Functions

- Template functions are used for generalization where you can write code for any type of data

```c++
template <class T>

T maximum (T x, T y)
{

return x > y ? x:y;
}

maximum (10, 15);
maximum (12.5, 9.5);
```

- Consider an example where the function can take multiple datatypes arguments from the template

```c++
template <class T, class R>

void add (Tx, Ry)
{
cout << x+y;
}

add(10, 12.9);
```

## [18.2] Template Classes 

- Consider an example of implementing the stack using array which contains a top pointer for pointing 
to a particular index. We also have function for pushing and popping values.

```c++
class stack
{
private:
int s[10];
int top;

public:
void push(int x);
int pop();
};
```

- This stack is only for integer. Hence it cannot take any datatype. Thus we can make class as template
and use it for any datatype

```c++
template <class T>
void stack <T> :: push (T x) // whenever you are using class name you have to write template parameter <T> with it
// This is to because it indicates the type of the class
{
}

template <class T> // note that for implementing each function outside you have to give template everytime
void stack :: pop ()
{
}
```

*  Now when we are creating object of this stack class then we have to mention which datatype it is

```c++
stack <int> s; // 
stack <float> s2; // float stack
```

- In C++ we can create our own user defined classes and functions of type Template (that is generic datatype). This function is not available in java where you cannot define your own template classes but built-in template classes are available.

```c++
#include <iostream>

using namespace std;

template <class T>
class stack
{
private:
    T *stk;
    int top;
    int size;
public:
    stack(int sz)
    {
        size = sz;
        top = -1;
        stk = new T[size];
    }
    void push(T x);
    T pop();
};

template <class T> // notice here whenever new body starts it must be defined as a template
void stack<T>::push(T x)
{
    if(top==size-1)
        cout << "Stack is Full" << endl;
    else
    {
    top++;
    stk[top] = x;
    }
}

template <class T>
T stack<T>::pop()
{
    T x = 0;
    if(top == -1)
        cout << "Stack is Empty" << endl;
    else
    {
        x = stk[top];
        cout << "Item Popped " << x << endl;
        top--;
    }
    return x;
}

int main()
{
    stack <int> s(1); // try changing the stack type to int, float, double, char, etc
    s.push(5);
    s.push(5);
   // s.push(5);

   // s.pop();


    return 0;
}
```

