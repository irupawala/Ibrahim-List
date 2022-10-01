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
from collections import deque
from threading import Lock
import time

class CallBack():
    def __init__(self, arrived_at, name):
        self.arrived_at = arrived_at
        self.name = name
    
    def call(self):
        #print("Hi, I am callback {0} arrived at {1}, thread name is {2}\n".format(self.name, self.arrived_at, current_thread().getName()), flush=True)
        pass
    
class Eventfire():
    def __init__(self):
        self.queue = deque()
        self.isEventFired = False
        self.cond = Condition()
        self.lock = Lock()
        #print("Thread is {0}".format(current_thread().getName()))
    
    def reg_cb(self, cb):
        self.lock.acquire()
        if not self.isEventFired:
            self.queue.append(cb)
            print("callback {0} stored in the queue, thread name is {1}\n".format(cb.name, current_thread().getName()), flush=True)
            self.lock.release()
        else:
            self.lock.release()
            print("callback {0} executed immediately, thread name is {1}\n".format(cb.name, current_thread().getName()), flush=True)
            cb.call()   

    
    def fire(self):
        print("----------------- Event Fired -----------------")
        self.lock.acquire()
        time.sleep(1)
        while len(self.queue) != 0:
            cb = self.queue.popleft()
            print("callback {0} I am after Eventfired, thread name is {1}\n".format(cb.name, current_thread().getName()), flush=True)
            self.lock.release()
            cb.call()
            self.lock.acquire()
            
        print("-------------Queue is empty now------------------")
        self.isEventFired = True
        print("Eventfired = {0}, thread name is {1}\n".format(self.isEventFired, current_thread().getName()), flush=True)        
        self.lock.release()
    
def register1(Event):
    time.sleep(0)
    Event.reg_cb(cb1)
    time.sleep(0.2)
    Event.reg_cb(cb2)
    time.sleep(0.5)
    Event.reg_cb(cb3)
    #Event.fire()
    Event.reg_cb(cb4)
    Event.reg_cb(cb5)
    Event.reg_cb(cb6)
    Event.reg_cb(cb7)    
    
def register2(Event):
    time.sleep(0)
    Event.reg_cb(cb1)
    Event.reg_cb(cb2)
    time.sleep(0.5)
    Event.reg_cb(cb3)
    Event.fire()
    Event.reg_cb(cb4)
    Event.reg_cb(cb5)
    Event.reg_cb(cb6)
    Event.reg_cb(cb7)   
    

if __name__ == "__main__":

    cb1 = CallBack(1, "cb1")
    cb2 = CallBack(2, "cb2")
    cb3 = CallBack(3, "cb3")
    cb4 = CallBack(4, "cb4")
    cb5 = CallBack(5, "cb5")
    cb6 = CallBack(5, "cb6")
    cb7 = CallBack(5, "cb7")
    Event = Eventfire()
    e1 = Thread(target=register1, args=(Event,), name = "Thread1", daemon = True)
    e2 = Thread(target=register2, args=(Event,), name = "Thread2", daemon = True)
    e1.start()
    e2.start()
    
    e1.join()
    e2.join()    
    
    print("I am currently in {}".format(current_thread().getName()))
    print("Main thread exiting")
    
    
'''
Points to consider

1. In the reg_cb it is important to acquire lock before enqueue operation as if it is not locked then it is possible that 
after the if not self.isEventFired statement isEventFired is set to True then the cb will get left in the queue without ever executing

2. In the reg_cb one must release the lock before calling the callback as if one thread is taking long and two threads try to acquire the 
lock simultaneously deadlock can be formed.

3. we must lock the process of checking and setting flag, thus no two threads can visit flag at the same time. That means,
when a thread is checking flag, no other threads can change flag. And also when a thread is changing flag, no other theads
can check the flag, they must wait until flag is changed successfully.

4. To insure the order of CallBack is the same, we must also lock the process of checking q.Count and pushing CallBack into 
q. That means, if a thread is checking q.Count, no other threads can push CallBack to the queue. But after checking q.Count,
we can unlock(), so when one thread is running a Callback poped from q, other threads can still add new CallBack to q. And we
will check the q.Count again, so it doesn't affect the order. When one thread is pushing CallBack into q, no other threads can
check q.Count, they must wait until the CallBack is pushed into q.
'''
    