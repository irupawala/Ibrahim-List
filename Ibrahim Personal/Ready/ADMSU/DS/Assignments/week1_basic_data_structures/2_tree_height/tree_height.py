# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        print(f"Before for loop ----  max_height = {max_height}")
        height = 0
        current = vertex
        while current != -1:
            print(f"Start of while loop xxxxxxxxxxx height = {height}, max_height = {max_height},  current = {current}")
            height += 1
            current = parents[current]
            print(f"Start of while loop kkkkkkkkkkkkkkkk height = {height}, max_height = {max_height},  current = {current}")
        max_height = max(max_height, height)
        
        print(f"After for loop oooooooooooooooooooooooooooooooooooooooo height = {height}, max_height = {max_height},  current = {current} \n")
    return max_height


def main():
    n = int(input("Enter the number of nodes = "))
    parents = list(map(int, input("Enter the value of nodes = ").split()))
#    n = int(input())
#    parents = list(map(int, input().split()))    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()


if __name__ == "__main__":
    main()
    
    
    
''' 

5 -1 0 4 0 3

'''