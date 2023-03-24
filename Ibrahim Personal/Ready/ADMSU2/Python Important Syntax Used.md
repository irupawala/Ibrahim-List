# Python Important Syntax Used 

### Swap elements of array 

```python
a[l], a[k] = a[k], a[l]
```

### Randint

```python
k = random.randint(0, 10)  
```

* Selects random element between 1 and 10

### Randrange

```python
n = random.randrange(0, 100, 1)
```

### range

```python
range(l + 1, r + 1)
```

* iterates through all the elements from l+1 to r+1

* r + 1 because last element is not considered in range 

### Integer Division

* `mid = len(a) // 2` 

* Results will be integer

### To Zip an item to each element of a list

```python
starts = list(zip(starts, cycle('l')))
```

* Here string l is zipped to each element of list starts
* from itertools import cycle to use cycle

### Creating table of coins with all -1

```python
table_of_coins = [-1] * (m + 1)
```

### To print with space without new line

```python
print(x, end=' ')
```

### To print list in reverse order

```python
for x in reversed(sequence):
    print(x, end=' ')
```

### To get minimum of a matrix column

```python
n = min(matrix, key = lambda t: t[1])[0]
```

* comparing the second column and passing off the first column in the sequence

### To find element in a list

```python
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
```

### Build c-style For loop using python using assert statement

```python
n_workers, n_jobs = map(int, input().split())
jobs = list(map(int, input().split()))
assert len(jobs) == n_jobs


#Reference for assert: https://www.w3schools.com/python/ref_keyword_assert.asp#:~:text=The%20assert%20keyword%20is%20used,False%2C%20check%20the%20example%20below.
```

### To apply arguments like min(), sorted() not directly to the array but after applying certain function to it. Key=lambda: 

```python
def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result
```

* See the link - 
  * https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
  * https://stackoverflow.com/questions/13669252/what-is-key-lambda
  * 

### Sys.stdin.readline() will not work in Spyder

* It only works to read text when you run it in a system terminal (i.e. bash or cmd.exe).
* It doesn't work in Spyder because its terminals are implemented in a different technology (PyQt vs. readline).
* https://stackoverflow.com/questions/46671039/reading-stdin-in-spyder
* Enter line k = input("press close to exit") to stop terminal from terminating automatically



### Class Formation

```python 
class TreeOrders():
    def __init__(self, elements):
        self.elements = elements
        self.key = [-1] * self.elements
        self.left = [-1] * self.elements
        self.right = [-1] * self.elements
        
    def PostOrder(self):
        self.result = []
        def PostOrderTraversal(node):
            if node == -1:
                return
            PostOrderTraversal(self.left[node])            
            PostOrderTraversal(self.right[node])
            self.result.append(self.key[node])
            
        PostOrderTraversal(0)
        return(self.result)           
```

### Any number of Inputs without For loop 

```python
def _input():
    data = sys.stdin.read().strip().split('\n') # This means though input is given in separate line they're separated by new line Char '\n'
    n = int(sqrt(len(data))) # n here is thus len of input which is 25
    blocks = []
    for d in data:
        blocks.append(d[1:-1].split(','))
    return n, blocks
```

### Always Create Two Dimensional Arrays using List Comprehensions

```python
# Create Two dimensional array using List Comprehension or for loop. This way you create separate memory for each index in the outer loop. Example

table = [[0 for i in range(len(string2)+1)] for j in range((len(string1) + 1))] 

# If two dimensional array is created like this then each outer loop index only points to the same element (for the inner loop)

table = [[0] * len(string2)] * string1
```

### Infinite in Python3

```python
# Defining a positive infinite integer
positive_infinity = float('inf')
print('Positive Infinity: ', positive_infinity)
 
# Defining a negative infinite integer
negative_infinity = float('-inf')
print('Negative Infinity: ', negative_infinity)
```

### Heapq (Priority Queue in Python)

``` python
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
```

### Function definition with type of each variable

```python
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    pass
```

### Sorting of a List

