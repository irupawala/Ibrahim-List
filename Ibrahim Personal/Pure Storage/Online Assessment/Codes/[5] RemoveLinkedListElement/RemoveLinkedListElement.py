# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        dummy = ListNode
        dummy.next = head
        prev = dummy
        
        while head is not None:
            if head.val == val:
                _next = head.next
                head.next = None
                prev.next = _next
                head = _next
            else:
                prev = head
                head = head.next
        
        return dummy.next