# LeetCode Link - https://leetcode.com/problems/ipo/

from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) :
        minCapitalHeap = []
        maxProfitHeap = []

        # insert all project capitals to a min-heap
        for i in range(0, len(profits)):
            heappush(minCapitalHeap, (capital[i], i))

        # let's try to find a total of 'k' best projects
        availableCapital = w
        for _ in range(k):
            # find all projects that can be selected within the available capital and insert them in a max-heap
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                capital, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-profits[i], i))

            # terminate if we are not able to find any project that can be completed within the available capital
            if not maxProfitHeap:
                break

            # select the project with the maximum profit
            availableCapital += -heappop(maxProfitHeap)[0]

        return availableCapital        
    
S = Solution()
#print(S.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
print(S.findMaximizedCapital(3, 0, [1,5,3,6,1], [0,1,2,1,2])) # Notice this test-case, Max-Heap always contains the previous projects with MaxProfits from lower availableCapital, this will help the scenario when the project with less capital has more profit than new higher availableCapital

'''
Time Complexity - O(NlogN+KlogN),where ‘N’ is the total number of projects and ‘K’ is the number of projects we are selecting.
Space Complexity - O(N)
'''
