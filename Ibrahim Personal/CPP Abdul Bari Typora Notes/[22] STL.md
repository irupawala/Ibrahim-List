# [22] STL

## [22.1] Why STL ?

- Standard Template Language
- For Storing collection of values we need data structures
- Data Structures are Collection or arrangement of data for its efficient utilization.
- Depending on the utilization one can arrange the data so that it can be utilized efficiently.
- Efficiency in terms of time and space.



- Let us say we have collection of marks of data and we want to do all the operations on them.
- So we can use a built-in data structure like array. Array is collection of similar data structures.
- Now we can find average, mean, max, min, etc



- let us say we have array of 10 elements now we cannot add 11th element.
- Hence we have to know the size of the array beforehand.
- Also if we define array of 100 elements but use only 10 elements then it is waste of memory.
- THESE ARE COMMON PROBLEMS IN **PRE_DEFINED DATA STRUCTURES**.



- let us say we have array of 10 elements now we cannot add 11th element.

- To deal with such kinds of problem we can have a new array of larger size defined in the heap dynamically and now pointer is pointing to that array.

- eg: 

  ```c++
  int *A = new int[10];
  A = new int[20];
  ```

## [22.2] Types of Data Structures

- Arrays have fixed size.
- Instead of array we can have LinkedList. Here instead of having fixed size array we have collection of nodes where each node can have values.
- Benefits of linkedlist is that size of linkedlist grows or reduce as and when numbers are added or deleted.
- Hence this will take the size depending on the elements hence the size is variable.

- New nodes can be added or deleted anywhere in the LinkedList. This is called singly linkedlist. It has 
one pointer and can only go in one direction.

- Similarly we have doubly linkedlist where every nodes have previous pointer too hence in Doubly LinkedList you can go in both forward and reverse direction.

- Some other data structures are stack, lifo, queue, Deque, Priority Queue, Map, Set.

- **C++ provides built-in libraries of classes for all the data structures called as STL.**

## [22.3] STL Classes

STL have:

1. Algorithms
2. Containers
3. Iterators

- **Built-in Algorithms are there to manage containers**

- Arrays linkedlist stack queue are containers. **Containers contains collection of data.**

- **Iterators are used for iterating over collection of value.**

  

- **some built-in algorithms are:** 
- **search(), sort(), reverse(), binary_search(), concat(), copy(), union(), intersection(), merge(), heap()**



- some built-in algorithms are: 
- search(), sort(), reverse(), binary_search(), concat(), copy(), union(), intersection(), merge(), heap()

### 1. Vector:

- Self-managed array. Dynamically manages the size of array.
- This can grow and reduce itself. If we create bigger array it will dynamically copy the array into
bigger size array and also it will copy to the smaller size array if we reduce the size.
- functions available are as follows: push_back(), pop_back(), insert(), remove(), size(), empty().

### 2. List:

- This is for Doubly linkedlist. It has a pointer for next node and previous node.
- It is a template class. It can have any objects like int, float, string, your own object, etc.
- It has all the functions of vector but also it has push_front(), push_back(), front(), back()

### 3. Forward_List:

- This is a singly linkedlist.
- If we know that we are going to access only in forward direction then avoid doubly as it takes more space
- same functions as lists.

### 4. Deque:

- Same as vector but double ended queue hence you can insert and delete from both the ends
- same set of function as list and forward_list
- In vector you cannot add/ delete elements from front side

### 5. Priority_queue:

- For max heap data structures.
- The objects, in addition to their usual data, contain another number called priority. The insertion of object in Priority Queue happens like in a normal Queue. The servicing of objects in Priority Queue happens in order of Priority, either the smallest or largest priority number depending if it is a Min-Priority-Queue or Max-Priority-Queue
- In a priority queue, each element has some type of value that can be ordered with respect to other values of the same type (like a number, or a string [strings can be ordered lexicographically]). As elements are pushed onto the back or popped off of the front, the priority queue re-orders itself to make the front of the queue contain the element with the smallest value (or the largest, if the priority is defined to be in descending order).
- Has the function like push(), pop(), empty(), size().

### 6. Stack:

- same as LIFO.
- same functions as priority_queue

### 7. Set:

- will only have unique elements.
- Order of the elements will not be maintained.
- This is a unique set of values and values cannot be modified but only displayed

### 8. Multiset:

- Same as set but allows **duplicate**

### 9. Map: 

- Allowed for storing key: value pair
- Uses hash table
- **uses unique key**

### 10. MultiMap:

