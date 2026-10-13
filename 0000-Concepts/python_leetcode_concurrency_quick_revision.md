# Python Concurrency — LeetCode Quick Revision

> **Core idea:** Threads are already provided by LeetCode. Your job is to coordinate *ordering*, *turns*, *shared state*, *resource limits*, and *termination*.

## 1. Pattern → Primitive → Problems

| Problem signal | Reach for | LeetCode |
|---|---|---|
| A must finish before B | `Event`, `Semaphore(0)` | 1114 |
| Alternating turns | Two `Semaphore`s | 1115 |
| One thread selects next worker | Multiple `Semaphore`s | 1116 |
| Eligibility depends on shared state | `Condition` + predicate | 1195 |
| Exactly k participants per group | `Semaphore` + `Barrier` | 1117 |
| Queue full/empty blocking | `Condition` or two `Semaphore`s + `Lock` | 1188 |
| Acquiring multiple shared resources | Ordered `Lock`s | 1226 |
| One atomic multi-step action | `Lock` | 1279 |
| Parallel I/O + deduplication | `ThreadPoolExecutor`, `Queue`, `Lock` | 1242 |

**Priority:** 1114 → 1115 → 1116 → 1195 → 1117 → 1188 → 1226 → 1279 → 1242.

---

## 2. Python concurrency primitives — methods you need

### `threading.Thread`

```python
from threading import Thread

t = Thread(target=fn, args=(arg1, arg2))
t.start()                # schedule execution
t.join()                 # block until finished
t.is_alive()             # whether thread is still running
```

| Method / argument | Meaning |
|---|---|
| `Thread(target=..., args=(...))` | Configure worker (`args` must be a tuple) |
| `.start()` | Start once; raises if started again |
| `.join(timeout=None)` | Wait until completion or timeout; returns `None` |
| `.is_alive()` | True while thread is active |
| `daemon=True` | Daemon threads don't keep interpreter alive; avoid for required cleanup |

### `threading.Lock`

```python
from threading import Lock
lock = Lock()
with lock:
    update_shared_state()
# or lock.acquire(); try: ...; finally: lock.release()
```

| Method | Meaning |
|---|---|
| `.acquire(blocking=True, timeout=-1)` | Obtain exclusive access; returns bool; `blocking=False` tries immediately |
| `.release()` | Unlock; raises if unlocked (primitive Lock need not be released by acquirer) |
| `.locked()` | Snapshot of locked status; **not** an atomic condition for later operations |
| `with lock:` | Acquire on entry, release on exit; preferred |

**Use:** protect `visited` set, counter, fork, car crossing. **Pitfall:** don't do slow/blocking I/O while holding it unless essential.

### `threading.RLock`

| Method | Meaning |
|---|---|
| `.acquire(...)`, `.release()`, `with rlock:` | Like Lock, but the **same thread** may acquire repeatedly; must release once per acquisition |

**Use:** nested synchronized methods; not needed for most LeetCode questions.

### `threading.Semaphore` / `BoundedSemaphore`

```python
from threading import Semaphore
ready = Semaphore(0)     # no initial permission
ready.release()          # signal / add one permit
ready.acquire()          # wait / consume one permit

capacity = Semaphore(3)  # allow at most 3 concurrent entrants
with capacity:
    use_resource()
```

| Method | Meaning |
|---|---|
| `Semaphore(value=k)` | Initialize permit counter to k |
| `.acquire(blocking=True, timeout=None)` | Consume permit or block; returns bool |
| `.release(n=1)` | Return n permits; can wake waiting threads |
| `with sem:` | Acquire and release one permit around block |
| `BoundedSemaphore(k)` | Like Semaphore, but `.release()` past initial bound raises `ValueError` |

**Use:** alternation, permits, capacity limits. **Pitfall:** `Semaphore(0)` starts *blocked*, `Semaphore(1)` starts *available*; extra releases on ordinary Semaphore accumulate.

### `threading.Event`

```python
from threading import Event
finished = Event()
finished.wait()          # blocks until flag set
finished.set()           # wakes all waiters and stays set
finished.clear()         # resets flag
```

| Method | Meaning |
|---|---|
| `.set()` | Make flag true; awaken all waiters |
| `.wait(timeout=None)` | Wait until flag true or timeout; returns bool |
| `.clear()` | Reset flag to false |
| `.is_set()` | Snapshot of flag state |

**Use:** one-time A → B dependency. **Pitfall:** `.set()` stays set until cleared; not a turn-taking counter.

### `threading.Condition`

```python
from threading import Condition
cv = Condition()          # owns an RLock by default

with cv:
    cv.wait_for(lambda: state_is_ready())
    update_state()
    cv.notify_all()
```

