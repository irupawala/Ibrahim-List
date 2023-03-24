# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:15:35 2021

@author: 1000249643
"""

denominations = [1,3,4]


def coinChangeDp(m) :
    
    if m <= 0:
        table_of_coins[m] = 0
        return 0
    
    best = 0
    
    for coin in denominations:
        if (table_of_coins[m] == -1):        
            next = coinChangeDp(m - coin)
        else:
            if (m - coin) >= 0:
                next = table_of_coins[m-coin]
        
        if (best == 0 or best > next + 1):
            best = next + 1
            table_of_coins[m] = best
            
    return best
            

if __name__ == "__main__":
    m = int(input("Enter the amount = "))
    table_of_coins = [-1] * (m+1)
    print(coinChangeDp(m))
    
    

'''

Time Complexity: O(n*m)

n = len(coins)
m = amount
Precisely speaking, the runtime would be a little less than O(n*m). 
If the coin is greater than 1 the inner loop will run (m - coin) iterations instead m, but here we're considering the worst case and ignoring the constant factors.

Space Complexity: O(m)

The extra space is used for caching. The array needs a size of amount to store all the sub-problems' result.

'''