from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        # Only allow 2 H threads at a time
        self.sem_h = Semaphore(2)
        # Only allow 1 O thread at a time
        self.sem_o = Semaphore(1)
        # Wait for 3 threads (2H + 1O) before releasing them
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem_h.acquire()
        self.barrier.wait() # Wait for the other H and the O
        releaseHydrogen()
        self.sem_h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.sem_o.acquire()
        self.barrier.wait() # Wait for the two H's
        releaseOxygen()
        self.sem_o.release()