| Method | Meaning |
|---|---|
| `Condition(lock=None)` | Create condition using supplied lock or new RLock |
| `.wait(timeout=None)` | Atomically release condition lock, block, then reacquire; returns bool |
| `.wait_for(predicate, timeout=None)` | Loop checking predicate under lock; returns final predicate result |
| `.notify(n=1)` | Wake up to n waiters; caller must hold lock |
| `.notify_all()` | Wake all waiters; caller must hold lock |
| `.acquire()`, `.release()`, `with cv:` | Manipulate associated lock |

**ALWAYS** wait in a loop / use `wait_for`. Wakeups do **not** guarantee the predicate is true; `notify` does not release the lock until the notifying thread exits its critical section. Include a termination predicate to prevent threads hanging after work ends.

### `threading.Barrier`

```python
from threading import Barrier
barrier = Barrier(3)
# Each of 3 participating threads:
barrier.wait()           # all must arrive before any proceeds
```

| Method / property | Meaning |
|---|---|
| `Barrier(parties, action=None, timeout=None)` | Fixed-size, reusable synchronization point |
| `.wait(timeout=None)` | Arrive + wait; returns distinct integer 0..parties-1 |
| `.reset()` | Reset barrier; existing waiters can receive `BrokenBarrierError` |
| `.abort()` | Mark broken; wake waiters with `BrokenBarrierError` |
| `.parties`, `.n_waiting`, `.broken` | Participant count, current waiters, broken state |

**Use:** exactly 3 threads form an H₂O group. **Pitfall:** if a participant never arrives, others can wait indefinitely unless timeout/abort is used.

### `queue.Queue` (thread-safe producer/consumer)

```python
from queue import Queue, Empty, Full
q = Queue(maxsize=10)
q.put(item)              # blocks if full
item = q.get()           # blocks if empty
try:
    process(item)
finally:
    q.task_done()
q.join()                  # wait until all enqueued items marked done
```

| Method | Meaning |
|---|---|
| `Queue(maxsize=k)` | Thread-safe bounded FIFO (0 = unbounded) |
| `.put(item, block=True, timeout=None)` | Add; may block / raise `Full` |
| `.get(block=True, timeout=None)` | Remove; may block / raise `Empty` |
| `.put_nowait(item)`, `.get_nowait()` | Non-blocking variants |
| `.task_done()` | Mark one fetched job complete |
| `.join()` | Wait for unfinished task counter to reach zero |
| `.qsize()`, `.empty()`, `.full()` | **Approximate** snapshots; not correctness checks |

**Important:** one `.task_done()` for each `.get()` (including sentinels). `q.join()` is about task completion, not thread termination; join worker threads separately.

### `concurrent.futures.ThreadPoolExecutor` + `Future`

```python
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, as_completed
with ThreadPoolExecutor(max_workers=8) as pool:
    future = pool.submit(fetch, url)
    result = future.result()     # waits, then returns or re-raises exception
    results = list(pool.map(fetch, urls))
```

| API | Meaning |
|---|---|
| `ThreadPoolExecutor(max_workers=k)` | Create a bounded number of worker threads |
| `pool.submit(fn, *args)` | Schedule one call; returns Future |
| `pool.map(fn, iterable)` | Map work; results yielded in input order |
| `pool.shutdown(wait=True, cancel_futures=False)` | Shutdown pool; `with` does this automatically |
| `future.result(timeout=None)` | Wait for result or raise worker exception |
| `future.done()` / `.running()` / `.cancelled()` | State checks |
| `future.cancel()` | Attempt to cancel work not yet running |
| `wait(futures, return_when=FIRST_COMPLETED)` | Wait for any completed future; returns `(done, not_done)` sets |
| `as_completed(futures)` | Iterate completed futures in completion order |

**Pitfall:** tasks running inside a fixed-size pool can deadlock if they block waiting on other tasks submitted to that same exhausted pool. Prefer coordinator-owned `visited` state for LC 1242.

---

## 3. The 9 problems — drop-in Python solutions

> LeetCode provides callback functions (`printFoo`, `turnGreen`, etc.). Callbacks are placeholders supplied by the judge, not functions you implement.

### 1114. Print in Order — Event

```python
from threading import Event

class Foo:
    def __init__(self):
        self.a = Event()
        self.b = Event()

    def first(self, printFirst):
        printFirst()
        self.a.set()

    def second(self, printSecond):
        self.a.wait()
        printSecond()
        self.b.set()

    def third(self, printThird):
        self.b.wait()
        printThird()
```

