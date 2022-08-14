# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2: return list1
        if not list1: return list2
        if not list2: return list1
        
        newHead = ListNode()
        currentHead = newHead
        head1, head2 = list1, list2
        
        while head1 and head2:
            if head1.val <= head2.val:
                currentHead.next = head1
                head1 = head1.next
            else:
                currentHead.next = head2
                head2 = head2.next     
            currentHead = currentHead.next
        
        if head1: currentHead.next = head1
        if head2: currentHead.next = head2
            
        return newHead.next
                    
'''
Time Complexity - O(n+m)
Space Complexity - O(1)
'''     
