class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # If this passes it means that a solution does exists and we know from the question that there is only a unique solution
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)): # We should go only till the length of gas because we know that a solution exists from sum(gas) < sum(cost) check hence no need to circle back to starting index
            total += (gas[i] - cost[i])
            
            if total < 0: 
                total = 0
                res = i+1
                
        return res
    
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
