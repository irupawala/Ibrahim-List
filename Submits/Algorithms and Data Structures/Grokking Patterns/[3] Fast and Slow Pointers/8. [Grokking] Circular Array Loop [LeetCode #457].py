# LeetCode Link - https://leetcode.com/problems/circular-array-loop/

class Solution:
    def circularArrayLoop(self, nums) :
        self.nums = nums
        self.visited = set()

        for i in range(len(nums)): 
            if i not in self.visited:
                self.is_forward = nums[i] >= 0  # if we are moving forward or not
                slow, fast = i, i

                while True:
                    self.visited.add(slow)
                    self.visited.add(fast)
                    
                    # move one step for slow pointer
                    slow = self.find_next_index(slow) 

                    # move two step for fast pointer
                    fast = self.find_next_index(fast) 
                    if (fast != -1): fast = self.find_next_index(fast) 

                    if slow == -1 or fast == -1 or slow == fast: break

                if slow != -1 and fast != -1 and slow == fast: return True             
        
        return False
    
    def find_next_index(self, current_index):
        direction = self.nums[current_index] >= 0
        if direction != self.is_forward: return -1 # change in direction, return -1
        
        next_index = (current_index + self.nums[current_index]) % len(self.nums)
        
        # one element cycle, return -1
        if next_index == current_index: next_index = -1
             
        return next_index
    
'''
Time Complexity - O(N^2)
Time Complexity with self.visited - O(N) # Notice how keeping track of nums visited reduces time immensely
Space Complexity - O(1)
'''
