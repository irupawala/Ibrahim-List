
# python3 program for power set
 
import math;
 
def printPowerSet(set,set_size):
     
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int) (math.pow(2, set_size));
    counter = 0;
    j = 0;
     
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        print(f"=================counter============== = {counter}")
        for j in range(0, set_size):
             
            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set            
            print(f"1<<j = {1<<j}")
            print(f"counter & (1<<j) = {counter & (1<<j)}")
            if((counter & (1 << j)) > 0):
                print("=======True========")
                print(set[j], end = "");
        print("");
 
# Driver program to test printPowerSet
set = ['a', 'b', 'c'];
printPowerSet(set, 3);
 
# This code is contributed by mits.