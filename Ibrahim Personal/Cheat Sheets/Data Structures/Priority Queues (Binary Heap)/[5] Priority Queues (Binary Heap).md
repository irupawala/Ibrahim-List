# Priority Queues (Binary Heap)

* A priority queue is a generalization of a queue where each element is assigned a priority and elements come out in order by priority.
* Operations supported are Insert(p), ExtractMax(), Remove(p), GetMax(), ChangePriority(x, p).
* With Unsorted list ExtractMax() operation is O(n) while with Sorted list Insert(p) operations is O(n). With the use of priority queues both Insert and ExtractMax takes **O(log n)** time.
* Priority queues can be implemented with the help of Binary Max Heap which **where the**
  **value of each node is at least the values of its children.**
* GetMax works in time O(1), all other operations (GetMax, ExtractMax, Insert, Remove, SiftUp, SiftDown, ChangePriority) work in time **O(tree height)**.
* How to keep a tree shallow ?. A binary tree is complete if all its levels are filled except possibly the last one which is filled from left to right.
* The running time of BuildHeap is **O(nlogn)** since we call SiftDown for O(n) nodes.
* Advantages of **Complete** binary tree :
  * Low Height O(log n)
  * Store as Array 
    * 1-based Array: parent(i) = floor(i/2), leftchild(i) = 2i, rightchild = 2i+1
    * 0-based Array: parent(i) = floor(i-1/2), leftchild(i) = 2i+1, rightchild = 2i+2
* In d-ary heap nodes on all levels except for possibly the last one have exactly d children.
* The height of such a tree is about **logd(n)**. The running time of SiftUp is **O(logd(n))** and SiftDown is **O(d*logd(n))**.



![1642756375347](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1642756375347.png)



## Time for common Operations

* All Operations work in time O(log n). Can also be very space efficient.

## When to use ?

* Use Priority Queue when Max or Min Number is to be extracted from the list during each iteration and also New numbers are to be added.
* Algorithms that use Priority Queues: Dijsktra’s algo, Prim’s algo, Huffman’s algo, Heap sort

## Python Implementation

### Built-In heapq Implementation

**Min Heap**

```python
import heapq

heap = []
heapq.heapify(heap) # Creating empty heap

# Adding items to the heap using heappush function
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)

# printing the value of minimum element
print("Head value of heap : "+str(heap[0]))
 
# printing the elements of the heap
for i in heap: print(i, end = ' ')
print("\n")

# Extracting Max items to the heap using heappush function
element = heapq.heappop(heap)

# Replacing Heap element
# It deletes the smallest element from the Heap and then inserts a new item. This function is more efficient than calling heappop() and heappush().
heapq.heapreplace(heap, element)

# nlargest() Syntax
# It finds the n largest elements from a given iterable. It also accepts a key which is a function of one argument.
# The selected items have to satisfy the k function. If any of them fails, then the next higher number is considered.
heapq.nlargest(n, iterable, key=None)
print(heapq.nlargest(2, heap))
print(heapq.nlargest(2, heap, is_even))

# nsmallest() Syntax
# It is also similar to the nlargest() in operation. However, it gets the n smallest elements from a given iterable. It too accepts a key which is a function of one argument.
# The selected items have to satisfy the k function. If any of them fails, then the next smaller number is considered.
heapq.nsmallest(n, iterable, key=None)
print(heapq.nsmallest(2, heap))
print(heapq.nsmallest(2, heap, is_even))

# Notice that heapq also allows inserting tuples/list to the set of elements. In this case Max/ Min will always be received based on the FIRST element.
heapq.heappush(heap, [9, 1, 2]) # Notice here that 9,8,7 will be compared
heapq.heappush(heap, [8, 2, 2])
heapq.heappush(heap, [7, 3, 3])

element = heapq.heappop(heap)
print(element)
```

### Delete Element from Heap

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
heapq.heappush(heap, 5)
heapq.heappush(heap, 6)
remove_index = heap.index(4)
heap[remove_index] = heap[0]
heapq.heappop(heap)
# O(n)
heapq.heapify(heap)
# O(logN)
if remove_index < len(heap):
    heapq._siftup(heap, remove_index)
    heapq._siftdown(heap, 0, remove_index)
    

