# python3

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
        
#if __name__ == '__main__':        
#    
#    n = int(input())
#    tree = TreeOrders(n)
#
#    print(" ".join(str(x) for x in tree.InOrder()))
#    print(" ".join(str(x) for x in tree.PreOrder()))
#    print(" ".join(str(x) for x in tree.PostOrder()))    
#    
     

def main():
    n = int(input())
    tree = TreeOrders(n)

    print(" ".join(str(x) for x in tree.InOrder()))
    print(" ".join(str(x) for x in tree.PreOrder()))
    print(" ".join(str(x) for x in tree.PostOrder()))    
    
threading.Thread(target=main).start()    


  