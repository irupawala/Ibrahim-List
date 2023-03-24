import random

class Node:
    def __init__(self, val = -1, right = None, bottom = None):
        self.val = val
        self.right = right
        self.bottom = bottom

class Skiplist:
    def __init__(self):
        self.head = Node()

    def flip_coin(self):
        return random.randrange(0, 2)

    def search(self, target: int) -> bool:
        node = self.head

        while node:
            while node.right and target > node.right.val:
                node = node.right
            if node.right and target == node.right.val:
                return True
            node = node.bottom

        return False

    def add(self, num: int) -> None:
        node = self.head
        record_levels = []

        while node:
            while node.right and num > node.right.val:
                node = node.right

            record_levels.append(node)
            node = node.bottom

        new_node = None

        while not new_node or self.flip_coin():
            if len(record_levels) == 0:
                self.head = Node(-1, None, self.head)
                prev_level = self.head
            else:
                prev_level = record_levels.pop()
            new_node = Node(num, prev_level.right, new_node)
            prev_level.right = new_node

    def erase(self, num: int) -> bool:
        node = self.head
        boolean = False

        while node:
            while node.right and num > node.right.val:
                node = node.right

            if node.right and num == node.right.val:
                node.right = node.right.right
                boolean = True
            node = node.bottom

        return boolean
    
    
'''
Time Complexity - O(logn) for Add, Search and Erase
Space Complexity 0 O(n)

- For the time complexity to be minimum the level L1 above the level L0 should have nodes L1nodes = sqrt(L0nodes)
- To acheieve min search time max no of elements in skiplist = log(total_elements)
- Probabilistic Insertion of Elements : To know if the given node is to be added to next upper level decision is made by tosing a coin
- Deletion: Deletion of elements should be done at all levels
- Same asymptotic time complexity as balanced tree and less memory complexity
- Time Complexity T = |L1| + |L0|/|L1|
- When 2 layers time complexity is 2*sqrt(n), when 3 TC = 3*cuberoot(n), .........., when k TC = k*kthroot(n) 
- hence the tiem complexity manipulating all these equations is O(logn)
'''


