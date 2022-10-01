from threading import Thread
from threading import Semaphore
import random
import time


class DiningPhilosopherProblem:

    def __init__(self):
        self.forks = [Semaphore(1) for _ in range(5)]
        self.max_diners = Semaphore(4)
        self.exit = False

    def life_cycle_of_a_philosopher(self, id):
        while self.exit is False:
            self.contemplate()
            self.eat(id)

    def contemplate(self):
        sleep_for = random.randint(800, 1200) / 1000
        time.sleep(sleep_for)

    def eat(self, id):
        # maxDiners allows only 4 philosophers to
        # attempt picking up forks.
        left, right =  id, (id + 1) % 5
        with self.max_diners:
            with self.forks[left], self.forks[right]:
                # eat to your heart's content
                print("Philosopher {0} is eating".format(id))


if __name__ == "__main__":

    problem = DiningPhilosopherProblem()

    philosophers = list()

    for id in range(0, 5):
        philosophers.append(Thread(target=problem.life_cycle_of_a_philosopher, args=(id,)))

    for philosopher in philosophers:
        philosopher.start()

    time.sleep(6)
    problem.exit = True

    for philosopher in philosophers:
        philosopher.join()
