# Queue

* First In First Out Structure (FIFO).

![Queue Data Structure | Studytonight](https://static.studytonight.com/data-structures/images/introduction-to-queue.png)

## Time for Common Operations

* All operations Enqueue(), Dequeue() and Empty are O(1).

## When to Use ?

* Use a queue when you want to get things out in the order that you put them in.

## Python Implementation

- Can be Implemented with either array or linked list. But for efficiency use deque inbuilt function.

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

