'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''

class Solution:
    def copyRandomList(self, head):
        if head is None: return None
        
        deep_copy = {None: None}
        
        current = head        
        while current:
            copy_node = Node(current.val)
            deep_copy[current] = copy_node
            current = current.next
        
        current = head
        while current:
            copy_node = deep_copy[current]
            copy_node.next = deep_copy[current.next]
            copy_node.random = deep_copy[current.random]
            current = current.next
        return deep_copy[head]
        
        
'''
S = Solution()
head1 = Node(3)
head2 = Node(3)
head3 = Node(3)
head1.next = head2
head2.next = head3
head1.random = None
head2.random = head1
head3.random = None

print(S.copyRandomList(head1))
'''

'''
Time Complexity - O(N)
Space Complexity - O(N)
'''
