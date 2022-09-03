class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize: # Group cannot be divided into groupSize
            return False
        
        count = Counter(hand)
        # print(count)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            
            for i in range(first, first + groupSize):
                if i not in count:
                    return False # group of 3 cannot be made
                
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False # This means that the no which is NOT min gets to 0 and there is a min No in the heap hence the group starting from min no can never be completed.
                    heapq.heappop(minH)
        return True
    
'''
Time Complexity - O(n*logn)
Space Complexity - O(n)
'''

# Ibrahim Solution 
'''
class Solution:
    def isNStraightHand(self, hand, groupSize):
        hand.sort()
        
        while hand:
            num = hand.pop()
            i = 0
            while i < groupSize-1:
                if len(hand)==0 or num-1 not in hand: 
                    return False
                num = num-1
                hand.remove(num)
                i += 1
        return True
'''    
