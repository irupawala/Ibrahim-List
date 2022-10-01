'''
Spin - Lock

In software engineering, a spinlock is a lock which causes a thread trying to acquire it to simply wait in a loop ("spin") while repeatedly checking if the lock is available. 
Since the thread remains active but is not performing a useful task, the use of such a lock is a kind of busy waiting. 
Once acquired, spinlocks will usually be held until they are explicitly released, 
although in some implementations they may be automatically released if the thread being waited on (that which holds the lock) blocks, or "goes to sleep".

Mutex

In computer science, mutual exclusion refers to the requirement of ensuring that no two concurrent processes are in their critical section at the same time; 
it is a basic requirement in concurrency control, to prevent race conditions. 
Here, a critical section refers to a period when the process accesses a shared resource, such as shared memory
'''



from threading import Thread
import time

def printer_thread_func():
    global prime_holder
    global found_prime
    
    
    while not exit_prog:
        # Mutex using a spinlock and flag, Also known as busy-waiting
        while not found_prime and not exit_prog:
            time.sleep(0.1) # wastes CPU cycles
            
        if not exit_prog:
            print(prime_holder)
            prime_holder = None 
            found_prime = False
            
    return

def is_prime(i):
    if i%2 == 0: return False
    return True
    
def finder_thread_func():
    global prime_holder # flags
    global found_prime # flags
    
    i = 1
    
    while not exit_prog:
        
        while not is_prime(i):
            i += 1
        
        found_prime = True
        prime_holder = i
        
        # Mutex using a spinlock and flag, Also known as busy-waiting
        while not found_prime and not exit_prog:
            time.sleep(0.1)
            
        i += 1
    
    
found_prime = False
prime_holder = None
exit_prog = False

printer_thread = Thread(target=printer_thread_func)
printer_thread.start()

finder_thread = Thread(target=finder_thread_func)
finder_thread.start()

time.sleep(3)
exit_prog = True
printer_thread.join()
finder_thread.join()


