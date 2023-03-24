# [19] Constants, Preprocessor Directives and Namespace

## [19.1] Constant Qualifiers

Usage of Constants:

### 1. Used as a constant identifier inside a function or class.

* If we write `const int x = 10;`  then it becomes constant identifiers and this constant identifier cannot be modified.

The properties of constant identifiers are as follows:

1. constant identifier is a also an identifier like variable albeit this identifier cannot be modified.
2. This will consume memory as per the datatype declared
3. constants are the part of the compiler.
4. Used for declaring constants inside the class or function

- In contrast #define x 10 is also a constant but it is a preprocessor directive and it is executed before compilation process starts.

The properties of preprocessor directive are as follows:

1. x also cannot be modified.
2. preprocessor directives does not hold space in memory. It is just like a symbol.
3. This is not part of a language. It is outside compiler meaning pre-compiler
4. These are used for declaring constants if it is used by the entire program just like a global variable.

### 2. Used as a pointer of type constant integer.

```c++
#include <iostream>
using namespace std;

int main()
{
    //const int x = 10;	// notice that here we cannot simply write const int x=10 and expect that pointer can point to it
    int x = 10; // Also note that after making the pointer of type integer constant we can also define int x as const and it will work as expected. Also we can directly make pointer of type int constant without defining x as const explicitly
    const int* ptr = &x;
    // int const *ptr=&x; // This can also be written this way
    //(*ptr)++;
    //++*ptr;
    cout << *ptr << endl;
}
```

- Note that in this case CONSTANT TO AN INTEGER POINTER cannot modify x when we write ++ *ptr because data is locked

* Also note that cout << *ptr can access the value of x but cannot modify it as it will treat the data as constant.
* Notice that here we cannot simply write const int x=10 and expect that pointer can point to it
* Address of constant identifier cannot be stored to the pointer hence we have to make a constant pointer
* This can be read from right to left as pointer of type integer constant.
* Also note that after making the pointer of type integer constant we can also define int x as const and 
  it will work as expected. Also we can directly make pointer of type int constant without defining x as const explicitly

```c++
int main()
{

int x = 10;
const int* ptr=&x;
// int const *ptr=&x; // This can also be written this way
int y = 20;
ptr = &y; // now we are pointing the same pointer to address of y
++ *ptr; // This cannot be modified as the integer is a constant.
cout << *ptr;
}
```

* In this case now the pointer will point to the address of y but note that even now it won't be able
to modify the value of y.

### 3. Used as a constant pointer of type integer 

* Instead of `int const *ptr` if we write `int *const ptr` then instead of data, pointer becomes locked now and hence cannot be modified. This means that pointer can now point to only one address which cannot be changed.

```c++
int main()
{

int x = 10;
int * const ptr=&x; // This is now constant pointer of type integer
int y = 20;
ptr = &y; // This is not possible now as the pointer itself is constant
++ *ptr; 
cout << *ptr;
}
```

### 4. Used as a constant pointer to integer constant

* If we write const before the constant pointer of type integer then it becomes constant pointer
  to integer constant. Hence now data is constant and also pointer is constant.

```c++
int main()
{

int x = 10;
const int* const ptr=&x; // This is now constant pointer to integer constant
int y = 20;
ptr = &y; // This is not possible now as the pointer itself is constant
++ *ptr; // Now this is also not possible as data cannot be modified.
cout << *ptr;
}
```

### 5. Constant Function:

```c++
#include <iostream>
using namespace std;

class Demo
{
public:
	int x=10;
	int y=20;
	
void Display() const
{
    cout << x << " " << y << endl;
    x++;
    y++;
    cout << x << " " << y << endl;
}
};
```

* In this example if we don't want the member function to modify the values of data members then
  we can write `const` at the end of the member function

- These are helpful when we want the member function to avoid modifying the data members by mistake.

### 6. Constant call by reference

```c++
#include <iostream>
using namespace std;

void fun(int &x, int &y) // call by reference hence x and y are alias of a and b 
// also notice that for call by reference we know that the function fun will be copied at the place of function call hence it becomes inline function because as we know that it is not possible for the function to modify the values of another function unless being an inline function. 
{
    x++;
    y++;
    cout << x << " " << y << endl;
}

int main()
{
    int a = 10, b = 20;
    fun(a,b);
}
```

