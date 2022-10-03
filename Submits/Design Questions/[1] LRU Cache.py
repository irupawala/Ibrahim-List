class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None
        
    
class LRUCache:
    def __init__(self, capacity):
        self.cache = {} # map key to node
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    # remove node from doubly linked list
    def remove(self, node):      
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
        
    # insert node at right in doubly linked list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev          
    
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)           

'''
Time Complexity - O(1) both for put and get
Space Complexity - O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.

'''        
        