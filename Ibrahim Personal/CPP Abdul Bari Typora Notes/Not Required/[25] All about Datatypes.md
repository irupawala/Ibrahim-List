# [25] All about Datatypes

![](C:\Users\1000249643\Desktop\Programming Langauages\Cpp Abdul Bari Udemy\Notes\[26] All about Datatypes\[1] Datatypes.PNG)



## [25.1] Character

- wchar_t is wide character
- char16_t and char32_t is used for storing unicode which 
is just like ASCII code for storing other Natural language
processing alphabets like chinese, hindi, etc.
- More info is available in unicode.org

## [25.2] Integer

- long int and long long can store larger integers.
- int can be of 2 bytes, 4 bytes.
- It depends on the bitsize of the machine i.e. ALU

## [25.3] Floating Point

- Float number is stored in IEEE 754 standard in every machine
- 17.26 is represented in 1726E-2
- **FLOAT ALWAYS TAKES 4 BYTES, CHAR ALWAYS TAKES 1 BYTES**
- **SIZE OF INT DEPENDS ON COMPILER.**

## [25.4] Boolean

* 0 : FALSE
* ANY OTHER NO: TRUE

## [25.5] Void

- Void:- Used for defining null function and pointer

## [25.6] Useful functions

* sizeof() is used for learning the size of the datatype
* CHAR_MIN, INT_MIN, CHAR_MAX, INT_MAX is used for learning the range

## [25.7] Variables

- Methods of assignment to a variable

```c++
int day=1;
int day(1);
int day=(0);
int day{0};
int day={0};
```

* Literals: Type of values that can be assigned to a variable

```c++
int a = 10;
int a = 010; // This is octal number system
int a = 0x10; // This is hexadecimal number system
```

* INT long literals are followed by L;

```c++
int dist = 65834L;
```

- To a float literal integer numbers can be assigned.

```c++
float a = 10;
```

* It is a good practice to follow a float literal by f;
because by default decimal numbers in C are double

```c++
float price = 12.5;
float cost = 1.52e4f;
double weight = 2.53e7L;
```

- DOUBLE float is followed by L;

```c++
char section = 'A' // single quote is char
char section = "A" // double quote is string
char section = 65 // This is also A assigned to section
```

* Notice that sting is a CLASS and not a pre-defined datatype like int, float,etc
* Hence we can also use name string whenever we want

```c++
//e.g: 

int string;
```

