# 1. The Basics

## [1] Program Vs Thread Vs Process

### Program

* A program is a set of instructions and associated data that resides on the disk and is loaded by the operating system to perform a task.
* An executable file or a python script file are examples of programs.
* In order to run a program, the operating system's kernel is first asked to create a new process, which is an environment in which a program is executed.

### Process

* A process is a program in execution.
* A process is an execution environment that consists of instructions, user-data, and system-data segments, as well as lots of other resources such as CPU, memory, address-space, disk and network I/O acquired at runtime.

### Thread

* A thread is the smallest unit of execution in a process. A process can have multiple threads running as part of it.
* Usually, there would be some state associated with the process that is shared among all the threads and in turn each thread would have some state private to itself.
* The globally shared state amongst the threads of a process is visible and accessible to all the threads, and special attention needs to be paid when any thread tries to read or write to this global shared state.
* **Processes don't share any resources amongst themselves whereas threads of a process can share the resources allocated to that particular process, including memory address space.** 



## [2] Concurrency Vs Parallelism

### Serial Execution

* When programs are serially executed, they are scheduled one at a time on the CPU. Once a task gets completed, the next one gets a chance to run.
* The analogy for serial execution is a circus juggler who can only juggle one ball at a time. Definitely not very entertaining!

### Concurrency

* A concurrent program is one that can be decomposed into constituent parts and each part can be executed out of order or in partial order without affecting the final outcome.
* A concurrent system can have two programs *in progress* at the same time where *progress* doesn't imply execution. One program can be suspended while the other executes. Both programs are able to make progress as their execution is interleaved.
* In concurrent systems, the goal is to maximize throughput and minimize latency.
* The classic example of a concurrent system is that of an operating system running on a single core machine. Such an operating system is **concurrent but not parallel.**

### Parallelism

* A parallel system is one which necessarily has the ability to execute multiple programs **at the same time.**
* Usually, this capability is aided by hardware in the form of multicore processors on individual machines or as computing clusters where several machines are hooked up to solve independent pieces of a problem simultaneously.
* Remember an individual problem has to be concurrent in nature, that is, portions of it can be worked on independently without affecting the final outcome before it can be executed in parallel.
* Either a single (large) problem can be executed in parallel or distinct programs can be executed in parallel on a system supporting parallel execution.
* **In parallel systems, the emphasis is on increasing throughput and optimizing usage of hardware resources. The goal is to extract out as much computation speedup as possible**.
* **Concurrency is about *dealing* with lots of things at once. Parallelism is about lots of things at once.** Last but not the least, you'll find literature describing concurrency as a property of a program or a system whereas parallelism as a runtime behaviour of executing multiple tasks.

## [3] Cooperative vs Preemptive Multitasking

### Preemptive Multitasking

* In preemptive multitasking, the operating system preempts a program to allow another waiting task to run on the CPU. 
* Programs or threads can't decide how long or when they can use the CPU. The operating system’s scheduler decides which thread or program gets to use the CPU next and for how much time.
*  A thread or program, once taken off of the CPU by the scheduler, can't determine when it will get on the CPU next. As a consequence, if a malicious program initiates an infinite loop, it only hurts itself without affecting other programs or threads.

### Cooperative Multitasking

* Cooperative Multitasking involves well-behaved programs voluntarily giving up control back to the scheduler so that another program can run. A program or thread may give up control after a period of time has expired or if it becomes idle or logically blocked.
* The operating system’s scheduler has no say in how long a program or thread runs for.
* A malicious program can bring the entire system to a halt by busy-waiting or running an infinite loop and not giving up control. The process scheduler for an operating system implementing cooperative multitasking is called a cooperative scheduler.

## [4] Throughput vs Latency

### Throughput

* Throughput is defined as the *rate of doing work* or how much work gets done per unit of time.
* If you are an Instagram user, you could define throughput as the number of images downloaded by your phone or browser per unit of time.

### Latency

* Latency is defined as the *time required to complete a task or produce a result*. Latency is also referred to as *response time*. 
* The time it takes for a web browser to download Instagram images from the internet is the latency for downloading the images.

## [5] Synchronous vs Asynchronous

### Synchronous 

* Synchronous execution refers to line-by-line execution of code. 
* If a function is invoked, the program execution waits until the function call is completed. 
* **Synchronous execution blocks at each method call before proceeding to the next line of code.**
* A program executes in the same sequence as the code in the source code file.

### Asynchronous

* **Asynchronous (or async) execution refers to execution that doesn't block when invoking subroutines.**
* Wikipedia definition: *Asynchronous programming is a means of parallel programming in which a unit of work runs separately from the main application thread and notifies the calling thread of its completion, failure or progress*.
* An asynchronous program doesn’t wait for a task to complete before moving on to the next task.
* Async execution can invoke a method and move on to the next line of code without waiting for the invoked function to complete or receive its result.
  * Usually, such methods return an entity sometimes called **future** or **promise** that is the representation of an in-progress computation. The program can query for the status of the computation via the returned future or promise and retrieve the result once completed.
  *  Another pattern is to pass a callback function to the asynchronous function call, which is invoked with the results when the asynchronous function is done processing.
* In non-threaded environments, asynchronous programming provides an alternative to threads in order to achieve concurrency and fall under the cooperative multitasking model.

## [6] I/O Bound vs CPU Bound

We write programs to solve problems. Programs utilize various resources of the computer systems on which they run. For instance a program running on your machine will broadly require:

- CPU Time
- Memory
- Networking Resources
- Disk Storage

### CPU Bound

* Programs which are compute-intensive, i.e. where the program execution requires very high utilization of the CPU (close to 100%), are called CPU bound programs. Such programs primarily depend upon improving CPU speed to decrease program completion time. This could include programs such as data crunching, image processing, matrix multiplication, etc.

### I/O Bound

* I/O bound programs are the opposite of CPU bound programs. Such programs spend most of their time waiting for input or output operations to complete while the CPU sits idle. I/O operations can consist of operations that write or read from main memory or network interfaces.
* Even though the physical distances are tiny, the time taken to move the data across is long enough for several thousand CPU cycles to go to waste. This is why I/O bound programs would show relatively lower CPU utilization than CPU bound programs.

## [7] Thread Safety

* The primary motivation behind using multiple threads is improving program performance that may be measured with metrics such as throughput, responsiveness, latency, etc. 
* Whenever threads are introduced in a program, the shared state amongst the threads becomes vulnerable to corruption. If a class or a program has immutable state then the class is necessarily thread-safe. 
* Programming languages provide constructs such as mutexes and locks to help developers guard sections of code that must be executed sequentially by multiple threads.

