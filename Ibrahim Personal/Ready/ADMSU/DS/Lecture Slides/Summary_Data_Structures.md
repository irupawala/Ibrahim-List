# Summary

# Week 1

## Arrays and Linked Lists

### Arrays

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\1.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\2.PNG)

* Arrays can be present in stack or heap
* Row Major - Column index changes fast

* Column Major - Row index changes fast

### Linked Lists

#### Singly - Linked Lists

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\3.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\4.PNG)



* PushFront is an O(1) operation

* PopFront is also an O(1) operation as well
* PushBack, Topback and PopBack are O(n) operations for a linkedlist without a tail as we don't have pointer to last element and we have to iterate through all the n elements.
* PushBack and Topback are O(1) operation with a tail.
* Popback is expensive because we have to update tail from last to send last element but the problem is that we don't have a pointer from last to second last but a pointer from second last to last hence we have to again iterate through all the elements starting from head until we find the node which is pointing to the node also pointed by current tail and then update the tail pointer and then update the pointer of the last element to null. Hence O(n) operation.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\5.PNG)

* Note that head is first node and tail is the last node. The figure showed as head --> and tail --> are just the pointers to first and last nodes.
* Hence notice that if the list contains just one element then head and tail are pointing to same node.
* An attribute L:headpoints to the first element of the list. If L:head=NIL, the list is empty.
* In a circular list,the prev pointer of the head of the list points to the tail, and the next pointer of
  the tail of the list points to the head.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\6.PNG)



* Notice that find(key), Erase(key) takes O(n) time in the worst case, since it may have to search the entire list.







#### Doubly - Linked Lists

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\7.PNG)

* Note that with doubly linked list popping back and adding before becomes cheap.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\8.PNG)





Summary:

* Arrays have random access as it is a contiguous area of memory consisting of equal-size elements indexed by contiguous integers. **For example for binary search we can easily get middle element in time O(1) but for linkedlist finding middle element is an O(n) operation as we don't know how many elements are present in LinkedList.**
* **Hence arrays have constant time to access any element while LinkedList has O(n) time.**
* Singly Linked list has constant time O(1) to insert at or remove from the front. However arrays have O(n) time to add or remove from the front.
*  With tail and doubly-linked, constant time to insert at or remove from the front and back both.
* O(n) time to find arbitrary element.
* List elements need not be contiguous.
* With doubly linked list, constant time to insert between nodes or remove a node.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\9.PNG)



## Stacks and Queues

### Stacks

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\10.PNG)

#### Balanced Bracket Problem - Stacks 

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\11.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\12.PNG)

* Stacks can be implemented with LinkedList. One limitation of array is that we have maximum size based on array lenght we initialized. Possibly we also wasted space if array allocated is large but no of elements to be used in stack are less. Potential benefit is that operations are of O(1).
* LinkedList can also be used to implement stack. The good thing is there is no pre-defined limit like array. The overhead here as compared to array is that we have to store pointer with keys but in array only elements are stored. On the other hand there is no waste of space in terms of allocated space that isn't actually used.
* Hence Linkedlist has fixed amount of array head while for array you may potentially over allocated.
* For LinkedList Push becomes PushFront. similarly Pop --> PopFront(), Top --> TopFront()

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\13.PNG)

### Queues

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\14.PNG)



* Queues can be implemented using Linked List.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\15.PNG)

* Queue can also be implemented using array in the same way that is pushing from the back and popping from the front but note that popping from the front will be an expensive operation unless we are using circular array.
* We have a write index which will tell us where the next enqueue operation will happen and the read tells you when dequeue should happen.
* To check if the queue is empty() we will compare read = write ?.
* When we will do enqueue(g) here it will not allow us to do that because if read and write index are same then read and write operation cannot be distinguished when the array is full.
* Note that read and write index will be equal if the array is empty.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\16.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\17.PNG)