- One of the benefits of the inline functions is it makes the code simple as the function is copied to 
the place of the function call but there is one big disadvantage. This is that lets say here in the 
function x is being incremented but now x is an alias of a hence the function is modifying the original integer a. If we don't want to allow the function fun to modify the values of the original function we can define them as `const` as shown below:

```c++
void fun(const int &x, int &y)
{
    x++;
    y++;
    cout << x << " " << y << endl;
}

int main()
{
    int a = 10, b = 20;
    fun(a,b);
}
```



## [19.2] Preprocessor Directives

- These are also called as macros
- These are instructions to compiler so that before starting compilation it can follow those instructions.
- They are instructions to compiler
- They are processed before compilation
- They are used for defining symbolic constant
- They are used for defining functions
- They also support conditional definition
- Most famous of these are #define

### e.g 1: Defining variable as constant

```c++
# define PI 3.1425

int main() {
    cout << PI;
}
```

- Here the value of PI will be replaced by 3.1425 before the compilation begins hence the compiler will 
see 3.1425 in the program and not PI.
- These # define pi (value) are known as SYMBOLIC CONSTANTS
- We can also do:

### e.g. 2: Defining object name as constant

```c++
#include <iostream>
using namespace std;

# define c cout // hence now we can also change object name

int main() {
c << "Ibrahim";
}
```

### e.g. 3: Defining functions as pre-processor directives

- We can also define functions as pre-processor directives:

```c++
# define SQR(x) (x * x) // NOTICE THAT EQUATION (x*x) HAS TO BE WRITTEN IN BRACKETS

int main(){
cout << SQR(5);
}
```

- Here 5 * 5 will be seen by the compiler. It has been replaced even before the compilation begins

### e.g. 4: Defining message to be displayed in double quotes

If we define the pre-processor directive with just #x then during the compilation the string will 
be replaced with double quotes in the definition.

```c++
# define MSG(x) #x

int main()
{

cout << MSG(Hello); // here MSG(Hello) will be replaced by "Hello" and Hello will be displayed on the screen

}
```

### e.g. 5: If not defined

```c++
Ifndef: // if not defined

# ifndef: 
	# define PI 3.142517
# endif

```

- Defining the value only if it is not defined because redefining will cause an error.

```c++
#include <iostream>
using namespace std;

#define max(x,y) (x>y?x:y)
#define msg(x) #x

#ifndef PI
	#define PI 3.1425
#endif

int main()
{
cout<<PI;
cout<<max(10,12)<<endl;
cout<<msg(hello)<<endl;
}
```

## [19.3] Namespace

- Namespaces are used for removing name conflicts
- If we require the functions or classes with the same name or signature or prototype then there will 
be name conflicts
- Ibrahim: NAMESPACE ARE USED TO STRUCTURE A PROGRAM INTO LOGICAL UNITS

```c++
void fun(){
cout << "First";
}

void fun(){
cout << "Second";
}

int main(){
fun();
}
```

* Here the compiler will not compile the program at the first place because name conflict will happen.

- Using the namespace we can encapsulate the function inside the namespace and then we can call the functions separately using the scope resolution operator.

```c++
namespace First {					// these brackets are mandatory
	void fun() {
	cout << "First";
	}
}

namespace Second {
	void fun() {
		cout << "Second";
		}
}

int main() {
First::fun();
}
```

- Also note that in one namespace we can have many other things like all the related classes, functions
and objects

* Also If we want to avoid using scope resolution operator all the time we can write **using namespace std**

```c++
using namespace first; // RECOMMENDED TO AVOID THESE KIND OF STATEMENTS
int main() {
fun();			// if you don't mention anything fun of first will be called
second::fun();  // if you explicitly mention namespace using scope resolution operator then second will be called
}
```

* NOW WE CAN UNDERTAND THAT INSTEAD OF NAMESPACE STD DECLARATION IN EVERY PROGRAM WE CAN ALSO WRITE

```c++
std::cout<<"kkk"<< endl;
```

