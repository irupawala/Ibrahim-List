# You are given a Worker Class and MultiWorker Class

# Worker Class Description
# start: when start is called and then worker_f will be executed in a new thread
# callback: callback will be executed after the execution of worker_f is finished.callback_f is executed after each worker_f

# MultiWorker Class Desscription
# add_worker: Can be called atleast once (meaning can be called more than one time), in this method worker_f (all incoming functions) needs to be stored in some form. 
# start_all: start_all will execute all worker_f that have been added and mw_callback_f is executed after all worker_f have been executed.
# MultiWorker class not allowed to write threads by itself, it needs to call Worker class methods to create a new Thread

# There will be no more add_worker after start_all is called.
# Non-blocking is required and there can be no busy waiting
# use a for-loop to add each function to a Data structure and remember the size of workers added
# there must be a global variable to remember the number of completed workers n_complete
# we need to add an if statement to check if n_complete is equal to size


from threading import Thread
from threading import Condition 
import time 


class Worker():
    def __init__(self, worker_f):
        self.worker_f = worker_f
        
    def _execute_thread(self):
        self.worker_f()
        self.cb()        
    
    def start(self, callback_f):
        self.cb = callback_f
        t = Thread(target = self._execute_thread, daemon = True)
        t.start()
    
class MultiWorker():
    def __init__(self):
        self.cond = Condition()
        self.work_queue = []
        self.reached_count = 0
        
    
    def add_worker(self, worker_f):
        worker = Worker(worker_f)
        self.work_queue.append(worker)
        
    
    def start_all(self, callback_f): # This should be non-blocking
        self.barrier_size = len(self.work_queue)
        self.released_count = self.barrier_size 
        self.callback_flag = False 
        
        for i in range(self.barrier_size):
            worker = self.work_queue[i]
            worker.start(callback_f)
            
            self.cond.acquire()
                    
            #while self.reached_count == self.barrier_size and not self.callback_flag:
            #    self.cond.wait()
                
            self.reached_count += 1    
            
            if self.reached_count == self.barrier_size:
                self.released_count = self.barrier_size
                
            else:
                while self.reached_count < self.barrier_size:
                    self.cond.wait()
                    
            self.released_count -= 1
            
            if self.released_count == 0:
                #self.reached_count = 0
                callback_f()
                self.callback_flag = True
                
            self.cond.notifyAll()
            self.cond.release()
            

def bar():
    time.sleep(0.1)
    print("bar.done")
    
    
if __name__ == "__main__":
    mw = MultiWorker()
    mw.add_worker(bar)