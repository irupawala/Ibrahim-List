class Solution:
    def totalFruit(self, fruits) -> int:
        window_start, max_no_fruits, window_len = 0, 0, 2
        type_of_fruits = {}
        
        for window_end in range(len(fruits)):

            right_fruit = fruits[window_end]
            if right_fruit not in type_of_fruits: 
                type_of_fruits[right_fruit] = 0
            type_of_fruits[right_fruit] += 1

            # shrink the window till type_of_fruits reduces to 2
            while len(type_of_fruits) > window_len:
                left_fruit = fruits[window_start]
                type_of_fruits[left_fruit] -= 1
                if type_of_fruits[left_fruit] == 0:
                    del type_of_fruits[left_fruit]
                window_start += 1

            max_no_fruits = max(max_no_fruits, window_end-window_start+1)
                
        return max_no_fruits
                
S = Solution()
print(S.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

'''
Time Complexity - O(N+N) =~ O(N)
Space Complexity - O(1) as there can be a maximum of three types of fruits stored in the frequency map.
'''