```python
# The sort method changes the order of a list permanently. The sorted() function returns a copy of the list, leaving the original list unchanged.

# In-place sorting

l = [3,2,1]
l.sort()
l.sort(reverse=True)
print(l)

# Out of place sorting

l = [3,2,1]
k = sorted(l)
k = sorted(l, reverse=True)
print(k)

# Reversing a list

l.reverse()
```

### Stack O(1) operations - deque

```python
from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')
print(q[0])

q.pop()
print(len(q)) or print(bool(q))
print(list(q))
print(len(q))
```

### Queue O(1) operations - deque

```python
from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

q.popleft()
print(q[0])

print(len(q)) or print(bool(q))
print(list(q))
print(len(q))
```

### Time for a Code

```python
import time

start = time.time()
print(time.time() - start)
```

### ASCII Value of a Char

```	python
# To Get the ASCII:
>> ord('a')
97
# To get the Char from ASCII
>> chr(97)
'a'
```

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\ADMSU2\Python Important Syntax Images\ASCII.PNG)

### Deep Copy a List

```python
lista = list_b[:]	
```

### Exceptions

Place code that might cause an error in the try block. Code that should run only if the try block was successful goes in the else block.

```python
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing")  
finally:
    print("Always execute this code")
```

![](C:\Users\1000249643\Desktop\Desktop\Programming Langauages\Ready\ADMSU2\Python Important Syntax Images\try_except_else_finally.a7fac6c36c55.png)

### Working with files

#### Reading a file and storing its lines

```python
filename = 'siddhartha.txt'
with open(filename) as file_obj:
    lines = file_obj.readlines()
    
for line in lines:
    print(line)
```

#### Writing a file

```python
filename = 'journal.txt'
with open(filename, 'w') as file_obj:
    file_obj.write("I love programming")
```

#### Appending a file

```python
filename = 'journal.txt'
with open(filename, 'a') as file_obj:
    file_obj.write("\nI love making games")
```

### Difference between sys.stdin.read(), readlines(), readline()

#### sys.stdin.read()

```python
# f.read() reads the file as an individual string. It will only terminate taking input when you input Ctrl + Z

# To get the inputs from read() in a list one need to use the split()

import sys

if __name__ == "__main__":
    input = sys.stdin.read()
    x = list(map(int, input.split()))
    print(x)
```

#### sys.stdin.readlines()

```python
# Use readlines() when each input appears in a separate line. NO NEED to use split()
# No " " is allowed while using readlines()

import sys

if __name__ == "__main__":
    input = sys.stdin.readlines()
    x = list(map(int, input))
    print(x)
```

#### sys.stdin.readline()

```python
# readline just reads one line. 
# This is very helpful when getting the specific number of inputs from the STDIN

import sys

if __name__ == "__main__":
    commands_list = []
    for x in range(4):
        input = sys.stdin.readline()
        commands_list.append(input.split())
    print(commands_list)
```

### Using sys.stdout.write()

```python
# Need to convert the argument to string before passing to write()
sys.stdout.write(str(self.stack2[len(self.stack2)-1]) + "\n")  

print(x) # is equivalent to 
print(str(x) + "\n")
```

### To Iterate List in Circular fashion

```python
l1 = ["I", "B", "U"]

i = 0
while i < len(l1):
    print (l1[i])
    i = (i+1)%len(l1)
```

### String Replace

```python
l1 = "IBRAHIM"

l1 = l1.replace("I", "E")
print(l1)
```

### Why Set is much faster then list in Python

* Sets are implemented using hash tables which has O(1) lookup time. Hence, the speed of this operation does not depend on the size of the set.
* Python lists are implemented using dynamic arrays which takes O(n) time in the worst case when whole list needs to be searched, which will become slower as the list grows.
* Note that sets are not faster than lists per se, but only if you have to handle a lot of elements.

### Max Heap

