# [7] Loops

* There are 4 loops statements in C++

1.  pre-tested loop while()
2. post-tested loop do..while()
3. counter controlled loop for()
4. for each loop for Collections for()

## [7.1] While statement

- Condition is checked first and then process is done.

```c++
while(int i <= n)
{
	process...
}
```

## [7.2] Do-While statement

- Process is done once then condition is checked if it is true then execution is done again

  ```c++
  do
  {
  	process...
  }while(int i <= n);
  
  ```



![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\Cpp Abdul Bari Udemy\Notes\[8] Loops\[2] While_Do_While.PNG)



## [7.4] For loops

```c++
for (i=0; i<=n; i++)
{
}
```

- Note that initialization, condition and increments are optional but if we don't include condition in for loop we have to manually add the condition
in the for block to break it off.

```c++
	{ // This is completely valid piece of code.
	int i=0;
	for (;i<=n;)
		{
		cout << i << "Hello\n";
		i++;
		}
	}
```

- We can also skip the condition but then we have to add condition manually

```c++
{ // This is completely valid piece of code.
int i=0;
for (;;)
	{
	cout << i << "Hello\n";
	i++;
	if (i>10)
		break;

	}
```
## [7.5] Nested For Loop

```c++
for (int i=0; i<3; i++)
	{
		for (int j=0; j<3; j++)
			{
				cout << i << j << endl;
			}
	}
```

## [7.6] For-each statement

- Introduced from C++ 11.
- For each loops are used with the collections of the elements like arrays, vectors, etc.
- For each loop will NOT work on Pointers.
- Benefit of for each over for is that here we don't have to know the total no of elements in the array

```c++
int A[] = {8, 6, 3, 9, 7, 4}

 for (int x : A) // read it as for each x in A
	{
		cout << x << endl; // note that in for statement i was index but here x is element itself
		}
```

Another example: (what if we do ++x in place of x ?)

```c++
for (int x: A)
	{
	cout << ++x << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}
```

Another example: (What if we want to change the value in array itself ?)

```c++
for (int &x: A) // note that this &x is called the reference. meaning it gives the name to the same value
				// This way the elements in original array will change
		{
	cout << ++x << endl; 
		}	
```

## [7.7] Auto Data Type

- One more benefit for using for each loop is AUTO datatype
- If we don't know the datatype of the elements in array we can write AUTO datatype in for each		

```c++
for (auto x: A) // This will automatically make the datatype of x as the datatype available in the array.
	{
		cout << x << endl;
		}
```

**Program Demonstrating for - each statement use**

```c++
#include <iostream>

using namespace std;

int main()

{

    int A[] = {8, 6, 3, 9, 7, 4};

    cout << "Displaying the incremented values and also storing it." << endl;


    for (int &x: A)
        {
        cout << ++x << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}


    cout << "Displaying the original values but storing incremented." << endl;

    for (int &x: A)
        {
        cout << x++ << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}

    // Displaying A

     cout << "Displaying A" << endl;

    for (int x: A)
        {
        cout << x << endl; // here 9, 7, 4... will be printed but note that original values in the array will remain unchanged.
		}


    return 0;
}



```

