
# Greedy Scheduling with Cooldowns — LeetCode Quick Revision

## 1. Recognize the pattern

**Signal:** Repeated items/tasks must be separated, or a task becomes eligible only after a wait.

| Question | Technique |
|---|---|
| Can tasks be reordered? | **No:** hash map of last/next eligible time (LC 2365). **Yes:** greedy selection. |
| Must identical items be at least `k` positions apart? | Max heap + cooldown queue (LC 358). |
| Are idle intervals allowed? | Advance time even if heap is empty (LC 621). |
| Only adjacent duplicates forbidden? | Max heap + hold last item (LC 767, 1054). |
| Constraint depends on last two output chars? | Max heap + check recent suffix (LC 1405). |
| Only minimum duration required? | Consider LC 621 frequency formula. |

**Spacing conversion:** LC 358 index distance `k` corresponds to LC 621 cooldown `n = k - 1` (there must be `n` intervals *between* identical tasks).

## 2. Core problems

| LC | Problem | Variant | Key idea |
|---|---|---|---|
| [767](https://leetcode.com/problems/reorganize-string/) | Reorganize String | No adjacent equals | Max heap + hold previous |
| [1054](https://leetcode.com/problems/distant-barcodes/) | Distant Barcodes | No adjacent equals | Same pattern with integers; valid answer guaranteed |
| [358](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | Rearrange String k Distance Apart | General separation | Max heap + cooldown FIFO; **no idle** |
| [621](https://leetcode.com/problems/task-scheduler/) | Task Scheduler | General separation | Max heap + cooldown; **idle permitted**; or formula |
| [2365](https://leetcode.com/problems/task-scheduler-ii/) | Task Scheduler II | **Order fixed** | Hash map of last execution day |
| [1405](https://leetcode.com/problems/longest-happy-string/) | Longest Happy String | No three consecutive | Max heap; take second choice if top would violate rule |
| [984](https://leetcode.com/problems/string-without-aaa-or-bbb/) | String Without AAA or BBB | No three consecutive | Similar to 1405; use all characters |
| [1417](https://leetcode.com/problems/reformat-the-string/) | Reformat The String | Alternate types | Greedy alternating groups; no heap needed |

### Related scheduling (not the same cooldown template)

- [1834 — Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/): sort arrivals + min heap of available tasks.
- [1882 — Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/): available-server heap + busy-server heap.
- [253 — Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/): min heap of room end times.
- [2402 — Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/): free-room heap + busy-room heap.

## 3. Reusable templates and solutions (Python)

### A. LC 767 — no equal adjacent characters

```python
from collections import Counter
from heapq import heapify, heappop, heappush

def reorganizeString(s: str) -> str:
    heap = [(-f, c) for c, f in Counter(s).items()]
    heapify(heap)
    prev = (0, '')  # Previous char held out of heap for one turn
    ans = []

    while heap:
        cnt, c = heappop(heap)
        ans.append(c)
        cnt += 1  # Negative frequencies move toward zero

        if prev[0] < 0:
            heappush(heap, prev)
        prev = (cnt, c)

    return ''.join(ans) if len(ans) == len(s) else ''
```

**LC 1054:** Same logic for integers instead of characters; return a list. `prev` stores `(negative_count, value)`.

**Complexity:** `O(N log U)` time, `O(N + U)` space including result; `U` distinct values.

### B. LC 358 — general distance `k`, no idle allowed

```python
from collections import Counter, deque
from heapq import heapify, heappop, heappush

def rearrangeString(s: str, k: int) -> str:
    if k <= 1:
        return s

    heap = [(-f, c) for c, f in Counter(s).items()]
    heapify(heap)
    cooldown = deque()  # (negative_remaining, char)
    ans = []

    while heap:
        cnt, c = heappop(heap)
        ans.append(c)
        cooldown.append((cnt + 1, c))

        # Oldest item can return after k scheduled positions.
        if len(cooldown) >= k:
            old_cnt, old_char = cooldown.popleft()
            if old_cnt < 0:
                heappush(heap, (old_cnt, old_char))

    return ''.join(ans) if len(ans) == len(s) else ''
```

Example: `s='aabbcc', k=3` -> `abcabc` (one valid result).

**Failure:** If heap empties while characters still need scheduling, idle would be necessary, so return `''`.

**Complexity:** `O(N log U)` time; `O(N + U + k)` loose space bound including output (queue actually bounded by `min(k, U)` here).

### C. LC 621 — CPU time, idle allowed

```python
from collections import Counter, deque
from heapq import heapify, heappop, heappush

def leastInterval(tasks: list[str], n: int) -> int:
    heap = [-f for f in Counter(tasks).values()]
    heapify(heap)
    cooldown = deque()  # (next_available_time, negative_remaining)
    time = 0

    while heap or cooldown:
        if heap:
            cnt = heappop(heap) + 1
            if cnt < 0:
                cooldown.append((time + n + 1, cnt))

        time += 1  # Also advances through idle slots
        if cooldown and cooldown[0][0] <= time:
            _, cnt = cooldown.popleft()
            heappush(heap, cnt)

    return time
```

Example: `AAABBB`, `n=2` -> `A B idle A B idle A B` -> **8 intervals**.

**Alternative formula** (when only length is needed):

- `N` = total tasks
- `f` = highest frequency
- `m` = number of task types with frequency `f`

```python
from collections import Counter

def leastInterval_math(tasks: list[str], n: int) -> int:
    if not tasks:
        return 0
    counts = Counter(tasks)
    f = max(counts.values())
    m = sum(v == f for v in counts.values())
    return max(len(tasks), (f - 1) * (n + 1) + m)
```

**Why:** `f - 1` full spacing blocks of width `n + 1`, then `m` final maximum-frequency tasks. Other tasks can fill gaps; the answer cannot be below `N`.

**Complexity:** Simulation `O(T log U)` where `T` includes idle intervals, `O(U)` extra space. Formula `O(N)` time, `O(U)` space (or `O(1)` for a fixed alphabet).

### D. LC 2365 — cooldown with immutable order

```python
def taskSchedulerII(tasks: list[int], space: int) -> int:
    last = {}   # task -> last execution day (0-based)
    day = 0

    for task in tasks:
        if task in last:
            day = max(day, last[task] + space + 1)
        last[task] = day
        day += 1

    return day
```

**Why no heap?** The task order is predetermined; only jump to the next legal execution day.

**Complexity:** `O(N)` time, `O(U)` space.

### E. LC 1405 — block triples, not a fixed cooldown

```python
from heapq import heappush, heappop

def longestDiverseString(a: int, b: int, c: int) -> str:
    heap = []
    for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
        if count:
            heappush(heap, (-count, char))

    ans = []
    while heap:
        cnt1, ch1 = heappop(heap)
        if len(ans) >= 2 and ans[-1] == ans[-2] == ch1:
            if not heap:
                break
            cnt2, ch2 = heappop(heap)
            ans.append(ch2)
            cnt2 += 1
            if cnt2 < 0:
                heappush(heap, (cnt2, ch2))
            heappush(heap, (cnt1, ch1))
        else:
            ans.append(ch1)
            cnt1 += 1
            if cnt1 < 0:
                heappush(heap, (cnt1, ch1))
    return ''.join(ans)
```

**Complexity:** `O(N log U)` time, `O(N + U)` space including output (`U=3`).

## 4. Quick feasibility tests

- **LC 767 (no adjacent equals):** a valid arrangement exists iff `max_frequency <= (N + 1) // 2`.
- **LC 358 (at least `k` apart, with `k >= 2`):** valid iff `(f - 1) * k + m <= N`, with `m` characters tied at maximum frequency `f`. This is the minimum necessary schedule length, without idle.
- **LC 621:** minimum time `max(N, (f - 1) * (n + 1) + m)`.

## 5. Mistakes to avoid

1. **Off-by-one:** LC 358 distance `k` means earliest reuse at index `i + k`; LC 621 cooldown `n` means earliest reuse at time `t + n + 1`.
2. **Treating LC 358 like LC 621:** In LC 358, an idle would become an illegal extra character; return empty if impossible.
3. **Using a heap for LC 2365:** Fixed input order removes the greedy-choice decision.
4. **Pushing a just-used char back too soon:** It must stay blocked until its cooldown ends.
5. **Forgetting ties in LC 621 formula:** Add `m`, not `1`, for the final maximum-frequency block.
6. **Confusing conditional constraints with timed cooldown:** LC 1405 depends on the last two output characters, not elapsed slots.

## 6. Study order

### Must-do (highest ROI)

1. **767** — heap + previous-item hold.
2. **358** — extend to arbitrary `k` via FIFO cooldown.
3. **621** — permit idle; derive frequency formula.
4. **1405** — dynamically disqualify the greedy first choice.

### Good follow-ups

5. **1054** — direct transfer of 767 to integers.
6. **2365** — cooldown, but fixed task order.
7. **984** — fill all characters without triples.
8. **1417** — alternation between groups, no heap.

### Separate heap-scheduling family

**1834 → 1882 → 253 → 2402** (arrival times, resource availability, busy/free heaps rather than repetition cooldown).

## 7. One-minute recap

> **Reorder + distance constraint** → max heap + cooldown queue.
>
> **No idle** → fail if heap empties prematurely.
>
> **Idle allowed** → advance time through empty heap.
>
> **Only adjacency** → hold the previous item.
>
> **Order fixed** → dictionary tracking next legal time.
>
> **Only output length** → check whether a frequency formula applies.



## SRC: https://chatgpt.com/s/t_6ac6bb2e89248191a06d033c6fe9656e