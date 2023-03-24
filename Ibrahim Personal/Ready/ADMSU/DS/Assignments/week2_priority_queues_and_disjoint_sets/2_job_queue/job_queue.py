# python3

import os
import sys
import threading
from collections import namedtuple

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(2100000000)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()


'''
Very Interesting problem. Note how a list of two elements can also be pushed in the Heap based on the value of the second element of the list.

Time Complexity - O(n_jobs*log(n_workers))
Space COmplexity - O(n_workers) for the array which contains the heap

'''





AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


##################################################### Fast Implementation ###########################################

class build_threads():
    def __init__(self, n_workers, jobs):
        self.n_workers = n_workers
        self.size = n_workers
        self.jobs = jobs
        self.min_heap = []
        self.result = []
        
    def siftdown(self, i):
        leftChild = (2*i) + 1
        rightChild = (2*i) + 2
#        print(leftChild)
#        print(rightChild)


        minIndex = i

        
        l = leftChild 
        if l < self.size:
            if self.min_heap[l][1] < self.min_heap[minIndex][1]:
                minIndex = l  
            if self.min_heap[l][1] == self.min_heap[minIndex][1]:
                if self.min_heap[l][0] < self.min_heap[minIndex][0]:
                    minIndex = l  
#                    
        r = rightChild 
        if r < self.size:
            if self.min_heap[r][1] < self.min_heap[minIndex][1]:
                minIndex = r  
            if self.min_heap[r][1] == self.min_heap[minIndex][1]:
                if self.min_heap[r][0] < self.min_heap[minIndex][0]:
                    minIndex = r                

        if i != minIndex: # If minIndex and i are equal it means that the node has no childrens
            self.min_heap[i], self.min_heap[minIndex] = self.min_heap[minIndex], self.min_heap[i]
            self.siftdown(minIndex)      
            
            
#        return (self.min_heap[0])
#        print (self.min_heap[0])        
    
    def buid_min_heap(self):
        

        
        for i in range(self.n_workers):
            self.min_heap.append([i, 0])
            
        for j,i in enumerate(self.jobs):
            a = self.min_heap[0].copy()
#            self.result.insert(len(self.result),a)
            self.result.append(a)
            self.min_heap[0][1] += i
            self.siftdown(0)


        return(self.result)
           

##################################################### Naive Implementation ###########################################


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        print(f'next_worker = {next_worker}')
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        print(f'Assigned_Job = {AssignedJob(next_worker, next_free_time[next_worker])}')
        next_free_time[next_worker] += job
#        print(f'next_free_time = {next_free_time[next_worker]}')

    return result



##################################################### Main_naive Function ###########################################
    

def main_naive():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs, "no of jobs should be similar to that mentioned in line 1"
    


    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


##################################################### Main Function ###########################################
    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    if (n_workers == 0 or n_jobs == 0) :
        print(0)
    else:
        assert len(jobs) == n_jobs, "no of jobs should be similar to that mentioned in line 1"
        B = build_threads(n_workers, jobs)
        result = B.buid_min_heap()
        
        for i, j in result:
            print(i, j)
    
    




############################################## Test Run  ############################################################
            
if __name__ == "__main__":
    main()
#    main_naive()

#threading.Thread(target=main).start()
#threading.Thread(target=failed_test).start()    