## [8] Critical Section & Race Conditions

### Critical Section

* Critical section is any piece of code that has the possibility of being executed concurrently by more than one thread of the application and exposes any shared data or resources used by the application for access.

### Race Condition

* Race conditions happen when threads run through critical sections without thread synchronization.
* The threads ***"race"*** through the critical section to write or read shared resources and depending on the order in which threads finish the "race", the program output changes.

## [9] Deadlock and Liveness

### Deadlock

* Deadlocks occur when two or more threads aren't able to make any progress because the resource required by the first thread is held by the second and the resource required by the second thread is held by the first.

### Liveness

* Ability of a program or an application to execute in a timely manner is called liveness. If a program experiences a deadlock then it's not exhibiting liveness.

### Live-Lock

* A live-lock occurs when two threads continuously react in response to the actions by the other thread without making any real progress.

### Starvation

* Other than a deadlock, an application thread can also experience starvation when it never gets CPU time or access to shared resources. Other **greedy** threads continuously hog shared system resources not letting the starving thread make any progress.

### Re-Entrant Lock [Come back Again after RLock]

## [10] Mutex Vs Semaphore

### Mutex

* Mutex as the name hints implies ***mutual exclusion***. A mutex is used to guard shared data such as a linked-list, an array, or any primitive type. A mutex allows only a single thread to access a resource or critical section.
* Mutex implies mutual exclusion and is used to serialize access to critical sections.

### Semaphore

* Semaphore, on the other hand, is used for limiting access to a collection of resources. Think of semaphore as having a limited number of permits to give out. If a semaphore has given out all the permits it has, then any new thread that comes along requesting a permit will be blocked till an earlier thread with a permit returns it to the semaphore.
* A semaphore with a single permit is called a **binary semaphore** and is often thought of as equivalent to a mutex.
* Semaphores can also be used for signaling among threads. This is an important distinction as it allows threads to cooperatively work towards completing a task.
* A semaphore can potentially act as a mutex if the permits it can give out is set to 1. However, the most important difference between the two is that in case of a mutex ***the same thread must call acquire and subsequent release on the mutex*** whereas in case of a binary semaphore, ***different threads can call acquire and release on the semaphore***.
* This leads us to the concept of **ownership**. **A mutex is owned by the thread acquiring it till the point the owning-thread releases it, whereas for a semaphore there's no notion of ownership.**

## [11] Mutex Vs Monitor

### Mutex Vs Monitor

* Concisely, a monitor is a mutex and then some. The additional composition of monitors consists of condition variables.
* Monitors are generally language-level constructs whereas mutex and semaphore are lower-level or OS-provided constructs.

* To understand monitors, let's first see the problem they solve. Usually, in multi-threaded applications, a thread needs to wait for some program predicate to be true before it can proceed forward. 
* What could be a crude way of accomplishing this?

```python
void busy_wait_function() {
    // acquire mutex
    while (predicate is false) {
      // release mutex
      // acquire mutex
    }
    // do something useful
    // release mutex
}
```

* Within the while loop we'll first release the mutex giving other threads a chance to acquire it, and set the loop predicate to true. Before we check the loop predicate again, we make sure we have acquired the mutex. This works but is an example of ***"spin waiting"*** which wastes a lot of CPU cycles. 

### Condition Variables

* Mutex provides mutual exclusion. However, at times mutual exclusion is not enough. We want to test for a predicate with a mutually exclusive lock so that no other thread can change the predicate when we test for it, but if we find the predicate to be false, we'd want to wait on a condition variable till the predicate's value is changed. This is the solution to spin waiting.
* The `wait()` method, when called on the condition variable, will cause the associated mutex to be atomically released and the calling thread would be placed in a **wait queue**.
* Since the mutex is now released, it gives other threads a chance to change the predicate that will eventually let the thread that was just placed in the wait queue to make progress.
* As an example, say we have a consumer thread that checks for the size of the buffer, finds it empty and invokes `wait()` on a condition variable. The predicate in this example would be **the size of the buffer**.
* Now imagine a producer places an item in the buffer. The predicate, the size of the buffer, just changed and the producer wants to let the consumer threads know that there is an item to be consumed.
* This producer thread would then invoke `signal()` on the condition variable. The `signal()` method, when called on a condition variable, causes one of the threads that has been placed in the **wait queue** to get ready for execution.
* Note that we didn't say the woken up thread starts executing. It just gets ready - and that could mean being placed in the ready queue. It is only **after the producer thread which calls the `signal()` method has released the associated mutex that the thread in the ready queue starts executing.** 
* The thread in the ready queue must wait to acquire the mutex associated with the condition variable before it can start executing.

```python
void efficient_waiting_function() {
    mutex.acquire()
    while (predicate == false) {
      cond_var.wait()
    }
    // Do something useful
    mutex.release()     
}

void change_predicate() {
    mutex.acquire()
    set predicate = true
    cond_var.signal()
    mutex.release()
}
```

* Note that the order of signaling the condition variable and releasing the mutex can be interchanged, but generally, the preference is to signal first and then release the mutex.
* If the snippet is re-written in the above manner using an `if` clause instead of a `while` then, we need a guarantee that once the variable `cond_var` is signaled, the predicate can't be changed by any other thread and that the signaled thread becomes the owner of the monitor. This may not be true. 
* **The idiomatic and correct usage of a monitor dictates that** ***the predicate always be tested for in a while loop*****.**
* Practically, in Python, a `Condition` object is a monitor which implicitly has a lock or can be passed one explicitly. You can think of a monitor as a ***mutex with a wait set***. Monitors allow threads to exercise **mutual exclusion** as well as **cooperation** by allowing them to wait and signal on conditions.

## [12] Mesa Vs Hoare Monitors

```python
while( condition == false ) {
    condVar.wait();
}
```

Once the asleep thread is signaled and woken up, you may ask why does it needs to check for the condition being false again if the signaling thread must have just set the condition to true?

### Mesa monitors (While Condition)

* it is possible that in the time gap between when thread B calls `notify()` and releases its mutex **and** the instant at which the asleep thread A wakes up and reacquires the mutex, **the predicate is changed back to false by another thread different than the signaler and the awoken threads!** The woken up thread competes with other threads to acquire the mutex once the signaling thread B **empties** the monitor. On signaling, thread B doesn't give up the monitor just yet; rather it continues to own the monitor until it exits the monitor section.

### Hoare Monitors (If Condition)

