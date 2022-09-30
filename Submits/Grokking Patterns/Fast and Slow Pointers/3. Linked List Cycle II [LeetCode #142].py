# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        
        # find the LinkedList cycle
        cycle_length = 0 # default case when cycle_length is 0
        slow, fast = head, head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:  # found the cycle
                cycle_length = self.calculate_cycle_length(slow)
                break
        return self.find_start(head, cycle_length) if cycle_length != 0 else None 
    
    def calculate_cycle_length(self, slow):
        cycle_length = 0
        current = slow
        while True:
            current = current.next
            cycle_length += 1
            if current == slow:
                return cycle_length
            
    def find_start(self, head, cycle_length):
        pointer1, pointer2 = head, head
        
        # offsetting end by start + cycle_length
        for i in range(cycle_length):
            pointer2 = pointer2.next
        
        # increment both pointers until they meet at the start of the cycle
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return pointer1
        
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