**Alternative:** two `Semaphore(0)` objects; each stage `.release()`s the next. **Time:** O(1) operations, **space:** O(1); blocked duration depends on scheduling.

### 1115. Print FooBar Alternately — two Semaphores

```python
from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_turn = Semaphore(1)
        self.bar_turn = Semaphore(0)

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_turn.acquire()
            printFoo()
            self.bar_turn.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_turn.acquire()
            printBar()
            self.foo_turn.release()
```

**Alternative:** `Condition` + `turn` flag, `wait_for(lambda: turn == ...)`, toggle, `notify_all()`. **Time:** O(n), **space:** O(1).

### 1116. Print Zero Even Odd — three Semaphores

```python
from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z = Semaphore(1)
        self.odd_sem = Semaphore(0)
        self.even_sem = Semaphore(0)

    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.z.acquire()
            printNumber(0)
            (self.odd_sem if i % 2 else self.even_sem).release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.z.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.z.release()
```

**Alternative:** `Condition` + `turn in {zero, odd, even}`. **Time:** O(n), **space:** O(1).

### 1195. FizzBuzz Multithreaded — Condition + predicates

```python
from threading import Condition

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.cv = Condition()

    def run(self, predicate, callback):
        while True:
            with self.cv:
                self.cv.wait_for(lambda: self.i > self.n or predicate(self.i))
                if self.i > self.n:
                    return
                callback(self.i)
                self.i += 1
                self.cv.notify_all()

    def fizz(self, printFizz):
        self.run(lambda i: i % 3 == 0 and i % 5 != 0,
                 lambda i: printFizz())

    def buzz(self, printBuzz):
        self.run(lambda i: i % 5 == 0 and i % 3 != 0,
                 lambda i: printBuzz())

    def fizzbuzz(self, printFizzBuzz):
        self.run(lambda i: i % 15 == 0,
                 lambda i: printFizzBuzz())

    def number(self, printNumber):
        self.run(lambda i: i % 3 != 0 and i % 5 != 0, printNumber)
```

**Alternative:** dedicated semaphores with a coordinator selecting next worker (requires an extra dispatcher thread; not drop-in for the standard four-worker API). **Time:** O(n) useful work plus notification overhead, **space:** O(1).

### 1117. Building H2O — quota Semaphores + Barrier

```python
from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        self.group = Barrier(3)

    def hydrogen(self, releaseHydrogen):
        with self.h:
            releaseHydrogen()
            self.group.wait()

    def oxygen(self, releaseOxygen):
        with self.o:
            releaseOxygen()
            self.group.wait()
```

**Alternative:** `Condition`, quotas (`h_slots=2`, `o_slots=1`), and an atomic 3-member completion counter. **Time:** O(1) per atom (excluding waits), **space:** O(1).

### 1188. Design Bounded Blocking Queue — Semaphores + Lock

```python
from threading import Semaphore, Lock
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.q = deque()
        self.empty_slots = Semaphore(capacity)
        self.available_items = Semaphore(0)
        self.lock = Lock()

    def enqueue(self, element: int) -> None:
        self.empty_slots.acquire()       # BEFORE lock
        with self.lock:
            self.q.append(element)
        self.available_items.release()

    def dequeue(self) -> int:
        self.available_items.acquire()  # BEFORE lock
        with self.lock:
            x = self.q.popleft()
        self.empty_slots.release()
        return x

    def size(self) -> int:
        with self.lock:
            return len(self.q)
```

**Alternatives:** `Condition.wait_for(len(q) < capacity / len(q) > 0)` or built-in `Queue(maxsize=capacity)` (`qsize()` is approximate). **Time:** O(1) enqueue/dequeue, **space:** O(capacity).

### 1226. Dining Philosophers — global lock ordering

```python
from threading import Lock

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork,
                   eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5
        first, second = sorted((left, right))

        with self.forks[first]:
            with self.forks[second]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
```

**Alternatives:** `Semaphore(4)` limiting philosophers trying to pick up forks + per-fork Locks; single global Lock (correct, but serializes all eating). **Time:** O(1) per call excluding waits, **space:** O(1).

### 1279. Traffic Light Controlled Intersection — Lock

```python
from threading import Lock

class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.green = 1

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        with self.lock:
            if self.green != roadId:
                turnGreen()
                self.green = roadId
            crossCar()
```

**Alternative:** `Condition` + `busy` flag (more complex than necessary). **Time:** O(1) per car excluding waits, **space:** O(1).

### 1242. Web Crawler Multithreaded — Futures, single owner for `visited`