* In contrast in **Hoare monitors** - the signaling thread B **yields** the monitor to the woken up thread A and thread A **enters** the monitor while thread B sits out. This guarantees that the predicate will not have changed and instead of checking for the predicate in a while loop, an if-clause would suffice. The woken-up/released thread A immediately starts execution when the signaling thread B signals that the predicate has changed. No other thread gets a chance to change the predicate since no other thread gets to enter the monitor.

## [13] Semaphore Vs Monitor

* Monitors take care of atomically acquiring the necessary locks whereas, with semaphores, the onus of appropriately acquiring and releasing locks is on the developer, which can be error-prone.
* Semaphores are lightweight when compared to monitors, which are bloated.
* A semaphore can allow several threads access to a given resource or critical section. However, only a single thread can **own** the monitor and access associated resource at any point.
* Semaphores can be used to address the issue of **missed signals**. However, with monitors, the additional state, called the predicate, needs to be maintained apart from the condition variable and the mutex, which make up the monitor, to solve the issue of missed signals.

## [14] Global Interpreter Lock

* The Python interpreter as explained is responsible for executing a program, but it can only execute a single thread at a time. 
* The interpreter executes a single thread in order to ensure that the reference count for objects is safe from race conditions.
* A reference count is associated with each object in a program.
* Execution of Python bytecode requires acquiring the GIL. This approach prevents deadlocks as there's a single global lock to manage and introduces little overhead. However, the cost is paid by making CPU-bound tasks essentially single-threaded.

## [15] Amdahl's Law

* Amdahl's law describes the theoretical speedup a program can achieve at best by using additional computing resources.
* S(n) = 1/((1-P) + P/n)
* **S(n)** is the speed-up achieved by using **n** cores or threads.
* **P** is the fraction of the program that is parallelizable.
* **(1 - P)** is the fraction of the program that must be executed serially.

## [16] Moore's Law

# 2. Threading Modules

## [1] Creating Threads

* Thread Constructor 

```python
Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

* Threads can be created using two methods.
* Note that if we use thread_task() instead of thread_task then main thread will be called.

### Using Functions

```python
from threading import Thread
from threading import current_thread


def thread_task(a, b, c, key1, key2):
    print("{0} received the arguments: {1} {2} {3} {4} {5}".format(current_thread().getName(), a, b, c, key1, key2))


myThread = Thread(group=None,  # reserved
                  target=thread_task,  # callable object
                  name="demoThread",  # name of thread
                  args=(1, 2, 3),  # arguments passed to the target
                  kwargs={'key1': 777,
                          'key2': 111},  # dictionary of keyword arguments
                  daemon=None  # set true to make the thread a daemon
                  )

myThread.start()  # start the thread

myThread.join()  # wait for the thread to complete

```

### Using SubClasses

```python
from threading import Thread
from threading import current_thread


class MyTask(Thread):

    def __init__(self):
        # The two args will not get passed to the overridden
        # run method.
        Thread.__init__(self, name="subclassThread", args=(2, 3))

    def run(self):
        print("{0} is executing".format(current_thread().getName()))


myTask = MyTask()

myTask.start()  # start the thread

myTask.join()  # wait for the thread to complete

print("{0} exiting".format(current_thread().getName()))
```

## [2] Daemon Thread

* A daemon is a computer program that runs as a background process rather than being under the direct control of an interactive user. A daemon thread in Python runs in the background. 
* The difference between a regular thread and a daemon thread is that **a Python program will not exit until all regular/user threads terminate.** However, a program may exit if the daemon thread is still not finished.
* Daemon threads are shut-down abruptly. Resources such as open files and database connections may not shut-down properly and daemon threads are not a good choice for such tasks. One final caveat to remember is that if you don't specify the `daemon` parameter in the constructor then the daemonic property is inherited from the current thread.

## [3] Lock

### Acquire

* A `Lock` object is equivalent of a mutex that you read about in operating systems theory.
* It offers two methods: `acquire()` and `release()`.
* A Lock object can only be in two states: **locked** or **unlocked**. A Lock object can only be unlocked by a thread that locked it in the first place.

### Release

* The `release()` method will change the state of the Lock object to unlocked and give a chance to other waiting threads to acquire the lock. If multiple threads are already blocked on the acquire call then only one arbitrarily chosen (varies across implementations) thread is allowed to acquire the Lock object and proceed.

```python
import time
from threading import Lock
from threading import Thread
from threading import current_thread

sharedState = [1, 2, 3]
my_lock = Lock()


def thread1_operations():
    my_lock.acquire()
    print("{0} has acquired the lock".format(current_thread().getName()))

    time.sleep(10)
    sharedState[0] = 777

    print("{0} about to release the lock".format(current_thread().getName()))
    my_lock.release()
    print("{0} released the lock".format(current_thread().getName()))


def thread2_operations():
    print("{0} is attempting to acquire the lock".format(current_thread().getName()))
    my_lock.acquire()
    print("{0} has acquired the lock".format(current_thread().getName()))

    print(sharedState[0])
    print("{0} about to release the lock".format(current_thread().getName()))
    my_lock.release()
    print("{0} released the lock".format(current_thread().getName()))

if __name__ == "__main__":
    # create and run the two threads
    thread1 = Thread(target=thread1_operations, name="thread1")
    thread1.start()

    thread2 = Thread(target=thread2_operations, name="thread2")
    thread2.start()

    # wait for the two threads to complete
    thread1.join()
    thread2.join()
```

### Deadlock Example

```python
from threading import *
import time


def thread_one(lock1, lock2):
    lock1.acquire()
    time.sleep(1)
    lock2.release()


