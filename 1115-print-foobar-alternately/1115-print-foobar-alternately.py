import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = threading.Lock()
        self.barlock = threading.Lock()
        self.barlock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foolock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barlock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.barlock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foolock.release()