```python
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from urllib.parse import urlsplit

class Solution:
    def crawl(self, startUrl, htmlParser):
        hostname = urlsplit(startUrl).hostname
        visited = {startUrl}

        with ThreadPoolExecutor(max_workers=8) as pool:
            pending = {pool.submit(htmlParser.getUrls, startUrl)}

            while pending:
                done, pending = wait(pending, return_when=FIRST_COMPLETED)
                for future in done:
                    for url in future.result():
                        if urlsplit(url).hostname != hostname:
                            continue
                        if url in visited:
                            continue
                        visited.add(url)
                        pending.add(pool.submit(htmlParser.getUrls, url))

        return list(visited)
```

**Why no lock?** Only coordinator accesses `visited`; worker threads just call `getUrls`. **Alternative:** `Queue` + worker threads; protect `if url not in visited: visited.add(url)` with a Lock; use `task_done()`/`join()` and send sentinel items to stop workers. **Work:** O(V + E) for pages/links (ignoring URL-string lengths), **space:** O(V + E) worst case plus worker state; wall time depends on I/O.

---

## 4. Templates to memorize

### A. One-time ordering

```python
ready = Event()
# A: work(); ready.set()
# B: ready.wait(); work()
```

### B. Alternation

```python
a, b = Semaphore(1), Semaphore(0)
# A: a.acquire(); work_a(); b.release()
# B: b.acquire(); work_b(); a.release()
```

### C. Predicate state machine

```python
with cv:
    cv.wait_for(lambda: can_run(state) or finished(state))
    if finished(state):
        return
    perform_action()
    update_state()
    cv.notify_all()
```

### D. Bounded buffer

```python
empty.acquire()
with mutex: q.append(x)
full.release()

full.acquire()
with mutex: x = q.popleft()
empty.release()
```

### E. Prevent deadlock when acquiring two locks

```python
first, second = sorted((resource_a, resource_b))
with locks[first]:
    with locks[second]:
        work()
```

### F. Parallel independent I/O

```python
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))
```

---

## 5. Failure modes / interview FAQ

| Symptom / question | What to remember |
|---|---|
| Why not `time.sleep()` for ordering? | Scheduling is nondeterministic; a delay is not a guarantee. |
| Why `while`/`wait_for`, not `if`? | Spurious wakeups and competing consumers; always recheck predicate. |
| Why call `notify_all()` under lock? | Mutate state and notify atomically with respect to predicate checks. |
| Does `notify_all()` instantly run everyone? | No; waiters must reacquire the Condition lock. |
| Why can `Semaphore(0)` be acquired at all? | Another thread later calls `.release()`. |
| Why must queue semaphore acquire be **outside** the mutex? | A waiting producer/consumer must not block the opposite side from making progress. |
| Why protect `visited` check-and-add together? | Separate check and insert can schedule duplicate jobs. |
| Must the GIL protect counters/dicts? | No. The GIL is not a substitute for synchronization; free-threaded builds exist too. |
| What is deadlock? | Threads permanently wait on circular resource dependencies. |
| How to avoid Dining Philosophers deadlock? | Global resource ordering or limit simultaneous contenders. |
| What is starvation? | A thread may wait indefinitely even though others keep making progress; deadlock avoidance alone doesn't ensure fairness. |
| Is `qsize()` reliable for deciding `get()`/`put()` won't block? | No, it is a racy snapshot. |
| Does `future.result()` propagate worker errors? | Yes, the worker exception is raised in the waiting caller. |

### Short mental model

- **Lock** = ownership of a critical section.
- **Semaphore** = count of available permits / whose turn it is.
- **Event** = persistent boolean signal.
- **Condition** = wait until shared state satisfies a predicate.
- **Barrier** = wait until all required participants arrive.
- **Queue** = thread-safe distribution of work.
- **ThreadPoolExecutor** = execute blocking work with reusable worker threads.

### Self-test checklist

- [ ] 1114 — Event AND Semaphore solution
- [ ] 1115 — Two semaphores AND Condition
- [ ] 1116 — Three semaphores AND Condition
- [ ] 1195 — Condition with termination predicate
- [ ] 1117 — Semaphores + Barrier; explain molecule boundary
- [ ] 1188 — Two semaphores + mutex; explain acquire order
- [ ] 1226 — Global lock order; explain four Coffman conditions
- [ ] 1279 — Single Lock; explain critical section extent
- [ ] 1242 — Futures + coordinator-owned set; Queue + worker alternative

> **Final one-liner:** Ordering → `Event`/`Semaphore`; turns → `Semaphore`; predicates → `Condition`; group synchronization → `Barrier`; exclusive state → `Lock`; bounded work → `Queue`; I/O parallelism → `ThreadPoolExecutor`.