def thread_two(lock1, lock2):
    lock2.acquire()
    time.sleep(1)
    lock1.release()


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=thread_one, args=(lock1, lock2))
    t2 = Thread(target=thread_one, args=(lock1, lock2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
```

## [4] RLock

* A reentrant lock is defined as a lock which can be reacquired by the same thread. A `RLock` object carries the notion of ownership. If a thread acquires a `RLock` object, it can chose to reacquire it as many times as possible. 
* In contrast to `Lock`, the reentrant lock is acquired twice in the above snippet without blocking. Note that it is imperative to release the lock as many times as it is locked, otherwise the lock remains in locked state and any other threads attempting to acquire the lock get blocked.

```python
from threading import RLock
from threading import Thread


def child_task():
    rlock.acquire()
    print("child task executing")
    rlock.release()


rlock = RLock()

rlock.acquire()
rlock.acquire()

rlock.release()

# UNCOMMENT THE FOLLOWING LINE TO MAKE THE
# PROGRAM EXIT NORMALLY.
# rlock.release()

thread = Thread(target=child_task)
thread.start()
thread.join()

```

### Ownership

* As explained, each reentrant lock is owned by some thread when in the locked state. Only the owner thread is allowed to exercise a `release()` on the lock. If a thread different than the owner invokes `release()` a RuntimeError is thrown as shown in the example below:
* Releasing unowned reentrant lock

```python
from threading import RLock
from threading import Thread


def perform_unlock():
    rlock.release()
    print("child task executing")
    rlock.release()


rlock = RLock()

# reentrant lock acquired by main thread
rlock.acquire()

# let's attempt to unlock using a child thread
thread = Thread(target=perform_unlock)
thread.start()
thread.join()

```

* Recognize this isn't a problem with non-reentrant locks.

```python
from threading import Lock
from threading import Thread


def perform_unlock():
    #lock.release()
    print("child task executing")
    lock.release()


lock = Lock()

# reentrant lock acquired by main thread
lock.acquire()

# let's attempt to unlock using a child thread
thread = Thread(target=perform_unlock)
thread.start()
thread.join()
```

## [5] Condition Variables

- Synchronization mechanisms need more than just mutual exclusion; a general need is to be able to wait for another thread to do something. Condition variables provide mutual exclusion and the ability for threads to wait for a predicate to become true.

## [6] Semaphores

* A semaphore is nothing more than an atomic counter that gets decremented by one whenever `acquire()` is invoked and incremented by one whenever `release()` is called.
* The semaphore can be initialized with an initial count value. If none is specified, the semaphore is initialized with a value of one.
* **The primary use of semaphores is signaling among threads which are working to achieve a common goal.** 

### acquire()

* If a thread invokes `acquire()` on a semaphore, the semaphore counter is decremented by one. If the count is greater than 0, then the thread immediately returns from the `acquire()` call. 
* If the semaphore counter is zero when a thread invokes `acquire()`, the thread gets blocked till another thread releases the semaphore.

### release()

* When a thread invokes the `release()` method, the internal semaphore counter is incremented by one. 

* If the counter value is zero and another thread is already blocked on an `acquire()` then a release would unblock the waiting thread. 

* If multiple threads are blocked on the semaphore, then one thread is arbitrarily chosen.


### Missed Signal

* Missed Signal happens when thread is notified before the first thread has a chance to wait on the condition variable.
* One way to remedy the above situation is to use semaphores. The internal counter of the semaphore *remembers* how many times the signal was received.

```python
from threading import Thread
from threading import Semaphore
import time


def task1():
    sem.acquire()


def task2():
    sem.release()

# initialize with zero
sem = Semaphore(-2)

# start thread 2 first which invokes release()
thread2 = Thread(target=task2)
thread2.start()

# delay starting thread 1 by three seconds
time.sleep(3)

# start thread 1
thread1 = Thread(target=task1)
thread1.start()

thread1.join()
thread2.join()
```

**Printer Program**

```python
from threading import Thread
from threading import Semaphore
import time


def printer_thread():
    global primeHolder

    while not exitProg:
        # wait for a prime number to become available
        sem_find.acquire()

        # print the prime number
        print(primeHolder)
        primeHolder = None

        # let the finder thread find the next prime
        sem_print.release()


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_thread():
    global primeHolder

    i = 1

    while not exitProg:

        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)

        primeHolder = i

        # let the printer thread know we have
        # a prime available for printing
        sem_find.release()

        # wait for printer thread to complete
        # printing the prime number
        sem_print.acquire()

        i += 1


sem_find = Semaphore(0)
sem_print = Semaphore(0)
primeHolder = None
exitProg = False

printerThread = Thread(target=printer_thread)
printerThread.start()

finderThread = Thread(target=finder_thread)
finderThread.start()

# Let the threads run for 3 seconds
time.sleep(3)

exitProg = True

printerThread.join()
finderThread.join()
```

### Event

* An event object is one of the simplest primitives available for synchronization. 

* Internally, it has a boolean flag that can be set or unset using the methods `set()` and `clear()`. Additionally, a thread can check if the flag is set to true by invoking the `is_set()` method.
* The event object exposes a `wait()` method that threads can invoke to wait for the internal boolean flag to become true. If the flag is already true, the thread returns immediately. If there are multiple threads waiting on the event object and an active thread sets the flag then all the waiting threads are unblocked.

#### Differences with Semaphores

Event objects may seem similar to semaphore or a bounded semaphore but there are slight differences:

* An unbounded semaphore can have its internal counter incremented as many times as `acquire()` is invoked on it, whereas an event object maintains an internal boolean flag that can only flip between two state: set or unset.
* Can a bounded semaphore intialized to 1 be equivalent to an event object? The answer is no because the bounded semaphore will raise a `ValueError` if the bounded semaphore is acquired more number of times than the initial passed in capacity. Also acquiring a semaphore decrements the internal counter of the semaphore whereas waiting on an event object doesn't change the state of the internal boolean flag.
* A thread never gets blocked on `wait()` of an event object if the internal flag is set to true no matter how many times the thread invokes the `wait()` method.

```python
from threading import Thread
from threading import Event
import time


def printer_thread():
    global primeHolder

    while not exitProg:
        # wait for a prime number to become available
        prime_available.wait()

        # print the prime number
        print(primeHolder)
        primeHolder = None

        # reset the event to false
        prime_available.clear()

        # let the finder thread know that printing is done
        prime_printed.set()


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_thread():
    global primeHolder

    i = 1

    while not exitProg:

        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)

        primeHolder = i

        # let the printer thread know we have
        # a prime available for printing
        prime_available.set()

        # wait for printer thread to print the prime
        prime_printed.wait()

        # reset the flag
        prime_printed.clear()

        i += 1



prime_available = Event()
prime_printed = Event()
primeHolder = None
exitProg = False

printerThread = Thread(target=printer_thread)
printerThread.start()

finderThread = Thread(target=finder_thread)
finderThread.start()

# Let the threads run for 3 seconds
time.sleep(3)

exitProg = True
prime_available.set()
prime_printed.set()

printerThread.join()
finderThread.join()
```

### Timer

* The Timer object allows execution of a callable object after a certain amount of time has elapsed. 
* Consider the snippet below where a `Timer` object executes the method `say_hi()` in a different thread than the main thread. 
* The timer constructor takes in a floating point number representing the seconds that need to elapse before the task is executed.
* Time is a subclass of the `Thread` class and similarly accepts arguments as a list or a keyword dictionary.
* A timer object can also be cancelled using the `cancel()` method before the task has been executed.

```python
from threading import Timer
from threading import current_thread
import time


