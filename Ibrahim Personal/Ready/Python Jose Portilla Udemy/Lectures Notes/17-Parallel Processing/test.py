from random import random
from multiprocessing import Pool
import timeit

def find_pi(n):
    """
    Function to estimate the value of Pi
    """
    inside=0

    for i in range(0,n):
        x=random()
        y=random()
        if (x*x+y*y)**(0.5)<=1:  # if i falls inside the circle
            inside+=1

    pi=4*inside/n
    return pi

if __name__ == '__main__':
    N = 10**5  # total iterations
    P = 5      # number of processes
    
    p = Pool(P)
    
    
    
    # Note here that the 10*5 iterations are divided in to 5 of list [2000, 2000, 2000, 2000, 2000]
    # now each of this is given to find_pi and the list of pi is obtained [3.14, 3.15, 3.13, 3.16, 3.14]
    # then all of the pi values are summed and divided by P to get the average pi
    # Pi is printed 10 times using lambda
    # All this iterations are timed and the time is given to x which is then printed
    
    
    
    x = timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.7f}'), number=10) # // is used instead of / because we
                                                                            # want integer answer
    #x = timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P}'), number=10) 
        
    #x = timeit.timeit(lambda: print(f'{p.map(find_pi, [N//P]*P)}'), number=10)
    #y = print(f'{p.map(find_pi, [N//P]*P)}')
    #x = timeit.timeit(y)
    
    print(x)
    p.close()
    p.join()
    print(f'{N} total iterations with {P} processes')
