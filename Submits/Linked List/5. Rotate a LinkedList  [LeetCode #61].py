# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        rotations = k
        if head is None or head.next is None or rotations <= 0:
            return head

        # find the length and the last node of the list
        last_node = head
        list_length = 1
        while last_node.next is not None:
            last_node = last_node.next
            list_length += 1

        last_node.next = head  # connect the last node with the head to make it a circular list
        rotations %= list_length  # no need to do rotations more than the length of the list
        skip_length = list_length - rotations
        last_node_of_rotated_list = head
        for i in range(skip_length - 1):
            last_node_of_rotated_list = last_node_of_rotated_list.next

        # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
        head = last_node_of_rotated_list.next
        last_node_of_rotated_list.next = None
        return head        

'''
S = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(S.rotateRight(head, 8))
'''

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