- **Multiple keys are allowed but same key value pairs are not allowed.**

## [22.4] Using STL Classes

- Iterators are available in every collection.
- Using vectors we don't have to worry whether the array is full or not, how to add or delete.

E.g. 1:

- Eg of using an object vector and inserting elements:

```c++
# include <vector>

int main()
{

	vector <int> v() // if you mention the size in brackets it will create a vector of that size or 
					 // else it will create an array of size 16
					 
	vector <int> v = {10, 20, 40, 90}; // you can also mention the initial vector
	
	v.push_back(25);
	v.push_back(70);
	v.pop_back();
	
}
```

### Iterators

* Iterators are used for accessing each elements in the vector

#### 1. For each loop (introduced in C++11)

```c++
for (int x: v)
cout << x;
```
#### 2. Use of Iterators classes

- Now we can get object of iterator and iterate through the list of elements as shown below:

```c++
vector<int>::iterator itr=v.begin();

// here iterator class belongs to a vector class. 
// The object of iterator is itr.
// itr = v.begin(); This will initialize the iterator to the starting point of the vector.
// begin and end functions are available in all containers. begin gives the starting of the collection and end gives end of the collection.
// We also have rbegin and rend functions which helps in traversing a collection from rear end. reverse traversing

vector<int>::iterator itr;
for (itr=v.begin(); itr!=v.end(); itr++)
	cout << *itr; // * because itr is like a pointer to the elements inside the collection
	
	
```

E.g. 2: // see how by one simple change we have changed vector to list. 

```c++
# include <list>

int main()
{
			 
	list <int> v = {10, 20, 40, 90}; 
	
	v.push_back(25);
	v.push_back(70);
	v.pop_back();
	
	
	
	list<int>::iterator itr;
	for (itr=v.begin(); itr!=v.end(); itr++)
	cout << *itr; 
		
}
```

- Notice that similarly we can also change the container to forward_list, dqueue as the functions are same
but not set as for set we cannot use push_back and push_front as it has the functions like insert 

- Handling of the data structures is the same but the performance and internal memory organization 
will be different.

```c++
#include <iostream>
#include <vector>
#include <list>
#include <forward_list>
#include <set>

using namespace std;

int main()
{
   // vector <int> v = {10, 20, 30, 40};
   // list<int> v = {10, 20, 30, 40};
    //forward_list<int> v = {10, 20, 30, 40}; // This is a singly linked list
    set<int> v = {10, 20, 30, 40}; // This is a unique set of values and values cannot be modified but only displayed

    // change to these functions while using the list and vectors
   // v.push_back(50);
   // v.push_back(60);
   // v.pop_back();

   // change to these functions while using the forward list
   //  v.push_front(50);
   //  v.push_front(60);

   // change to these functions while using set
   v.insert(50);
   v.insert(60);


///////////////////////////////////////////////////////////////////////

    //vector<int>::iterator itr;
    //list<int>::iterator itr;
    //forward_list<int>::iterator itr;
    set<int>::iterator itr;

    cout << "Displaying value using Iterator" << endl;

    for (itr=v.begin(); itr!=v.end(); itr++)
        //cout << ++*itr << endl;
        cout << *itr << endl; // sets have unique elements and value of sets cannot be modified

///////////////////////////////////////////////////////////////////////

    cout << "Displaying value using For-each loop" << endl;
    for (int x: v)
        cout << x << endl;


/* Notice how by one simple class change the container is converted to doubly linked list */
/* Notice that Iterators are capable of modifying the values */
/* Sets have unique elements and value of sets cannot be modified */

    return 0;
}

```



## [22.5] Map Function

- These are used for storing key-value pairs 
- These are used when the search is required for a particular key.
- Note that instead of key-value pair you can store any data types like your own objects too.

```c++
#include <iostream>
#include <map>

using namespace std;

int main()
{
    map <int, string> m;
    m.insert(pair<int, string> (1, "John"));
    m.insert(pair<int, string> (2, "Ravi"));
    m.insert(pair<int, string> (3, "Khan"));
    //cout << "Hello world!" << endl;

    map<int, string>::iterator itr;
    for (itr = m.begin(); itr!= m.end(); itr++)
    {
        cout << itr->first << " " << itr->second << endl;
    }

    // you can use key to get the pair using the find function

    map<int, string>::iterator itr1;

    itr1=m.find(2);
    cout << "Value found for key 2 is" << endl;
    cout << itr1->first <<  " " << itr1->second << endl;



    return 0;
}

```