def say_hi(name):
    print("{0} says Hi {1}!".format(current_thread().getName(), name))


timer = Timer(1, say_hi, args=["reader"])
timer.start()

time.sleep(2)
timer.cancel()

print("{0} exiting".format(current_thread().getName()))

```

## [7] Barrier

* A barrier is a synchronization construct to wait for a certain number of threads to reach a common synchronization point in code.
* The involved threads each invoke the barrier object's `wait()` method and get blocked till all of threads have called `wait()`.
* When the last thread invokes `wait()` all of the waiting threads are released simultaneously. 

```python
from threading import Barrier
from threading import Thread
import random
import time


def thread_task():
    time.sleep(random.randint(0, 7))
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()


num_threads = 5
barrier = Barrier(num_threads)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()

```

* The barrier constructor also accepts a callable argument as an action to be performed when threads are released. Only one of the threads released will invoke the action. An example is given below:

```python
from threading import Barrier
from threading import Thread
from threading import current_thread
import random
import time


def thread_task():
    time.sleep(random.randint(0, 5))
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()


def when_all_threads_released():
    print("All threads released, reported by {0}".format(current_thread().getName()))


num_threads = 5
barrier = Barrier(num_threads, action=when_all_threads_released)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()

```

* If you execute the above snippet multiple times, you'll see that the action passed into barrier constructor is executed by a randomly chosen thread each time.

**Broken Barriers**

The barrier object exposes an `abort()` method which can be invoked to avoid deadlocks if needed. Threads already waiting on a barrier experience a `BrokenBarrierError` if `abort()` is invoked. The example below demonstrates this scenario.

```python 
from threading import Barrier
from threading import Thread
import time


def thread_task():
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()
    print("Barrier broken")


num_threads = 5
barrier = Barrier(num_threads + 1)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()

time.sleep(3)

print("Main thread about to invoke abort on barrier")
barrier.abort()

```

## [8] With

* Programs often use resources other than CPU time, including access to local disks, network sockets, and databases etc. The usage pattern is usually a `try-except-finally` block. Any cleanup actions are performed in the `finally` block. An alternative to the usual boilterplate code is to use the `with` statement. 
* The `with` statement wraps the execution of a block of statements in a context defined by a **context manager** object.

### Context Management Protocol

A context manager object abides by the context management protocol, which states that an object defines the following two methods. Python calls these two methods at appropriate times in the resource management cycle:

* `__enter__`
* `__exit__`
* If an error is raised in `__init__()` or `__enter__()` then the code block is never executed and `__exit__()` is not called.
* Once the code block is entered, `__exit__` is always called, even if an exception is raised in the code block.

```python
class ExampleClass():
    def __init__(self, val):
        print("init")
        self.val = val

# __enter__() should return an object that is assigned to the variable after as in the above template. By default the returned object is None, and is optional. A common pattern is to return self and keep the functionality required within the same class.        
    def __enter__(self): 
        print("enter invoked")
        return self
    
    def display(self):
        print(self.val)
        lala

# __exit__() is called on the original Context Manager object, not the object returned by __enter__(). If, however, we return self in the __enter__() method, then it is obviously the same object.     
    def __exit__(self, exc_type, exc_val, exc_tb): #exception type, value and trace back
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("exit invoked")

if __name__ == "__main__":
    with ExampleClass("hello world") as example:
        example.display()

    
```

* The `with` statement helps simplify some common resource management patterns by abstracting their functionality and allowing them to be factored out and reused. 

### Using With Statement in Multithreading 

* Some classes in the `threading` module such as `Lock`, support the context management protocol and can be used with the `with` statement. 
* In the example below, we reproduce an example from an earlier section and use the `with` statement with the `Lock` object `my_lock`.
* Note, we don't need to explicitly `acquire()` and `release()` the lock object. The context manager automatically takes care of managing the lock for us.

```python
import time
from threading import Lock
from threading import Thread
from threading import current_thread

sharedState = [1, 2, 3]
my_lock = Lock()


def thread1_operations():

    with my_lock:
        print("{0} has acquired the lock".format(current_thread().getName()))

        time.sleep(3)  #
        sharedState[0] = 777

        print("{0} about to release the lock".format(current_thread().getName()))

    print("{0} released the lock".format(current_thread().getName()))


def thread2_operations():
    print("{0} is attempting to acquire the lock".format(current_thread().getName()))

    with my_lock:
        print("{0} has acquired the lock".format(current_thread().getName()))

        print(sharedState[0])
        print("{0} about to release the lock".format(current_thread().getName()))

    print("{0} released the lock".format(current_thread().getName()))


if __name__ == "__main__":
    # create and run the two threads
    thread1 = Thread(target=thread1_operations, name="thread1")
    thread1.start()

    thread2 = Thread(target=thread2_operations, name="thread2")
    thread2.start()

    # wait for the two threads to complete
    thread1.join()
    thread2.join()
```



# 2. Multiprocessing

## [1] Introduction

* Python offers the ability to execute tasks as processes using the `multiprocessing` module. Most of the APIs in the module mirror the APIs found in the `threading` module.
* The limitations of the global interpreter lock are to an extent addressed by the `multiprocessing` module.
* The `multiprocessing` module offers hope by allowing a program to spin-off tasks as separate processes that can then run on individual processors.
* This allows Python to be both concurrent and parallel, whereas with the threading module, Python is only concurrent and not parallel. Languages without a GIL in their design, such as Java, can exhibit both concurrency and parallelism using only threads on a multicore system.
* Creating, managing and tearing down processes is more expensive than doing the same for threads. Furthermore, inter-process communication is relatively slower than inter-thread communication. Both these drawbacks may not make Python a practical technology choice for super-critical or time-sensitive use-cases.

## [2] Process

* A process is a program in execution.
* operating systems provide different ways of creating new processes.
* Furthermore, each operating system has its own nuances when spawning new processes, which gets reflected in Python's APIs.
* The multiprocessing module offers the method `set_start_method()` to let the developer choose the way new processes are created. There are three of them:
  * Fork
  * Spawn
  * Fork-server
* Example
* In the above examples, we don't specify `set_start_method()` and let Python choose the default.

```python 
from multiprocessing import Process
from multiprocessing import current_process
import os


def process_task(x, y, z, key1, key2):
    print("\n{0} has pid: {1} with parent pid: {2}".format(current_process().name, os.getpid(), os.getppid()))
    print("Received arguemnts {0} {1} {2} {3} {4}\n".format(x, y, z, key1, key2))


