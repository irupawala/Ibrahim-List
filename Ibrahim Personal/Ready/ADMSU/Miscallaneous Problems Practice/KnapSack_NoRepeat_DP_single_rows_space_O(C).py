"""
- This is a single array implementation of the Knapsack Problem
- This space optimization solution can also be implemented using a single array. 
It is a bit tricky, but the intuition is to use the same array for the previous and the next iteration!
- If you see closely, we need two values from the previous iteration: dp[c] and dp[c-weight[i]]
- When we access dp[c], it has not been overridden yet for the current iteration, so it should be fine.
- dp[c-weight[i]] might be overridden if “weight[i] > 0”. Therefore we can’t use this value for the current iteration.
To solve the second case, we can change our inner loop to process in the reverse direction: c:capacity-->0. 
This will ensure that whenever we change a value in dp[], we will not need it again in the current iteration.
"""


def knapSackNoRepeat(total_weight):
    
    for w in range(1, total_weight+1):
        if bars_weight[0] <= w:
            memoization_table[w] = bars_weight[0]
    
    for i in range(1, no_of_bars):
        for w in range(total_weight, 0, -1): # Using in the reverse direction to avoid using overridden value of dp[c-weight[i]]
        
             memoization_table[w] = memoization_table[w] # excluding the current bars_weight 
             
             # including the current bars_weight 
             wi = bars_weight[i]
             if wi <= w:
                 W = memoization_table[w-wi] + wi # Repetition not allowed. WE are never calculating weight considering the best acheieved in the same row thus repetition is NOT Allowed
#                 W = memoization_table[i][w-wi] + wi # Repetition is allowed
                 
                 if memoization_table[w] < W:
                     memoization_table[w] = W
                                
    return memoization_table[total_weight]

if __name__ == "__main__":

    total_weight, no_of_bars = 13, 3
    bars_weight = [1,4,8]    
  
    memoization_table = [0 for x in range(total_weight+1)]
    print(knapSackNoRepeat(total_weight))
    
'''
The above solution has the time and space complexity of O(C), ‘C’ is the maximum capacity.    
'''