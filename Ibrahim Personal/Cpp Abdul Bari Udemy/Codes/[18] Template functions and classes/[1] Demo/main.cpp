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
