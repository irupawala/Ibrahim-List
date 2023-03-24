

#include <iostream>

using namespace std;

class stack
{
private:
    int *stk;
    int top;
    int size;
public:
    stack(int sz)
    {
        size = sz;
        top = -1;
        stk = new int[size];
    }
    void push(int x);
    int pop();
};

void stack::push(int x)
{
    if(top==size-1)
        cout << "Stack is Full";
    else
    {
    top++;
    stk[top] = x;
    }
}

int stack::pop()
{
    int x = 0;
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

int main##()
{
    stack s(4);
    s.push(0);
    s.push(1);
    s.push(2);
    s.push(3);
    s.pop();
    s.pop();
    s.pop();

    return 0;
}
