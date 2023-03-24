# Uses python3
import sys
import random

def get_change_recursive(m):
    #write your code here
    
    if m == 0:
        return 0
    
    best = -1
    denominations = [1, 3, 4]
    for coin in denominations:
        if m >= coin:
            next = get_change_recursive(m-coin)
        
        if (best < 0 or best > next + 1):
            best = next + 1
            
    return best



def get_change_dp(m):
    #write your code here
    
    if m == 0:
        table_of_coins[m] = 0 # assign 0 to all values in table
        return 0
    
    best = -1
    denominations = [1, 3, 4] # predefined given in question
    for coin in denominations:
        if m >= coin: # if value is greater then coin go till you find the min recursively. This is necessary because there is no value of m-coin in table for m < coin
            if table_of_coins[m-coin] == -1:
                next = get_change_dp(m-coin) # if there is no value in the table then make a recursive call to the lower m
            else:
                next = table_of_coins[m-coin] # this means that value exists in table
        
        if (best < 0 or best > next + 1): # best < 0 --> first time and best > next + 1 meaning better value can be obtained with table_of_coins[m-coin] + 1 (that coin)
            best = next + 1 # FIND OUT THE BEST RESULT WITH M-COIN AND THEN ADD 1 TO IT TO GET THE BEST M THAT'S HOW DP CRITERIA IS OBTAINED
    
    table_of_coins[m] = best    
    return best
        
if __name__ == '__main__':
    m = int(sys.stdin.read())
#    m = int(input("Enter the value of money = "))
    table_of_coins = [-1] * (m + 1) # creating the table for all the coins and initializing table with -1
    print(get_change_dp(m))
    #print(get_change_recursive(m))



##################################################### Random Tests: #####################################################

'''    
       
    while(1):      
    

        m = random.randrange(0, 20, 1)
        table_of_coins = [-1] * (m + 1) # creating the table for all the coins

        change_recursive = get_change_recursive(m)
        change_dp = get_change_dp(m)
        
        
        print(f'get_change_recursive_{m} = {change_recursive}')        
        print(f'get_change_dp_{m} = {change_dp}')          

        
        if (change_recursive == change_dp):
            print("====OK====")
        else:
            print("===========================================Wrong Answer========================================")
            break
        
'''        