process = Process(target=process_task,
                  name="process-1",
                  args=(1, 2, 3),
                  kwargs={
                      'key1': 'arg1',
                      'key2': 'arg2'
                  })
process.start()

process.join()
```

## [3] Fork

* Fork is the default method Python uses to create processes on Unix based systems.

### Fork System Call

* There are two families of system calls, **fork** and **exec** that can be invoked by a process to create sub processes on **Unix** based systems.
* A process can invoke this system call and get an ***almost*** clone of itself.
* We qualify the statement with *almost* because not everything is copied when a fork happens. The exact list of what isn't copied can be found by checking out the **manpage** of fork on your platform (type "man fork" in terminal).
* The child process gets an identical memory image so any **open file descriptors are copied**. However, **multiple threads of a process don't get copied.**
* **Any threads running in the parent process do not exist in the child process.** Additionally, fork isn't available on a Windows platform. Under the hood, Python uses `os.fork()` to create the child process.
* Often times we don't want to fork processes because the newly created process (called the child process) comes with **identical copies of data-structures and file descriptors of the parent process**, which can be problematic.

```python
from multiprocessing import Process
import multiprocessing

class Test:
    value = 777


def process_task():
    print(Test.value)


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    # change the value of Test.value before creating
    # a new process
    Test.value = 999
    process = Process(target=process_task, name="process-1")
    process.start()
    process.join()
```

* Every data structure, open file, and database connection that exists in the parent process is copied over, open and ready to use, in the child process.

```python
from multiprocessing import Process
import multiprocessing
import os

file_desc = None


def process_task():
    # write to the file in a child process
    file_desc.write("\nline written by child process with id {0} having parent id {1}".format(os.getpid(), os.getppid()))
    file_desc.flush()


if __name__ == '__main__':
    # create a file descriptor in the parent process
    file_desc = open("sample.txt", "w")
    file_desc.write("\nline written by parent process with id {0}".format(os.getpid()))
    file_desc.flush()

    multiprocessing.set_start_method('fork')

    process = Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    # read and print the contents of the file
    file_desc = open("sample.txt", "r")
    print(file_desc.read())

    os.remove("sample.txt")

```

* When we fork, the entire Python process is duplicated in memory including the Python interpreter, code, libraries, current stack, etc.
* This creates a new copy of the python interpreter. The implication is that forking creates two python interpreters each with its own GIL. 
* A single GIL is no more a blocker and we can have true multi-processing on a multi-core system. In contrast, threads in one process share the same GIL, meaning only one thread runs at a given moment, giving only the illusion of parallelism.

### Problems with Fork

* To illustrate what problems fork can create, consider the below snippet. The main process created a `Lock` object and acquires it just before forking a child process. The child process receives a copy of all the global data-structures of the parent process.
* It attempts to acquire the lock but when the lock object was copied it was already in the locked state so the child ends up waiting on a lock object that was inherited in the locked state and will never be unlocked because there's no other thread in the process that will unlock it. The child process will hang. If you run the executable code, the execution will time out.
* **The moment when the fork happens, synchronization primitives can be copied in a state that causes the child process to hang.**

```python
from threading import Lock
from multiprocessing import Process
import time
import multiprocessing

lock = Lock()


def process_task():
    lock.acquire()
    print("I am child process")
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    process = Process(target=process_task)

    # acquire the lock just before starting a new process
    lock.acquire()

    process.start()

    # release the lock after starting the child process
    lock.release()

    # wait for child process to be done
    print("Parent process waiting for child process to finish")
    process.join()
    print("done")
```

* Some libraries assume proper initialization for each process but this isn't true when a process is a result of a fork. The assumptions of the underlying libraries may not hold anymore causing the program to fail in myriad ways.
* Portability can be an issue because of differences amongst platforms. **For instance, how open file descriptors get inherited by a child process or what system calls can be executed after a fork vary across platforms.**
* The fork method can't be used on a Windows platform.

## [4] Spawn

#### exec system call

* Using **exec**, the running process loads a program (instructions and data) and replaces its own program with the loaded one and starts execution.
* Both fork and exec can be called independently and need not be called in succession. For instance, a process that is ending can simply call exec and start another program rather than forking itself. Similarly, a process listening on a socket may want to fork itself to let the child process deal with a received request while it goes back to listening.
* But the usual way to create a new process in the Unix world is to first fork in the parent process and then exec in the child process.
* **Remember, forking produces two processes, whereas exec loads an executable in the existing process's address space. The current executable image is replaced with another one loaded from an executable file.**





* Spawn is essentially a combination of fork followed by an exec (one of its variants) system call.
* **The module state isn’t inherited by a child process, rather it starts from scratch.**
* A new python interpreter process is created and the child doesn't inherit any resources from the parent process other **than those required to execute the specified callable target.**
* When a child process is spawned anything imported at the module level in the __main__ module of the parent process gets reimported in the child. Consider the example below. 

* Running the below code will result in an error because the value of the variable `file_desc` isn't copied over to the child process.

```python 
from multiprocessing import Process
import multiprocessing
import os

file_desc = None


def process_task():
    # write to the file in a child process
    file_desc.write("\nline written by child process with id {0}".format(os.getpid()))
    file_desc.flush()


if __name__ == '__main__':
    # create a file descriptor in the parent process
    file_desc = open("sample.txt", "w")
    file_desc.write("\nline written by parent process with id {0}".format(os.getpid()))
    file_desc.flush()

    # changed the start method to spawn
    multiprocessing.set_start_method('spawn')

    process = Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    # read and print the contents of the file
    file_desc = open("sample.txt", "r")
    print(file_desc.read())

    os.remove("sample.txt")

```

* Examine the other program from the previous section, where the change in the `Test` class's variable isn't reflected in the child process if the start method is specified to be spawn.

```python 
from multiprocessing import Process
import multiprocessing

class Test:
    value = 777


def process_task():
    print(Test.value)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')

    # change the value of Test.value before creating
    # a new process
    Test.value = 999
    process = Process(target=process_task, name="process-1")
    process.start()
    process.join()

```

* Note that if we pass any arguments to the process's callable target, the child process does receive them. This is in line with the documentation that says the child process inherits just enough resources from the parent process to execute the run method of the process object.

```python
from multiprocessing import Process
import multiprocessing

global_arg = "this is a global arg"

def process_task(garg, larg):
    print(garg + " - " + larg)


if __name__ == '__main__':

    multiprocessing.set_start_method('spawn')
    local_arg = "this is a global arg"

    process = Process(target=process_task, name="process-1", args=(global_arg, local_arg))
    process.start()
    process.join()

