import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, num_philosophers):
        self.num_philosophers = num_philosophers
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        self.waiter = threading.Lock()
        
    def get_forks(self, philosopher_id):
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers
        
        self.waiter.acquire()
        self.forks[left_fork].acquire()
        self.forks[right_fork].acquire()
        self.waiter.release()
        
    def put_forks(self, philosopher_id):
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers
        
        self.forks[left_fork].release()
        self.forks[right_fork].release()
        
    def dine(self, philosopher_id):
        #while True:
        t_end = time.time() + 15
        while time.time() < t_end:
            print(f'Philosopher {philosopher_id} is thinking')
            time.sleep(random.uniform(1, 3))
            print(f'Philosopher {philosopher_id} is hungry')
            self.get_forks(philosopher_id)
            print(f'Philosopher {philosopher_id} is eating')
            time.sleep(random.uniform(1, 3))
            self.put_forks(philosopher_id)

if __name__ == "__main__":
    num_philosophers = 3
    philosophers = []
    dining_table = DiningPhilosophers(num_philosophers)

    for i in range(num_philosophers):
        philosopher = threading.Thread(target=dining_table.dine, args=(i,))
        philosophers.append(philosopher)
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()
