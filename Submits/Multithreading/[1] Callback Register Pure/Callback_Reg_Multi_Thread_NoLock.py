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
        #print("Thread is {0}".format(current_thread().getName()))
    
    def reg_cb(self, cb):
        # implement this
        # print("RegCB Thread is {0}".format(current_thread().getName()))
        if not self.isEventFired:
            self.queue.append(cb)
            print("callback {0} stored in the queue, thread name is {1}\n".format(cb.name, current_thread().getName()), flush=True)
        else:
            print("callback {0} executed immediately, thread name is {1}\n".format(cb.name, current_thread().getName()), flush=True)
            cb.call()   
            
    
    def fire(self):
        # implement this
        print("----------------- Event Fired -----------------")
        while self.queue:
            cb = self.queue.popleft()
            print("callback {0} I am after Eventfired, thread name is {1}\n".format(cb.name, current_thread().getName()), flush=True)
            #cb.call()
 
        #print("FIRE Thread is {0}".format(current_thread().getName()))
        self.isEventFired = True
        print("Eventfired = {0}, thread name is {1}\n".format(self.isEventFired, current_thread().getName()), flush=True)    
    
    
def register1(Event):
    Event.reg_cb(cb1)
    Event.reg_cb(cb2)
    Event.reg_cb(cb3)
    #Event.fire()
    Event.reg_cb(cb4)
    Event.reg_cb(cb5)
    
    
def register2(Event):
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
    e1 = Thread(target=register1, args=(Event,), name = "Thread1", daemon = True)
    e2 = Thread(target=register2, args=(Event,), name = "Thread2", daemon = True)
    e1.start()
    e2.start()
    
    e1.join()
    e2.join()    
    
    print("I am currently in {}".format(current_thread().getName()))
    print("Main thread exiting")
    
    
'''
Notice here that in absence of any kind of locks in this example there are couple of issues.

1. When the Event is fired then then all the tasks waiting in the queue should be executed first before executing any new task but this is not
happening as observed from the output.

2. As event is fired after that point nothing should be stored in queue. all callbacks should get executed immediately
'''
    