```

## [5] Forkserver

* The official documentation states that with forkserver as the start method, a brand new single-threaded process, called server is started.
* Whenever, a new process needs to be created, the parent process connects to the server and requests that it forks a new process. Since the server process is single threaded, it can safely invoke `os.fork()` to create a new process.

## [6] Queues and Pipes

* There are two ways that processes can communicate between themselves:
  * Queues
  * Pipes

### Queues

* The multiprocessing module offers three types of queues which are all FIFO structures based on the `queue` module's Queue (queue.Queue) implementation in the standard library. These are:
  * Simple Queue
  * Queue
  * Joinable Queue 
* The queues in the multiprocessing module can be shared among multiple processes.
* Remember the following:
  * We can enqueue any element in the queue that is pickable.
  * Queues are thread and process safe.
  * If multiple processes enqueue objects at the same time in a queue, the receiver may receive them out of order. However, all the object enqueued by a single process are always received in order.
* Consider the program below. The main process acts as a producer and fills up a queue with ten messages. The child processes each access the queue and consumes messages from it.

```python
from multiprocessing import Process, Queue, current_process
import multiprocessing, sys
import random


def child_process(q):
    count = 0
    while not q.empty():
        print(q.get())
        count += 1

    print("child process {0} processed {1} items from the queue".format(current_process().name, count), flush=True)

if __name__ == '__main__':
    multiprocessing.set_start_method("forkserver")
    q = Queue()
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

### Pipes

* Pipes can be best thought of as a two way connection between two processes. Whatever is written to one end of the pipe can be retrieved from the other end of the pipe.
* If two threads or processes attempt to write to the same end of the pipe at the same time, the data can potentially become corrupt.
* The Pipe constructor takes in a boolean value. If passed in False, the pipe acts as a one-way communication where one end can only send messages and the other can only receive messages. For example:

`recv_conn, send_conn = Pipe(duplex=False)`

* The first argument `recv_conn` returned by the constructor can receive messages and the second argument `send_conn` can send messages. By default or if the constructor is passed-in True, the connection created is bidirectional.
* Consider the program below, the function `Pipe()` returns two objects each representing one end of the pipe. The child process writes ten strings to the pipe which the parent prints on the console after retrieving them from the queue.

```python
from multiprocessing import Process, Pipe
import time

def child_process(conn):
    for i in range(0, 10):
        conn.send("hello " + str(i + 1))
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    time.sleep(3)

    for _ in range(0, 10):
        msg = parent_conn.recv()
        print(msg)

    parent_conn.close()
    p.join()

```

### Non-Blocking Method Calls

```python
from multiprocessing import Process, Queue, current_process
import multiprocessing, sys
import random


def child_process(q):
    count = 0
    while not q.empty():
        try:
            print(q.get(block=False, timeout=5))
            count += 1
        except:
            pass

    print("child process {0} processed {1} items from the queue".format(current_process().name, count), flush=True)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    q = Queue()

    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

## [7] Sharing State

* The queue and the semaphore object are truly shared between the two processes and both the parent and the child work on the same object. This is so because we are using the queue and semaphore from the `multiprocessing` module. Had we used the ones from the `threading` module then the child would only receive a copy.

## [8] Value

* We can use the `Value` class to create a **ctype** object in shared memory. By default the function `Value()` returns a wrapper over the requested object, thus making the reads and writes to the underlying ctype object process-safe.

**Using Value**

```python
from multiprocessing import Value

pi = Value('d', 3.1415)
print(pi.value)
```

* In the above code, we specify the code for the object we want created. The **'d'** specifies double and the second argument is passed over to the ctype double constructor.
* The third option not listed above is a boolean which, if set to false, will return an object without synchronized access. On the other hand, if set to true, a recursive lock is automatically created to guard access to the object. We can also specify an external lock and pass that instead of a boolean value. The passed-in lock is then used to synchronize access to the created object.

### Array

* `Array` is very similar to how we use `Value`. Below is a sample script demonstrating how to use Array.

```python
from multiprocessing import Process, Semaphore, Array
import multiprocessing

def child_process(sem1, sem2, arr):
    print("Child process received var = {0} with id {1} from queue".format(str(arr[0]), id(arr)), flush=True)
    sem1.release()
    sem2.acquire()

    print("After changes by parent process, child process sees var as = {0}".format(arr[0]), flush=True)


if __name__ == '__main__':
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    arr = Array('i', range(5))
    print("Parent process puts item on queue with id " + str(id(arr)))

    process = Process(target=child_process, args=(sem1, sem2, arr))
    process.start()

    sem1.acquire()

    # change var and verify the change is reflected in the child process
    arr[0] += 100
    print("Parent process changed the enqueued item to " + str(arr[0]), flush=True)
    sem2.release()
    process.join()

```

Note that these shared state objects can only be **inherited** by the child process. Trying to pass them via a `Queue` or a `Pipe` will result in an error. An example of the failure is shown below:

```python
from multiprocessing import Process, Value, Queue
import multiprocessing


def child_process( var, q):
    print("Child process received var = {0} with id {1} from queue".format(str(var.value), id(var)), flush=True)


if __name__ == '__main__':
    q = Queue()
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))

    var = Value('I', 1, lock=False)

    # generates error
    q.put(var)

    print("Parent process puts item on queue with id " + str(id(var)))

    process = Process(target=child_process, args=(var, q))
    process.start()
    process.join()
```

## [9] Locks & Reentrant Lock

### Lock

* Lock is a non-recursive object and shares the same DNA as the `threading.Lock` class. In the section on using Queues and Pipes we introduced a snippet with a bug, that could potentially hang depending on the order in which the two processes consumed objects placed on the queue.

```python
from multiprocessing import Process, Queue, current_process, Lock
import multiprocessing, sys
import random
import time

def child_process(q, lock):
    count = 0
    keep_going = True

    while keep_going:
        lock.acquire()
        if not q.empty():
            print(q.get())
            count += 1
        else:
            keep_going = False
        lock.release()
        # Added this sleep so that not all items get processed by
        # a single process
        time.sleep(0.001)

    print("child process {0} processed {1} items from the queue".format(current_process().name, count), flush=True)


