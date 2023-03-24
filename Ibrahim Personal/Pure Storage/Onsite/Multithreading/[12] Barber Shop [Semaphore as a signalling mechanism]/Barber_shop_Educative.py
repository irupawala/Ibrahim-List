from threading import Thread
from threading import Semaphore
from threading import Lock
import time


class BarberShop:

    def __init__(self):
        self.total_chairs = 3
        self.waiting_customers = 0
        self.haircuts_given = 0
        self.lock = Lock()
        self.wait_for_customer_to_enter = Semaphore(0)
        self.wait_for_barber_to_get_ready = Semaphore(0)
        self.wait_for_barber_to_get_ready = Semaphore(0)
        self.wait_for_barber_to_cut_hair = Semaphore(0)
        self.wait_for_customer_to_leave = Semaphore(0)

    def customer_walks_in(self):
        with self.lock:
            if self.waiting_customers == self.total_chairs:
                print("Customer walks out, all chairs occupied")
                return

            self.waiting_customers += 1

        self.wait_for_customer_to_enter.release()
        self.wait_for_barber_to_get_ready.acquire()
        
        with self.lock:
            self.waiting_customers -= 1

        self.wait_for_barber_to_cut_hair.acquire()
        self.wait_for_customer_to_leave.release()



    def barber(self):

        while True:
            self.wait_for_customer_to_enter.acquire()
            self.wait_for_barber_to_get_ready.release()

            self.haircuts_given += 1

            print("Barber cutting hair ... {0}".format(self.haircuts_given))
            time.sleep(0.05)

            self.wait_for_barber_to_cut_hair.release()
            self.wait_for_customer_to_leave.acquire()


if __name__ == "__main__":

    barber_shop = BarberShop()

    barber_thread = Thread(target=barber_shop.barber)
    barber_thread.setDaemon(True)
    barber_thread.start()

    # intially 10 customers enter the barber shop one after the other
    customers = list()
    for _ in range(0, 10):
        customers.append(Thread(target=barber_shop.customer_walks_in))

    for customer in customers:
        customer.start()

    time.sleep(0.5)

    # second wave of 5 customers
    late_customers = list()
    for _ in range(0, 5):
        late_customers.append(Thread(target=barber_shop.customer_walks_in))

    for customer in late_customers:
        customer.start()

    for customer in customers:
        customer.join()

    for customer in late_customers:
        customer.join()
