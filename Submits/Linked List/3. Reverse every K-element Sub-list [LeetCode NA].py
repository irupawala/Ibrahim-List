# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head, k):
        
        if k <= 1 or head is None:
            return head
        
        current, previous = head, None
        while True:
            
            last_node_of_previous_part = previous
            # after reversing the LinkedList 'current' will become the last node of the sub-list
            last_node_of_sub_list = current
            next = None  # will be used to temporarily store the next node
            i = 0
            while current is not None and i < k :  # reverse 'k' nodes
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1

            # connect with the previous part
            if last_node_of_previous_part is not None:
                last_node_of_previous_part.next = previous
            else:
                head = previous

            # connect with the next part
            last_node_of_sub_list.next = current

            if current is None:
                break
            previous = last_node_of_sub_list

        return head 
    
S = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(S.reverseKGroup(head, 3))

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