```python
class Maxheap():
    
    def __init__(self, A):
        self.A = A
        self.size = len(self.A) 
        self.buildHeap()

    def siftDown(self, i):
        maxIndex = i
        l = (2*i) + 1 # leftchild
        if l <= self.size - 1 and self.A[l] > self.A[maxIndex]:
            maxIndex = l
            
        r = (2*i) + 2 # rightchild
        if r <= self.size - 1 and self.A[r] > self.A[maxIndex]:
            maxIndex = r   
            
        if i != maxIndex:
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
#        del(self.A[self.size-1])  
        self.size = self.size-1      
        self.siftDown(0)
        return result

    def getMax(self):
        result = self.A[0]
        return result

    def buildHeap(self): # Turns array into heap
        for i in reversed(range(self.size//2)):
            self.siftDown(i)
            
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
    H.remove(8)
    H.remove(11)    
    H.remove(12)    
    H.remove(10)    
    print(H.A)
    print(H.extractMax())
    print(H.extractMax())
    print(H.extractMax())    
    H.insert(12)
    H.insert(11)
    H.insert(10)    
    print(H.extractMax())    
    print(H.extractMax())   
    print(H.extractMax())           
```

### Change Stack size and Run the code as an external thread

```python
import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26) # new thread will get stack of such size

def main():
    pass

threading.Thread(target=main()).start()
```

### Python get() Method

* The get method returns the value of the item with specified key.

* | Parameter | Description                                                  |
  | --------- | ------------------------------------------------------------ |
  | *keyname* | Required. The keyname of the item you want to return the value from |
  | *value*   | Optional. A value to return if the specified key does not exist. Default value None |

```python 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
```

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)
```

* Get method can be used to check if the key does not exists like this.

```python
freq = {} #maps each character to its frequency

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1
```

### Max Heap and Min Heap using built-in heapq functions

**Min Heap**

```python
import heapq

# Creating empty heap
heap = []
heapq.heapify(heap)

# Adding items to the heap using heappush function
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)
heapq.heappush(heap, 100)

# printing the value of minimum element
print("Head value of heap : "+str(heap[0]))
 
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
print("\n")
 
element = heapq.heappop(heap)

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
```

**Max Heap**

```python
import heapq

# Creating empty heap
heap = []
heapq.heapify(heap)

# Adding items to the heap using heappush function
heapq.heappush(heap, -10)
heapq.heappush(heap, -30)
heapq.heappush(heap, -20)
heapq.heappush(heap, -100)

# printing the value of minimum element
print("Head value of heap : "+str(heap[0]))
 
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-i, end = ' ')
print("\n")
 
element = heapq.heappop(heap)
 
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-i, end = ' ')
```

### Max and Min Heap using built-in PriorityQueue

**Min Heap**

```python 
import queue

heap = queue.PriorityQueue()

heap.put(10)
heap.put(20)
heap.put(30)
heap.put(100)

print(heap.queue[0])
print(heap.queue)
print(heap.get())
print(heap.queue)
print(heap.get())
print(heap.queue)
```

**Max Heap**

```python
import queue

heap = queue.PriorityQueue()

heap.put(-10)
heap.put(-20)
heap.put(-30)
heap.put(-100)

for i in heap.queue:
    print(-i, end = ' ')
```

* The `PriorityQueue` uses the same `heapq` implementation from 2) internally and thus has the same time complexity. However, it is different in two key ways. Firstly, it is *synchronized,* so it supports concurrent processes (you can read more about [here](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/)). Secondly, it is a `class` interface instead of the `function` based interface of `heapq` . Thus, `PriorityQueue` is the classic OOP style of implementing and using Priority Queues.

### Disjoint Sets (Union Find) Algorithm 

* In this code note that you need to pass the list of values for which disjoint sets needs to be created
* Runs all operations in constant amortized time

```python 
class Node:
    def __init__(self, id, parent, rank):
        self.id = id
        self.rank = rank
        self.parent = parent
        self.weight = 1 # Stores the number of elements in this set
        
