from threading import Semaphore, Lock
import collections

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.queue = collections.deque()
        self.capacity_sem = Semaphore(capacity) # Track empty slots
        self.items_sem = Semaphore(0)           # Track filled slots
        self.lock = Lock()                      # Protect queue mutation

    def enqueue(self, element: int) -> None:
        self.capacity_sem.acquire()  # Wait if full
        self.lock.acquire()
        self.queue.append(element)
        self.lock.release()
        self.items_sem.release()     # Signal that an item is available

    def dequeue(self) -> int:
        self.items_sem.acquire()     # Wait if empty
        self.lock.acquire()
        val = self.queue.popleft()
        self.lock.release()
        self.capacity_sem.release()  # Signal that space freed up
        return val

    def size(self) -> int:
        self.lock.acquire()
        sz = len(self.queue)
        self.lock.release()
        return sz