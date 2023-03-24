"""
This is the implementation without the first row with all zeroes
"""



def knapSackNoRepeat(total_weight):
    
    for w in range(1, total_weight+1):
        if bars_weight[0] <= w:
            memoization_table[0][w] = bars_weight[0]
    
    for i in range(1, no_of_bars):
        for w in range(1, total_weight+1):
        
             memoization_table[i][w] = memoization_table[i-1][w] # excluding the current bars_weight 
             
             # including the current bars_weight 
             wi = bars_weight[i]
             if wi <= w:
                 W = memoization_table[i-1][w-wi] + wi # Repetition not allowed. WE are never calculating weight considering the best acheieved in the same row thus repetition is NOT Allowed
#                 W = memoization_table[i][w-wi] + wi # Repetition is allowed
                 
                 if memoization_table[i][w] < W:
                     memoization_table[i][w] = W
                                
    return memoization_table[no_of_bars-1][total_weight]

if __name__ == "__main__":

    total_weight, no_of_bars = 13, 3
    bars_weight = [1,4,8]    
  
    memoization_table = [[0 for x in range(total_weight+1)] for y in range(no_of_bars)]
    print(knapSackNoRepeat(total_weight))
    

'''
The above solution has the time and space complexity of O(N*C), where ‘N’ represents total items, and ‘C’ is the maximum capacity.    
'''