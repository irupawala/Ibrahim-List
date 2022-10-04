# Definition for singly-linked list.
#class Node:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
        
# LeetCode Link - https://leetcode.com/problems/reorder-list/
        
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head is None or head.next is None:
            return 
        
        # find middle of the LinkedList
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is now pointing to the middle node
        head_first_half = head
        head_second_half = self.reverse_list(slow)  # reverse the second half      
        
        # rearrange to produce the LinkedList in the required order
        while head_first_half is not None and head_second_half is not None:
            temp = head_first_half.next        
            head_first_half.next = head_second_half
            head_first_half = temp
    
            temp = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = temp    

        # set the next of the last node to 'None'
        if head_first_half is not None:
            head_first_half.next = None
    
    def reverse_list(self, head):
        prev, current = None, head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current 
            current = temp
            
        return prev 

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''  