```

### Alternate Method to Delete Element from Heap

```python
# removes an element from the heap keeping the heap property
def remove(self, heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
        heapq._siftup(heap, ind)
        heapq._siftdown(heap, 0, ind)
```

### Built-In Queue Implementation

**Max Heap**

```python
import queue

heap = queue.PriorityQueue()

heap.put(-10)
heap.put(-20)
heap.put(-30)
heap.put(-100)

print(-heap.queue[0])
print(-heap.queue)
print(-heap.get())

for i in heap.queue:
    print(-i, end = ' ')
```



### Python Implementation using Dictionaries for ChangePriority

```python
def MakeQueue(cost):
    H = {index: cost for index, cost in enumerate(cost)} #using dictionary as it does not change the index upon deletion of an element
    return H
    
def ExtractMin(H):
    values_list = list(H.values())
    keys_list = list(H.keys())
    min_distance_element = min(values_list) 
    min_index = keys_list[values_list.index(min_distance_element)] #Extracting the index of min distance
    del(H[min_index]) # deleting min distance
    return (min_index)
   
def ChangePriority(PrioQ, v, dist):
    PrioQ[v] = dist # updating the distance values in H
    return 0

cost = [100000] * 5
cost[0] = 0

PrioQ = MakeQueue(cost) # Index and Distance as keys

v = ExtractMin(PrioQ)
index = 1
cost[index] = 10
ChangePriority(PrioQ, index, cost[index])   

```



### Python Implementation from Scratch

```python
class Maxheap():
    
    def __init__(self, A):
        self.A = A
        self.size = len(self.A) 
        self.buildHeap()

    def buildHeap(self): # Turns array into heap
        for i in reversed(range(self.size//2)):
            self.siftDown(i)        
        
    def siftDown(self, i):
        maxIndex = i
        l = (2*i) + 1 # leftchild
        if l <= self.size - 1 and self.A[l] > self.A[maxIndex]:
            maxIndex = l
            
        r = (2*i) + 2 # rightchild
        if r <= self.size - 1 and self.A[r] > self.A[maxIndex]:
            maxIndex = r   
            
        if i != maxIndex: # Meaning one of the child is greater because maxIndex = i in the beginning
            self.A[i], self.A[maxIndex] = self.A[maxIndex], self.A[i]
            self.siftDown(maxIndex)
            
    def siftUp(self, i):
        parent_i = (i - 1)//2  # parent
        while parent_i >= 0 and self.A[parent_i] < self.A[i]:           
            self.A[parent_i], self.A[i] = self.A[i], self.A[parent_i]
            i = parent_i 
            parent_i = (i - 1)//2  # parent
                
    def extractMax(self):
        result = self.A[0]
        self.A[0] = self.A[self.size - 1]
        # del(self.A[self.size-1])  
        self.size = self.size-1      
        self.siftDown(0)
        return result

    def getMax(self):
        result = self.A[0]
        return result
            
    def insert(self, p):
        self.A[self.size] = p
        self.siftUp(self.size)
        self.size += 1
        
    def remove(self, p):
        i = self.A.index(p)
        self.A[i] = float('inf')
        self.siftUp(i)
        self.extractMax()
        
if __name__ == '__main__':
    
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
    
    H = Maxheap(A)  
    H.remove(12)       
    print(H.A)
    print(H.extractMax())
    print(H.extractMax())
    H.insert(10)    
    print(H.extractMax())           
```

### Python Implementation

```python 
# Implementation without self.size management and directly using len(self.A)-1
# Also deleting max elements to remove the unnecessary elements from self.A


class Maxheap():
    
    def __init__(self, A):
        self.A = A
        self.buildHeap()

    def buildHeap(self): # Turns array into heap
        for i in reversed(range(len(self.A)//2)):
            self.siftDown(i)        
        
    def siftDown(self, i):
        maxIndex = i
        l = (2*i) + 1 # leftchild
        if l <= len(self.A) - 1 and self.A[l] > self.A[maxIndex]:
            maxIndex = l
            
        r = (2*i) + 2 # rightchild
        if r <= len(self.A) - 1 and self.A[r] > self.A[maxIndex]:
            maxIndex = r   
            
        if i != maxIndex: # Meaning one of the child is greater because maxIndex = i in the beginning
            self.A[i], self.A[maxIndex] = self.A[maxIndex], self.A[i]
            self.siftDown(maxIndex)
            
    def siftUp(self, i):
        parent_i = (i - 1)//2  # parent
        while parent_i >= 0 and self.A[parent_i] < self.A[i]:           
            self.A[parent_i], self.A[i] = self.A[i], self.A[parent_i]
            i = parent_i 
            parent_i = (i - 1)//2  # parent
                
    def extractMax(self):
        result = self.A[0]
        self.A[0] = self.A[len(self.A) - 1]
        del(self.A[len(self.A) - 1])     
        self.siftDown(0)
        return result

    def getMax(self):
        result = self.A[0]
        return result
            
    def insert(self, p):
        self.A.append(p)
        self.siftUp(len(self.A) - 1)

    def remove(self, p):
        i = self.A.index(p)
        self.A[i] = float('inf')
        self.siftUp(i)
        self.extractMax()
        
if __name__ == '__main__':
    
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
    
    H = Maxheap(A)  
    H.remove(12)       
    print(H.A)
    print(H.extractMax())
    print(H.extractMax())
    H.insert(10)    
    print(H.extractMax())           
```
