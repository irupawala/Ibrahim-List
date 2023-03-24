'''
We want to implement a callback Mechanism that allows listeners to register a fucntion that will be invoked when the event fires.

The API functions are register_callback and event_fired.

    1. There is only one event and it will be fired only once.
    2. Callbacks registered before the event fires shouldn't block waiting for the event to fire.
    3. Callbacks registered after the event fires should get invoked ASAP.
    
    
- Callbacks are the threads coming at any time interval continuosly.
- We have an Eventfire (Event handler) which has two methods
    1. reg_cb: this method keeps on saving the callbacks before the event gets fired at a particular time
    2. fire: when the event fires all the previous callbacks are executed at once, after this all the 
    incoming callbacks will be executed immediately
'''

from threading import Thread 
from threading import Condition 
from threading import current_thread
import time
from collections import deque

class CallBack():
    def __init__(self, arrived_at, name):
        self.arrived_at = arrived_at
        self.name = name
    
    def call(self):
        print("Hi, I am callback {0} arrived at {1}, thread name is {2}\n".format(self.name, self.arrived_at, current_thread().getName()), flush=True)

class Eventfire():
    def __init__(self):
        self.queue = deque()
        self.isEventFired = False
        self.cond = Condition()
        #print("Thread is {0}".format(current_thread().getName()))
    
    def reg_cb(self, cb):
        # implement this
        # print("RegCB Thread is {0}".format(current_thread().getName()))
        if not self.isEventFired:
            self.queue.append(cb)
            print("callback {0} stored in the queue".format(cb.name))
        else:
            print("callback {0} executed immediately".format(cb.name))
            cb.call()   
            
    
    def fire(self):
        # implement this
        while len(self.queue) != 0 :
            cb = self.queue.popleft()
            print("callback {0} I am after Eventfired".format(cb.name))
            cb.call()
        
        #print("FIRE Thread is {0}".format(current_thread().getName()))
        self.isEventFired = True
        print("Eventfired = {0}\n".format(self.isEventFired))
 
    
def register(Event):
    Event.reg_cb(cb1)
    Event.reg_cb(cb2)
    Event.reg_cb(cb3)
    Event.fire()
    Event.reg_cb(cb4)
    Event.reg_cb(cb5)
    

if __name__ == "__main__":

    cb1 = CallBack(1, "cb1")
    cb2 = CallBack(2, "cb2")
    cb3 = CallBack(3, "cb3")
    cb4 = CallBack(4, "cb4")
    cb5 = CallBack(5, "cb5")
    
    Event = Eventfire()
    e = Thread(target=register, args=(Event,), name = "Thread1", daemon = True)
    e.start()
    e.join()
    print("I am currently in {}".format(current_thread().getName()))
    print("Main thread exiting")
    
    
'''
Without lock there are many issues if this code is multithreaded. Let's say if some thread thread1 is executing reg_cb() and 
if after self.isEventFired statement line #42 another thread thread2 executes fire() and changes self.isEventFired = True 
now as the event is fired only once the cb of thread1 will get enqueued in the queue and will never get executed.

'''    
    