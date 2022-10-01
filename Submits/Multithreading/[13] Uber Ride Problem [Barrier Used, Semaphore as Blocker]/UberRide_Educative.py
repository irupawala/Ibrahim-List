from threading import Thread
from threading import Semaphore
from threading import current_thread
from threading import Lock
from threading import Barrier
import random


class UberSeatingProblem():

    def __init__(self):
        self.democrats_count = 0
        self.democrats_waiting = Semaphore(0)
        self.republicans_count = 0
        self.republicans_waiting = Semaphore(0)
        self.lock = Lock()
        self.barrier = Barrier(4)
        self.ride_count = 0

    def drive(self):
        self.ride_count += 1
        print("Uber ride # {0} filled and on its way".format(self.ride_count), flush=True)

    def seated(self, party):
        print("\n{0} {1} seated".format(party, current_thread().getName()), flush=True)

    def seat_democrat(self):
        ride_leader = False

        self.lock.acquire()

        self.democrats_count += 1

        if self.democrats_count == 4:
            # release 3 democrats to ride along
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            ride_leader = True
            self.democrats_count -= 4

        elif self.democrats_count == 2 and self.republicans_count >= 2:
            # release 1 democrat and 2 republicans
            self.democrats_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            ride_leader = True

            # remember to decrement the count of dems and repubs
            # selected for next ride
            self.democrats_count -= 2
            self.republicans_count -= 2

        else:
            # can't form a valid combination, keep waiting and release lock
            self.lock.release()
            self.democrats_waiting.acquire()

        self.seated("Democrat")
        self.barrier.wait()

        if ride_leader is True:
            self.drive()
            self.lock.release()

    def seat_republican(self):
        ride_leader = False

        self.lock.acquire()

        self.republicans_count += 1

        if self.republicans_count == 4:
            # release 3 republicans to ride along
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            ride_leader = True
            self.republicans_count -= 4

        elif self.republicans_count == 2 and self.democrats_count >= 2:
            # release 1 republican and 2 democrats
            self.republicans_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            ride_leader = True

            # remember to decrement the count of dems and repubs
            # selected for next ride
            self.republicans_count -= 2
            self.democrats_count -= 2


        else:
            # can't form a valid combination, keep waiting and release lock
            self.lock.release()
            self.republicans_waiting.acquire()

        self.seated("Republican")
        self.barrier.wait()

        if ride_leader is True:
            self.drive()
            self.lock.release()


def random_simulation():
    problem = UberSeatingProblem()
    dems = 0
    repubs = 0

    riders = list()
    for _ in range(0, 16):
        toss = random.randint(0, 1)
        if toss == 1:
            riders.append(Thread(target=problem.seat_democrat))
            dems += 1
        else:
            riders.append(Thread(target=problem.seat_republican))
            repubs += 1

    print("Total {0} dems and {1} repubs".format(dems, repubs), flush=True)
    for rider in riders:
        rider.start()

    for rider in riders:
        rider.join()


def controlled_simulation():
    problem = UberSeatingProblem()
    dems = 10
    repubs = 10
    
    total = dems + repubs
    print("Total {0} dems and {1} repubs\n".format(dems, repubs))

    riders = list()

    while total != 0:
        toss = random.randint(0, 1)
        if toss == 1 and dems != 0:
            riders.append(Thread(target=problem.seat_democrat))
            dems -= 1
            total -= 1
        elif toss == 0 and repubs != 0:
            riders.append(Thread(target=problem.seat_republican))
            repubs -= 1
            total -= 1

    for rider in riders:
        rider.start()

    for rider in riders:
        rider.join()


if __name__ == "__main__":
    controlled_simulation()

    # running the below simulation may hang the
    # program if an allowed combination can't be 
    # made
    #random_simulation()
