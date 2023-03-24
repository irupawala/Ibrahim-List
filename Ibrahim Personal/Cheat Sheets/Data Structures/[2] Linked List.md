# Linked List

* A Linked List consists of nodes where each node contains a data field (Key) and a pointer to the next node in the list.
* Singly-Linked List consists of key and next pointer.
* Doubly-Linked List consists of key, next pointer and previous pointer.

![1642541260695](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1642541260695.png)

## Time for common Operations

|      Operations      |  Singly Linked List  |  Doubly Linked List  |
| :------------------: | :------------------: | :------------------: |
|    PushFront(Key)    |         O(1)         |         O(1)         |
|      TopFront()      |         O(1)         |         O(1)         |
|      PopFront()      |         O(1)         |         O(1)         |
|    PushBack(Key)     | O(n), O(1) with Tail | O(n), O(1) with Tail |
|      TopBack()       | O(n), O(1) with Tail | O(n), O(1) with Tail |
|      PopBack()       |         O(n)         |         O(1)         |
|      Find(Key)       |         O(n)         |         O(n)         |
|      Erase(Key)      |         O(n)         |         O(n)         |
|       Empty()        |         O(1)         |         O(1)         |
| AddBefore(Node, Key) |         O(n)         |         O(1)         |
| AddAfter(Node, Key)  |         O(1)         |         O(1)         |

## When to use ?

* When you need constant time insertions/ deletions from front and back (with doubly-linked and tail)
* You don't know how many items will be there. With arrays, you may need to re-declare and copy memory if the array grows too big. DOESN'T APPLY TO PYTHON LISTS !
* You don't need random access to any elements. O(n) time to find(Key)

## Python Implementation

```python
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 12:36:49 2022

@author: 1000249643
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        
        if values is not None:
            for value in values:
                self.PushBack(value)
                
    def PushBack(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def PopBack(self):
        old_tail = self.tail
        new_tail = self.tail.prev
        new_tail.next = None
        old_tail.prev = None
        self.tail = new_tail
        print(f"{old_tail.data} removed")
        del(old_tail)

    def PopFront(self):
        old_head = self.head
        new_head = self.head.next
        new_head.prev = None
        old_head.next = None
        self.head = new_head
        print(f"{old_head.data} removed")
        del(old_head)

    def PushFront(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def PrintList(self):
        printval = self.head
        while printval:
            print(printval.data, end = " ")
            printval = printval.next
        print("")
            
    def Find(self, key):
        current_node = self.head
        while current_node.data != key:
            current_node = current_node.next
        return current_node
            
    def AddAfter(self, value, key):
        node = Node(value)
        insert_after_node = self.Find(key)
        if insert_after_node:
            node.next = insert_after_node.next
            node.prev = insert_after_node
            insert_after_node.next = node
            if node.next:
                node.next.prev = node
            else:
                self.tail = node
            
    def Remove(self, key):
        removed_node = self.Find(key)
        removed_node.next.prev = removed_node.prev
        removed_node.prev.next = removed_node.next
        removed_node.next = None
        removed_node.prev = None
        print(f"{removed_node.data} removed")
        del removed_node

if __name__ == "__main__":
    L = DoublyLinkedList([1, 2, 3])
    L.PushBack(5)
    L.PushFront(0)
    L.AddAfter(4, 3)
    L.AddAfter(6, 5)
    print(L.tail.data)
    L.PrintList()
    L.PopBack()
    L.PopFront()
    L.Remove(4)
    L.PrintList()
```

