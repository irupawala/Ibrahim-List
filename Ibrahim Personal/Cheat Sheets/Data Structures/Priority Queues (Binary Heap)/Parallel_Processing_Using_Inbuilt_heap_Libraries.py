# python3

##################################################### Main Function ###########################################

import heapq
heap = []         
    

def main_heapq():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    if (n_workers == 0 or n_jobs == 0) :
        print(0)
    else:
        assert len(jobs) == n_jobs, "no of jobs should be similar to that mentioned in line 1"
        for i in range(n_workers):
            worker_finish_time = [0, i]
            heapq.heappush(heap, worker_finish_time)
        
        result = []
        for time in jobs:
            job = heapq.heappop(heap)
            result.append(job[::-1])
            job[0] = job[0] + time 
            heapq.heappush(heap, job)

        for i, j in result:
            print(i, j)

##################################################### Main Function ###########################################

import queue
heap = queue.PriorityQueue()

def main_queue():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    if (n_workers == 0 or n_jobs == 0) :
        print(0)
    else:
        assert len(jobs) == n_jobs, "no of jobs should be similar to that mentioned in line 1"
        for i in range(n_workers):
            worker_finish_time = [0, i]
            heap.put(worker_finish_time)
        
        result = []
        for time in jobs:
            job = heap.get()
            result.append(job[::-1])
            job[0] = job[0] + time 
            heap.put(job)

        for i, j in result:
            print(i, j)


############################################## Test Run  ############################################################
            
if __name__ == "__main__":
    main_heapq()
