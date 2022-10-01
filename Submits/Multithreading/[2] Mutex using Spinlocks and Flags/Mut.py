import time

class Mutex():
    def __init__(self):
        self.lock = False
    
    def getlock(self):
        print("lock acquired")
        while not self.lock:
            time.sleep(0.1)
            
        print("lock released")
        
    def unlock(self):
        print("unlocking")
        self.lock = True
        
        

if __name__ == "__main__":
    M = Mutex()
    M.getlock()
    time.sleep(0.5)
    M.unlock()
    
    
            
    