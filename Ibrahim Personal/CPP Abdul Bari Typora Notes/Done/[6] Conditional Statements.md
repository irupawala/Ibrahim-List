# [6] Conditional Statements

## [6.1] Simple If-else

```c++
if(roll>0)
     {
     cout<<"Valid Roll No."<<endl;
     }
else
     {
     cout<<"Invalid Roll No."<<endl;
     }
```



## [6.2] Nested If-else

``` c++
if(a>b && a>c)
    {
    cout<<a<<endl;
    }
else if(b>c)
    {
    cout<<b<<endl;
    }
else
    {
    cout<<c<<endl;
    }
```

## [6.3] Short Circuit:

* In the AND condition if one of the inputs is true the output is true

* Similarly in the OR condition if one of the inputs is false the output is false.

* Consider the example below : 

  ```C++
  #include <iostream>
  using namespacestd;
  int main()
  {
  int	a=10,b=5,i=5;
      if(a>b && ++i<=b)
      {
      }
  	cout<<i<<endl;
      if(a<b || ++i<=b)
      {
      }
  	cout<<i<<endl;
  }
  ```

* Here the compiler will only check the first statement and if it is satisfied then the compiler will never go to the second statement. Hence the increment operator in the second part of the if statement will never be executed and hence the output i display will be false.
* This is called as **Short Circuit** in programming and hence the takeaway is one should always avoid increment/ decrement operator or assignment in the second part of the conditional statements.

## [6.4] Dynamic Declaration - Special if statement

* Note that if you define a variable in a function then the memory for that function is allocated dynamically during the function only and removed from the memory once you exit the function

```C++
if ()
{
	int k;
}
```



- Now k will be allocated memory in heap and will removed from heap once you exit the if() function.

* Consider this situation:

```C++
int main()
{

int a,b,c;
int k = exp;

if (k<a)
	{				// now we want the scope of this variable inside the if only
	}

if (int k=exp; k<a) // hence C++17 onwards provides this function to declare the scope just inside this if
	{
	}

}
```



* If you want to limit the scope of any variable then enclose it inside the dummy block { }

```c++
{
int d=a-b;
if(true)
	{
 cout<<d<<endl;
     }
 }
 cout<<d<<endl; // here d won't be accessible here as it's scope has ended in the last bracket

 
```

## [6.5] Switch Statement

- switch is a branch and control statement.

- switch is faster then if-else because unlike if-else it doesn't check all the conditions

- `switch(exp)` --> note that this code exp can be char or int

- **note that in the statement `case 1:` there is a space between case and 1. It will generate wrong results if you don't give this space**

  ```C++
  switch(exp)
  {
  case 1:
  ---
  break;
  
  case 2:
  ---
  break;
  
  default:
  ---
  }
  ```

- default is optional. it won't throw an error if you don't include default. 
- If you give any value in the expression for which there is no case then the default will be executed.
- default can also be written anywhere in the program but if not in end then the break statement has to be included with it.
- Every case block must terminate with break. 
- **If you don't mention break after any case then it will execute that case and the case after that until the break statement is reached. This is called fall through in programming.**
- If int type then cases can be 0,1,2.... If the char type then we have char labels like 'a', 'b', 'c'..... but cases names cannot be STRINGS.

## [6.6] Nested Switch

- Switch statement inside a switch statement.

- Switch is used for menu-driven programs like file option in notepad will have New, Save, Save as, etc

  **Menu Driven Program using Switch Case**

```c++
#include <iostream>
using namespacestd;
int main()
{
    cout<<"Menu"<<endl;
    cout<<"1. Add\n"<<"2. Sub\n"<<"3. Mul\n"<<"4. Div\n";
    int option;
    cout<<"Enter your choice no."<<endl;
    cin>>option;
    int a,b,c;
    cout<<"Enter two numbers"<<endl;
    cin>>a>>b;
    switch(option)
    {
        case 1: c=a+b;
        break;
        case 2: c=a-b;
        break;
        case 3: c=a*b;
        break;
        case 4: c=a/b;
        break;
    }
    cout<<c<<endl;
    return 0;
}
```