* Notice that if we want the queue of fixed size then array is good choice if size is not fixed then queue.
* but note that if array size is too long then used space could lead to waste of memory. If we implement with linkedlist then for every element we will have to pay for the pointer.
* If we attempt to dequeue an element from an empty queue, the queue underflows.
* When Q.head=Q.tail + 1, the queue is full, and if we attempt to enqueue an element, then the queue overflows.

## Trees

### Binary Search Tree

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\18.PNG)

* Binary search tree only has two children's.
* Note that this tree above shown is interesting. Alphabetically at each node left child is less then node and right child is greater then node. This allows searching for any name possible.



![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\19.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\20.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\21.PNG)

* Root: Top node in the tree.
* Child has a line down directly from a parent.
* Ancestor: parent, parent of parent, etc
* Descendant: child, child of child
* Sibling: two node sharing the same parent
* Leaf: node with no children
* Interior node: All nodes that aren't leaves
* Level: 1 + num of edges between root and node. Fred = level 1 and sam = level 3 here
* Height: Maximum depth of subtree node and farthest leaf. Fred = height 3, Kate = height 2, Sam = height 1
* Forest: Collection of trees

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\22.PNG)

* Code to find height of the tree.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\23.PNG)

* Code to find number of nodes in a tree.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\24.PNG)

### Tree Traversal

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\25.PNG)



#### Depth - First Traversal Methods

* In Order Traversal, Pre-Order and Post order are depth first traversal methods.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\28.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\26.PNG)

* InOrder Traversal is only used for Binary trees. But PreOrder and PostOrder Traversals are used not just for binary trees but all other trees.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\29.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\27.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\30.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\31.PNG)



* Note that for recursive traversal stack is being used under the cover.
* This is because every time we call a subroutine we have to store the return address which is stored in a stack.

#### Breadth - First Traversal Methods

* In a breadth - first traversal method we are going to use a queue instead of a stack.
* Instantiate a queue and put a root of the tree.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\32.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\33.PNG)



* Notice that over here breadth first search is implemented with an explicit queue.
* You can do depth-first searches rather than recursively, iteratively, but you will need an additional data structure which is a stack to keep track of the work still to be done.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\34.PNG)



# Week 2

## Dynamic Array and Amortized Analysis

### Dynamic array

* Semi-solution: dynamically allocated array. Decide array size during runtime.
* But what if you don't know max size when allocating an array.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\35.PNG)

* Notice that dynamically allocated array are the ones in which you allocate the size but once the size is fixed you can't change it but dynamic arrays are the one in which you store a pointer to a dynamically allocated array, and replace it with a newly-allocated array as needed.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\36.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\37.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\38.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\39.PNG)

* Notice that there is no static array in python.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\40.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\41.PNG)

* Notice that dynamic array can also be resized smaller as soon as we got under one-half utilization.

### Amortized Analysis

* Sometimes looking at the individual worst-case may be too severe. We may want to know the total worst-case cost for a sequence of operations.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\42.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\43.PNG)

* Amortized cost is the monthly installment on the car paid per month while worst case cost is the total amount paid in one month.

#### Aggregate Method



![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\44.PNG)

* Notice that n in n + 2j is because every ci has a cost of 1 so we sum that n times + sum of all powers of 2 till n-1. for eg for 100 power of 2 is 2, 4, 6,...64.
* Hence n+2j = 2n = O(n) and then O(n)/n.

#### Banker's Method

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\45.PNG)

* Note that aggregate method is like paying monthly installments to car seller while bankers method is like putting money in bank.
* Note that we're not actually changing our code, this is strictly analysis. But we're conceptually thinking about putting our saved saved extra cost as sort of tokens in our data structure that later on we'll be able to use to pay for the expensive operations.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\45.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\46.PNG)

* When we pushback any element we place a token for that element and element located capacity/2 before that.
* when we move the element to a bigger array when array needs to be resized we have already prepaid for moving that element and the buddy element located before the n - (capacity/2) location.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\47.PNG)