if __name__ == '__main__':

    multiprocessing.set_start_method("forkserver")
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    lock = Lock()
    q = Queue()

    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q, lock))
    p2 = Process(target=child_process, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

```

### RLock

* A reentrant lock can be acquired multiple times by a process without blocking. But remember to release the lock just as many times as it has been acquired. 

```python 
from multiprocessing import Process, RLock, current_process
import multiprocessing
import time


def child_task(rlock):
    for _ in range(0, 5):
        rlock.acquire()
        print("I am child process {0}".format(current_process().name))
        time.sleep(0.01)

    for _ in range(0, 5):
        rlock.release()

if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    rlock = RLock()
    rlock.acquire()

    process1 = Process(target=child_task, args=(rlock,))
    process1.start()

    process2 = Process(target=child_task, args=(rlock,))
    process2.start()

    # sleep 3 seconds before releasing the lock
    time.sleep(3)
    rlock.release()

    process1.join()
    process2.join()
```

## [10] Barrier, Semaphore, Condition Variable

### Semaphore

* The `multiprocessing.Semaphore` is very similar to `threading.Semaphore`.
* The script uses `multiprocessing.Semaphore` initialized to zero. Additionally, we also use a `multiprocessing.Value` boolean object to indicate to the two processes to exit.

```python
from multiprocessing import Semaphore, Process, Value
from ctypes import c_bool
import time
import multiprocessing


def process_A(sem1, sem2, exit):
    while not exit.value:
        print("ping", flush=True)
        sem1.release()
        sem2.acquire()
        time.sleep(0.05)


def process_B(sem1, sem2, exit):
    while not exit.value:
        # wait for a prime number to become available
        sem1.acquire()
        print("pong", flush=True)
        sem2.release()
        time.sleep(0.05)


if __name__ == '__main__':
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)

    exit_prog = Value(c_bool, False)

    processA = Process(target=process_A, args=(sem1, sem2, exit_prog))
    processA.start()

    processB = Process(target=process_B, args=(sem1, sem2, exit_prog))
    processB.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog.value = True

    processA.join()
    processB.join()

```

### Barrier

* The `multiprocessing.Barrier` is similar in behavior to `threading.Barrier`.

```python
from multiprocessing import Barrier, Process, current_process
import random
import time


def process_task():
    time.sleep(random.randint(0, 5))
    print("\nCurrently {0} processes blocked on barrier".format(barrier.n_waiting), flush=True)
    barrier.wait()


def when_all_processes_released():
    print("\nAll processes released, reported by {0}".format(current_process().name), flush=True)


num_processes = 5
barrier = Barrier(num_processes, action=when_all_processes_released)
processes = [0] * num_processes

for i in range(num_processes):
    processes[i - 1] = Process(target=process_task)

for i in range(num_processes):
    processes[i].start()

```

### Condition Variable

* The `multiprocessing.Condition`works very similarly to `threading.Condition`. 

## [11] Pool

* The `Pool` object consists of a group of processes that can receive tasks for execution. The concept is very similar to a **thread pool**.
* Creating and tearing down threads is expensive so most programming language frameworks provide a notion of a pool of threads.
* Once a thread is done executing a task, it is returned back to the pool rather than being terminated. The process pool concept is similar where the processes are kept alive till there are tasks to be executed.
* The above program submits an integer to the pool to get the square of its value. If you run the below program you'll see the output showing PIDs of two different processes. One is the main process and the other is the pool process that actually does the computation.

```python
from multiprocessing import Pool
import os
import time


def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".format(os.getpid(), main_id))


def square(x):
    return x * x


if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(processes=1,
                initializer=init,
                initargs=(main_process_id,),
                maxtasksperchild=1)

    result = pool.apply(square, (3,))
    print(result)

    time.sleep(6)

```

An asynchronous variant of the same method is available by the name of `apply_async()`. This non-blocking variant also takes in callbacks for success and failure. We rewrite the same program using the asynchronous version.

**Using asynchronous apply**

```python
from multiprocessing import Pool
import os
import time


def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".format(os.getpid(), main_id))


def square(x):
    return x * x


def on_success(result):
    print("result is " + str(result))


def on_error(err):
    print("error is " + str(err))


if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(processes=1,
                initializer=init,
                initargs=(main_process_id,),
                maxtasksperchild=2)

    result = pool.apply_async(square, (9,), callback=on_success, error_callback=on_error)

    # prevent main from exiting before the pool process completes
    time.sleep(6)

```

* If you pay attention at the output of the program, you'll notice that the initialization method is called twice since its print statement appears twice. The first time it gets printed is when we set-up the pool. 
* If you comment out **line#30** you'll still see the initialization method being invoked because the pool creates worker processes. Next, one of the pool workers executes our task and then exits because we have set **maxtasksperchild** to be exactly 1. This is why the two print statements show the worker processes having different pids. 
* If you change the **maxtasksperchild** to 2 in the above code the second print statement would disappear because the remaining 1 pool is not assigned any tasks yet and hence the pool exists.

### ThreadPoolExecutor

* The `ThreadPoolExecutor` uses threads for executing submitted tasks. Let's look at a very simple example.

```python
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread


def say_hi(item):

    print("\nhi " + str(item) + " executed in thread id " + current_thread().name, flush=True)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)
    lst = list()
    for i in range(1, 10):
        lst.append(executor.submit(say_hi, "guest" + str(i)))

    for future in lst:
        future.result()

    executor.shutdown()
```

#### Map

* The `map()` returns an iterator over the results of applying a function to a list of values. Both the function and the values are passed-in as parameters to the `map()` call.
* In our example `square()` is the callable. Internally, the iterator's `__next()__` calls the `result()` method of the future, which is a blocking call. If the result isn't ready for one of the futures, the iteration will block.
* To mitigate this situation, we can specify a timeout value in the map call and if the result isn't ready after timeout number of seconds have elapsed, a `Timeout` exception is raised.
* We are able to iterate over the futures which have completed but the first future encountered whose computation hasn't completed will result in blocking the iteration.

```python
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time


def square(item):
    if item == 5:
        time.sleep(10)
    return item * item


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                     chunksize=1, timeout=2)

    for sq in it:
        print(sq)

    executor.shutdown()

```

* Lastly, note that the argument **chunksize** will have no effect when used with a thread pool.

### ProcessPoolExecutor

* The process pool is very similar to a thread pool except that it is pool of processes that execute the task rather than threads. Let's rewrite one of the previous examples using a process pool instead of a thread pool.
* The only major difference when using `map()` with threads vs processes is the effect of the **chunksize** argument. In the above example, we have set the chunksize to one which implies each square will be calculated by a different process. If we change the chunksize to five then we only require two processes to square the ten input values. Depending on the usecase it may happen that a chunksize set to a higher value results in faster execution as time is saved in creating and then tearing down more number of processes.



