from threading import Thread
import time

class Worker:
    
    def __init__(self, work_f):
        self.work = work_f
        # saves work_f to be run later. returns immediately.    
    
    def _execute_thread(self):
        self.work()
        self.cb()
    
    def start(self, callback_f):
        self.cb = callback_f
        t = Thread(target=self._execute_thread)
        t.setDaemon(True)
        pass # start the execution of previously added work_f in a separate thread and register callback_f then return without waiting for either function to finish.
    
class MultiWorker:
    def __init__(self):
        self.work_queue = []
        self.in_progress_cnt = AtomicInt(0)
        self.in_progress_cnt = 0
        
    def add_work(self, work_f):
        # 1- 10k times
        item = Worker(work_f)
        self.work_queue.append(item)
        
    def start(self, callback_f):
        # t_pool = []
        # lock.aquire()
        for i in range(len(self.work_queue)):
            work = self.work_queue[i]
            # is_done =
            self.in_progress_cnt += 1
            work.start(self.finished_callback)
            # t1 = Thread(target=work)
            # t_pool.append()
            # t1.start()
        
        t1 = Worker(work_f = self.check_callback)
        t1.start(callback_f)
        self.work_queue = []
        # lock.release()
        # t2 = Thread(target=callback_f)
        # t2.start()
        
        # #join each thead in the pool
        # for t in t_pool:
        #     t.join()
        # t2.join()
        
    def finished_callback(self):
        self.in_progress_cnt -= 1
        
    def check_callback(self, callback_f):
        while self.in_progress_cnt != 0:
            continue
            
        callback_f()
        
        
# Test situation
def foo():
    time.sleep(100000)
    print("foo done")
    
def bar():
    time.sleep(1)
    print("bar done")
    
def my_cb():
    print("all done")    

def test():
    mw = MultiWorker()
    mw.add_work(bar)
    mw.add_work(bar)
    mw.add_work(bar)
    mw.add_work(bar)
    mw.add_work(bar)
    mw.add_work(bar)
    mw.add_work(foo)
    mw.start(my_cb)
    return

'''
bar done
bar done
bar done
bar done
bar done
bar done
foo done
'''


