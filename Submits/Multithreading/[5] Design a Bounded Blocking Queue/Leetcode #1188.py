from threading import Condition
from threading import Thread
from collections import deque

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.curr_size = 0
        self.cond = Condition()
        self.q = deque()
        

    def enqueue(self, element: int) -> None:
        
        self.cond.acquire()
        while self.curr_size == self.max_size:
            self.cond.wait()
            
        self.q.append(element)
        self.curr_size += 1
        self.cond.notifyAll()
        self.cond.release()

    def dequeue(self) -> int:
        
        self.cond.acquire()
        while self.curr_size == 0:
            self.cond.wait()
            
        returned_element = self.q.popleft()
        self.curr_size -= 1
        self.cond.notifyAll()
        self.cond.release()
        
        return returned_element
    
    def size(self) -> int:
        return self.curr_size