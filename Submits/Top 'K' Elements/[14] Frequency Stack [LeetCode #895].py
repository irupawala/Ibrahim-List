from heapq import *

class Element:
    def __init__(self, number, frequency, sequenceNumber):
        self.number = number
        self.frequency = frequency
        self.sequenceNumber = sequenceNumber
        
    def __lt__(self, other):
        # higher frequency wins:
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        # if both elements have same frequency, return the element that was pushed later
        return self.sequenceNumber > other.sequenceNumber        

class FreqStack:

    def __init__(self):
        self.sequenceNumber = 0
        self.maxHeap = []
        self.frequencyMap = {}

    def push(self, num: int) -> None:
        self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
        heappush(self.maxHeap, Element(num, self.frequencyMap[num], self.sequenceNumber))
        self.sequenceNumber += 1

    def pop(self) -> int:
        num = heappop(self.maxHeap).number
        # decrement the frequency or remove if this is the last number
        if self.frequencyMap[num] > 1:
            self.frequencyMap[num] -= 1
        else:
            del self.frequencyMap[num]
        return num            
            

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)

'''
Time Complexity - O(logN)
Space Complexity - O(N)
'''
