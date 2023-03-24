# [8] Array

## [8.1] Single Dimensional Array

Array is a collection of similar data elements under one name, each element is accessible using its index

• Memory for array is allocated contagiously
• For-each loop is used for accessing array
• N-dimension arrays are supported by C++
• Two-Dimensional Arrays are used for Matrices
• Array can be created in Stack or Heap Section of memory

- int A[5] = {1, 2, 3}
- float B[3] = {1.2, 3.4, 5.6}
- Char C[] = {'A', 'B', 'C'}

```c++
int main()
	{
		float A[] = {2.3f, 4.5f, 9, 8, 7};
		
		for (int x:A)
			cout << x << endl;
			
		return 0;
		
	}
```

```c++
int main()
	{
		char A[] = {'A', 66, 'C', 68};
		
		for (auto x:A)
		// for (int x:A)
			cout << x << endl;
    	
    	// here char C can be accessed using following commands
    	cout << A[3] << endl;
		cout << 3[A] << endl;
    	cout << *(A + 3) << endl;
    	cout << *(3 + A) << endl;
    
		return 0;
		
	}
```

- Always notice that here the name of the array name A, B, C never stores the value itself but the address of the array
- In C the operator a[b] = b[a] = *(a+b) hence individual elements of array can be accessed as a[b], b[a], *(a+b)
- Visit the link https://stackoverflow.com/questions/381542/with-arrays-why-is-it-the-case-that-a5-5a/381549#381549



## [8.2] Multi Dimensional Array

```c++
int A[2][3]={{2,3,4}, {5,6,7}};
int B[2][3]= {2,3,4,5,6,7};

```

## [8.3] For-each for Multi Dimensional Array

```c++
int main()
{
   // int A[2][3] = {2,3,4,6,3,5};
   int ROWS, COLS;

   cout << "Enter the number of row ";
   cin >> ROWS;
   cout << "Enter the number of columns";
   cin >> COLS;

   int A[ROWS][COLS] = {};

    //* For (int &x:A) // Notice that we cannot use x of type int here because x must be of type "ROW"
    //* Also notice that x is "ROW" hence we have to take it as type reference using "&" or else it will throw compilation error
    //* using reference here x is of type "ROW" of A and y is of type "COLUMN" of x
    //* Note that reference symbol here is a syntax. It won't create a new variable but use the same variable.    
    
    cout << "Input the array" << endl;
    for (auto &x:A)
    {
        for(auto &y:x )
        {
           cin >> y;
        }

        cout << endl;
    }

    // printing each element of for-each loop

    for (auto &x:A)
    {
        for(auto &y:x )
        {
           cout << y << " ";
        }

        cout << endl;
    }

    return 0;
}

```

