# Leetcode Link - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head, left, right):
        
        # Skip the first left nodes
        i = 1
        lastNodeBeforeReversal, current = None, head
        while i != left:
            lastNodeBeforeReversal = current
            current = current.next
            i += 1
        
        if lastNodeBeforeReversal is not None: lastNodeBeforeReversal.next = None
        prev, current = current, current.next
        firstNodeInReversal = prev
        
        while i < right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i += 1
            
        if lastNodeBeforeReversal is not None: lastNodeBeforeReversal.next = prev
        else: head = prev # If the reverse begun from left = 1 then have to update head
        firstNodeInReversal.next = current
    
        return head

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