class Disjointsets:
    def __init__(self, list_nodes):
        self.disjoint_sets = {}      
        for x in set(list_nodes):
            self.disjoint_sets[str(x)] = self.makeset(x)
            
    def makeset(self, x):
        return Node(x, x, 0)
            
    def find(self, x):
        node_x = self.disjoint_sets[str(x)]
        
        # keep on recursively calling find untill root node is not found
        if node_x.parent != x: 
            node_x.parent = self.find(node_x.parent)          
        return node_x.parent    
            
    def union(self, u, v):       
        root_u, root_v = self.find(u), self.find(v)  
        if root_u == root_v: # Both have same root hence elements are already in same set 
            return
        
        root_node_u, root_node_v = self.disjoint_sets[str(root_u)], self.disjoint_sets[str(root_v)]     

        if root_node_u.rank < root_node_v.rank:
            root_node_u.parent = root_v
            root_node_v.weight = root_node_u.weight + root_node_v.weight
            
        else:
            root_node_v.parent = root_u
            root_node_u.weight = root_node_u.weight + root_node_v.weight
            if root_node_u.rank == root_node_v.rank:
                root_node_u.rank += 1       
                
if __name__ == "__main__":
    
    gb = [[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]
    
    nodes_list = []
    for x in gb: nodes_list.extend(x)
    
    D = Disjointsets(nodes_list)    
    for (u, v) in gb:
        D.union(u, v)
              
```

### Python List cannot be modified at the same time while iterating over it

Note, though, that one cannot iterate over the list and modify it at the same time; to do that, you should instead iterate over a slice of the list (which is basically a copy of the list). As in:

```python
 for item in lst[:]: # Notice the [:] which makes a slice
       # Now we can modify lst, since we are iterating over a copy of it
```

### Named Tuples

- Note that remembering which index to use is tedious for larger codes. Hence namedtuple comes into play

- namedtuple assigns name as well as index to each and every member of the tuple

- Format:

  **variable_name = namedtuple(name of the class, list of all the strings which are attributes - each attribute is separated by a space '')**

```python 
from collections import namedtuple
# Each way of declaring named tuples works
Dog = namedtuple("Dog", "age breed name")
#Dog = namedtuple("Dog", "age, breed, name")
#Dog = namedtuple("Dog", ["age", "breed", "name"])
sam = Dog(age=2, breed = "Lab", name="Sammy")
print(sam)
print(sam.age)
print(sam.breed)
print(sam[1])
print(sam[2])
```

### *args

* When a function parameter starts with an asterisk, it allows for an ***arbitrary** number* of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

```python
def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)
```

### **kwargs

* Similarly, Python offers a way to handle arbitrary numbers of *keyworded* arguments. Instead of creating a tuple of values, `**kwargs` builds a dictionary of key/value pairs. For example:

```python
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")
        
myfunc(fruit="apple", veggie = "lettuce")
```

### Appendleft

* Note that using deque() one can also appendleft() just like popleft()

```python
from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')
q.appendleft('0')
q.appendleft('1')
q.appendlef('2')

q.popleft()
print(q[0])

print(len(q)) or print(bool(q))
print(list(q))
print(len(q))
```

### How to use int() to convert decimal, octal and hexadecimal to int?

* https://www.programiz.com/python-programming/methods/built-in/int

```python
# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))
print("For 0b1010, int is:", int('0b1010', 2))
print(int("1000",2))
print(int("0b1000",2))

# octal 0o or 0O
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))
print(int("12",8))
print(int("0O12",8))

# hexadecimal
print("For A, int is:", int('A', 16))
print("For 0xA, int is:", int('0xA', 16))
print(int("F",16))
print(int("0XF",16))
```



### String Padding

* %32s %n, where n is the object and s is the type of the object. 32 is how long the final ans will be 

* If object is binary use b. If object is string use s

```python
n = 43261596 
n = bin(n)[2:]         # convert to binary, and remove the usual 0b prefix
n = '%32.0s' %n         # print number into a pre-formatted string with space-padding
n = n.replace(' ','0') # Convert the useful space-padding into zeros
print(n)


```

