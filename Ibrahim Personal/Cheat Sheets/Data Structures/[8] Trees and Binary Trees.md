# Trees and Binary Trees

* Trees have one root node and child nodes.
* Some common terminologies are root, child, ancestor, descendant, siblings, leaf, height.
* A Tree structure in which each node has only two children is called Binary Tree.
* When working with trees recursive algorithm is common.
* Tree can be traversed using Bread First Search (BFS) or Depth First Search (DFS).

![Working With Trees. Trees are a hierarchical data structure… | by Michael  Verdi | Medium](https://miro.medium.com/max/677/1*Z89j_NoDx9HkFcPHy3rPZg.png)

## Time for common Operations

* Each Operation has a worst case time of O(Depth)

## When to Use ?

* Store hierarchical data, like folder structure, organization structure, XML/HTML data.

## Python Implementation of Trees Traversal

```python
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
    
class TreeOrders():
    def __init__(self, elements):
        self.elements = elements
        self.key = [-1] * self.elements
        self.left = [-1] * self.elements
        self.right = [-1] * self.elements
        
        for i in range(self.elements):
            keys = list(map(int, input().split()))
            self.key[i] = keys[0]
            self.left[i] = keys[1]
            self.right[i] = keys[2]
            
    def InOrder(self): 
        self.result = [] 
        def InOrderTraversal(node):
            if node == -1:
                return 
            InOrderTraversal(self.left[node])
            self.result.append(self.key[node])
            InOrderTraversal(self.right[node])  
        InOrderTraversal(0)    
        return(self.result)
           
    def PreOrder(self):
       self.result = []
       def PreOrderTraversal(node):
           if node == -1:
               return
           self.result.append(self.key[node])
           PreOrderTraversal(self.left[node])
           PreOrderTraversal(self.right[node])
           
       PreOrderTraversal(0)
       return(self.result)
     
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

def main():
    n = int(input())
    tree = TreeOrders(n)

    print(" ".join(str(x) for x in tree.InOrder()))
    print(" ".join(str(x) for x in tree.PreOrder()))
    print(" ".join(str(x) for x in tree.PostOrder()))    
    
threading.Thread(target=main).start()    
```

