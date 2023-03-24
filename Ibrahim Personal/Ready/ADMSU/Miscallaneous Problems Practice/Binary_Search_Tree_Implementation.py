class Node():
    def __init__(self, node):
       self.key = node
       self.parent = None
       self.leftChild = None
       self.rightChild = None

class BinarySearchTree():
    
    def __init__(self, array):
        self.root = None
        
        for x in array:
            self.Insert(x)
       
    # Returns the key where the node should be inserted when the key is not found    
    def Find(self, x, root):
        if root.key == x:
            return root
        elif root.key > x:
            if root.leftChild != None: # Go more deep only if leftChild is None
                return self.Find(x, root.leftChild)
            return root # return the last node if the intended node is not present
        elif root.key < x:
            if root.rightChild != None:
                return self.Find(x, root.rightChild)
            return root       
        
    def Insert(self, x):
        if self.root == None:
            self.root = Node(x)
        else:
            insert_node = self.Find(x, self.root)
            if insert_node.key != x: # Ensures that the node you're trying to insert is not already present
                node = Node(x)
                if insert_node.key > node.key: 
                    insert_node.leftChild = node                   
                else:
                    insert_node.rightChild = node  
                node.parent = insert_node
            
    def Next(self, x):
        N = self.Find(x, self.root)
        if x != N.key: # If x is not found return the Find element because that's the place where x should be inserted
            return N
        if N.rightChild != None: # If there is no rightChild then the next is extreme leftChild of N.right
            return self.leftDescendant(N.rightChild)
        else:
            if N.key > x: # If x is not in the tree return the last biggest node
                return N
            return self.rightAncestor(N) # If not right child then the next smallest is an ancestor
        
    def leftDescendant(self, N):
        if N.leftChild == None:
            return N
        else:
            return self.leftDescendant(N.leftChild)
        
    def rightAncestor(self, N):
        if N.parent == None:
            return Node(None) # Reached the root node hence there is no Next element
        if N.key < N.parent.key:
            return N.parent
        else:
            return self.rightAncestor(N.parent)
     
    def rangeSearch(self, x, y):
        L = []
        N = self.Find(x, self.root)
        while N.key <= y:
            if N.key >= x:
                L.append(N.key)
            N = self.Next(N.key)
        return L
     
if __name__ == "__main__":
#    array = list(map(int, input().split()))
#    print(array)
    
    array = [7, 4, 13, 1, 6, 10, 15]
    bst = BinarySearchTree(array)
    
    find_key = bst.Find(9, bst.root).key
    print(find_key)
    
    next_key = bst.Next(15).key
    print(next_key)
    
    list_range = bst.rangeSearch(5,12)
    print(list_range)
