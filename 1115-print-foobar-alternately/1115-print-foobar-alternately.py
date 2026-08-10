from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = Semaphore(1) # Foo goes first
        self.bar_sem = Semaphore(0) # Bar waits

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release() # Wake up bar

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release() # Wake up foo