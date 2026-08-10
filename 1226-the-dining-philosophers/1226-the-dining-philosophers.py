from threading import Lock, Semaphore
class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        # Prevent deadlock: max 4 philosophers can "sit down" to eat at once
        self.throttle = Semaphore(4) 

    def wantsToEat(self, philosopher: int, 
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5
        
        self.throttle.acquire()
        
        self.forks[left_fork].acquire()
        self.forks[right_fork].acquire()
        
        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()
        
        self.forks[right_fork].release()
        self.forks[left_fork].release()
        
        self.throttle.release()