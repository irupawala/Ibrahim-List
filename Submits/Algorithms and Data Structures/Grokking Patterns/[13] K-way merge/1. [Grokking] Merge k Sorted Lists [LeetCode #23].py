# LeetCode Link - https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import *

# Definition for singly-linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = Node()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        if l1: current.next = l1
        if l2: current.next = l2
            
        return dummy.next
    

'''
S = Solution()
head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)
print(S.mergeKLists([head1,head2,head3]))
'''

'''
Time Complexity - O(n.log(k)), where k is number of lists
Space Complexity - O(1)
'''

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __lt__(self, other):
        return self.val < other.val   
  

class Solution:
    def mergeKLists(self, lists) :
        if not lists: return None    

        minHeap = []

        # put the root of each list in the min heap
        for root in lists:
            if root is not None:
                node = Node(root)
                heappush(minHeap, node)       
        
        # take the smallest(top) element form the min-heap and add it to the result
        # if the top element has a next element add it to the heap
        resultHead, resultTail = None, None
        while minHeap:
            node = heappop(minHeap)
            if resultHead is None:
                resultHead = resultTail = node
            else:
                resultTail.next = node
                resultTail = resultTail.next

            if node.next is not None:
                heappush(minHeap, node.next)

        return resultHead               
'''

'''
Time Complexity - O(N.log(K)), where ‘N’ is the total number of elements in all the ‘K’ input arrays.
Space Complexity - O(K)
'''
