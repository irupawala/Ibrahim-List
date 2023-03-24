# python3 program for power set
 
import math
def printPowerSet(set):

    set_size = len(set)
    pow_set_size = (int) (math.pow(2, set_size)) # set_size of power set of a set with set_size n is (2**n -1)
    power_set = []
     
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size): # Inner loop (1<<j) always produces 1,2,4... binary and with 1,2,3,4... produces binary representation of 1,2,4.. 
        subset = [] # for adding the elements contained in subset 
        for j in range(0, set_size):
            if((counter & (1 << j)) > 0):  # Check if jth bit in the counter is set If set then print jth element from set        
                subset.append(set[j])
        power_set.append(subset) 
    return power_set

#set = ['a', 'b', 'c']
set = range(1,5)
#print(printPowerSet(set))

print("\n".join(map(str,printPowerSet(set))))

