# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# LeetCode Link - https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = self.reverse_list(slow)
        copy_head_second_half = head2 # If the node is not copied and left hanging it will be deleted from the memory
        
        
        while head1 and head2:
            #print(head1.val, head2.val)
            if head1.val != head2.val: break
            head1 = head1.next
            head2 = head2.next
        
        # Returning List again in the original condition
        self.reverse_list(copy_head_second_half)
        if head1 is None or head2 is None:  # if both halves match
            return True

        return False

    
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
