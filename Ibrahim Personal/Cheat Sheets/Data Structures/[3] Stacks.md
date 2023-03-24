# Stacks

* Last In First Out Structure (LIFO).  

![Stack Implementation Using Array | Code Pumpkin](https://codepumpkin.com/wp-content/uploads/2017/03/stack.bmp)

## Time for Common Operations

* All the operations: Push, Pop, Top and Empty are O(1).

## When to Use ?

* Use a stack when you want to get things out in the reverse order than you put them in.

## Python Implementation

* Can be Implemented with either array or linked list. But for efficiency use deque inbuilt function.

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

