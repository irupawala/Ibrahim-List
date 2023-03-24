from threading import Thread
from threading import Semaphore
from threading import Condition
from threading import current_thread
import time


class AsyncExecutor:

    def work(self, callback):
        # simulate work
        time.sleep(5)
        # work is done so now invoke callback
        callback()

    def execute(self, callback):
        Thread(target=self.work, args=(callback,)).start()


class SyncExecutor(AsyncExecutor):

    def __init__(self):
        self.sem = Semaphore(0)

    def work(self, callback):
        super().work(callback)
        self.sem.release()

    def execute(self, callback):
        super().execute(callback)
        self.sem.acquire()


def say_hi():
    print("Hi")


if __name__ == "__main__":
    exec = SyncExecutor()
    exec.execute(say_hi)

    print("main thread exiting")


###############################################################################################################################################################################


# Using Condition Variables
    
class AsyncExecutor:

    def work(self, callback):
        time.sleep(5)
        callback()

    def execute(self, callback):
        Thread(target=self.work, args=(callback,)).start()


class SyncExecutor(AsyncExecutor):

    def __init__(self):
        self.cond = Condition()
        self.is_done = False

    def work(self, callback):
        super().work(callback)

        print("{0} thread notifying".format(current_thread().getName()))
        self.cond.acquire()
        self.cond.notifyAll()
        self.is_done = True
        self.cond.release()

    def execute(self, callback):
        super().execute(callback)

        self.cond.acquire()
        while self.is_done is False:
            self.cond.wait()
        print("{0} thread woken-up".format(current_thread().getName()))
        self.cond.release()


def say_hi():
    print("Hi")


if __name__ == "__main__":
    exec = SyncExecutor()
    exec.execute(say_hi)

    print("main thread exiting")
