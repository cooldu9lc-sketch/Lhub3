from collections import deque
from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.c = Condition()
        self.q = list()
        self.capacity = capacity

    def enqueue(self, element: int) -> None:
        with self.c:
            self.c.wait_for(lambda: len(self.q) < self.capacity)
            self.q.append(element)
            self.c.notify_all()

    def dequeue(self) -> int:
        with self.c:
            self.c.wait_for(lambda: len(self.q) > 0)
            val = self.q.pop(0)
            self.c.notify_all()
            return val
        
    def size(self) -> int:
        return len(self.q)