#### Physicist's Method

* The idea of the physicist's method is to define a potential function, which is a function that takes a state of a data structure and maps it to an integer which is its potential.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\48.PNG)

* first rule: phi of h sub 0 means initial state of the data structure and that has to have a potential of 0.
* second rule: potential is never negative
* Ct is the true cost
* Amortized cost is 
  * ct plus the change in potential before doing the operation and after doing the operation.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\49.PNG)

* Notice that what the last equation means is we've come up with a lower bound on the sum of the amortized costs which is the sum of the true costs. So if we want to look at a cost of entire sequence of operations we know it's at least the sum of the true costs.
  

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\50.PNG)

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\51.PNG)

* Assume cost of insertion Ci = 1, as we are not resizing Cap remains the same and hence gets cancelled out.
* Sizei - Sizei-1 = 1 as we are just adding one element. Note that 3 obtained is same as what has been obtained with bankers method.. 

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\52.PNG)



* Will the same argument work if we replace the potential function and set \Phi(h) = 3 \times size - capacityΦ(*h*)=3×*size*−*capacity*?

* For the case when no resize is made, c_i + \Phi(h_i) - \Phi(h_{i-1}) =*c**i*+Φ(*h**i*)−Φ(*h**i*−1)= = 1 + 3size_i - cap_i - (3size_{i - 1} - cap_{i - 1}) ==1+3*s**i**z**e**i*−*c**a**p**i*−(3*s**i**z**e**i*−1−*c**a**p**i*−1)= = 1 + 3(size_i - size_{i - 1}) = 1 + 3 = 4=1+3(*s**i**z**e**i*−*s**i**z**e**i*−1)=1+3=4.

  For the case with resize, if k = size_{i - 1} = cap_{i - 1}*k*=*s**i**z**e**i*−1=*c**a**p**i*−1, then \Phi(h_{i - 1}) = 3size_{i - 1} - cap_{i - 1} = 3k - k = 2kΦ(*h**i*−1)=3*s**i**z**e**i*−1−*c**a**p**i*−1=3*k*−*k*=2*k*, \Phi(h_i) = 3size_i - cap_i = 3(k+1) - 2k = k + 3Φ(*h**i*)=3*s**i**z**e**i*−*c**a**p**i*=3(*k*+1)−2*k*=*k*+3. Then c_i + \Phi(h_i) - \Phi(h_{i - 1}) =*c**i*+Φ(*h**i*)−Φ(*h**i*−1)= = (size_i) + k + 3 - 2k = (k + 1) + k + 3 - 2k = 4=(*s**i**z**e**i*)+*k*+3−2*k*=(*k*+1)+*k*+3−2*k*=4.



## Amortized Analysis: Summary

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\53.PNG)

* Can we add a constant factor each time instead of using the constant multiplicative factor ?

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\54.PNG)

* Note that if we add constant factor then amortized cost id O(n) and not O(1) when using multiplicative element.

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\55.PNG)

# Week 3

* Heap Sort Algo Visualization - https://www.cs.usfca.edu/~galles/visualization/HeapSort.html

* Notice that heap sort is an improvement of selection sort algorithms and is an inplace algorithm.
* Heap sort has running time of O(nlogn).
* In practice quick sort is usually faster. However heap sort has worst case running time of nlogn while quick sort algo has average case running time of nlogn. Hence one of the popular approach is intra sort algo where you first run quick sort algo, if it turns out to be slow meaning if the recursion depth  exceeds clog(n) for some constant c then you stop quick sort and switch to heap sort algo which is guaranteed to have running time nlog(n).

![](C:\Users\1000249643\Desktop\Programming Langauages\Algorithms and Data Structures Udemy\Data Structures\Images\56.PNG)

* Notice that after we know that building heap takes linear time n it can be used to solve a problem of extracting k max elements from n elements in linear time O(n). This k has to be less then or equal to n/logn which is also equal to less then or equal to sqrt(n). 

