# NeetCode Solution
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
'''


# Ibrahim Solution
class Solution:
    def mergeTriplets(self, triplets, target):
        target_trip = [None, None, None]
        # 1st element
        for trip in triplets:
            if trip[0] == target[0]:
                if trip[1] <= target[1] and trip[2] <= target[2]:
                    target_trip = trip
                    
        # 2nd element
        for trip in triplets:
            if trip == target_trip:
                continue
            if trip[1] == target[1]:
                if trip[0] <= target[0] and trip[2] <= target[2]:
                    target_trip[1] = target[1]
                    break
                    
        # 3rd element 
        for trip in triplets:
            if trip == target_trip:
                continue
            if trip[2] == target[2]:
                if trip[0] <= target[0] and trip[1] <= target[1]:
                    target_trip[2] = target[2]
                    break
        
        if target_trip == target: return True
        return False
    
#S = Solution()
#print(S.mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))


'''
Time Complexity - O(3n)
Space Complexity - O(1)
'''
