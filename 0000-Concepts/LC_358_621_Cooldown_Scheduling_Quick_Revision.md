# LC 358 & LC 621 — Cooldown Scheduling: Quick Revision

## Pattern

**Greedy + Max Heap + Cooldown Queue**: always schedule the most frequent *currently available* task/character, then keep it in cooldown until it can be used again.

| | LC 358: Rearrange String k Distance Apart | LC 621: Task Scheduler |
|---|---|---|
| Goal | Construct valid rearrangement | Minimum number of CPU intervals |
| Separation | Same letters' indices differ by **at least `k`** | At least **`n` slots between** equal tasks |
| Idle allowed? | **No**; impossible → `""` | **Yes**; idle counts toward answer |
| Equivalent separation | `k` | `n + 1` |
| Best approach | Max heap + cooldown queue | Frequency formula, or heap + queue |

**Translation:** `k = n + 1`. For LC 358, `k <= 1` means no restriction.

## Core intuition

- **Heap** stores characters/tasks available now, ordered by highest remaining frequency (`-count` in Python).
- **Queue** stores characters/tasks temporarily on cooldown.
- **Why greedy?** Scheduling frequent items first spreads the hardest-to-place items apart.
- **Crucial fork:** If the heap is empty but cooldown is not, **LC 358 fails**, whereas **LC 621 idles**.

## LC 358 — Rearrange String k Distance Apart

Example: `s = "aabbcc", k = 3` → `"abcabc"` is valid.

```python
from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        heap = [(-cnt, ch) for ch, cnt in Counter(s).items()]
        heapify(heap)
        cooldown = deque()  # (negative remaining count, character)
        ans = []

        while heap:
            cnt, ch = heappop(heap)
            ans.append(ch)
            cnt += 1  # negative count moves toward 0
            cooldown.append((cnt, ch))

            # A character chosen k positions ago is now eligible.
            if len(cooldown) >= k:
                old_cnt, old_ch = cooldown.popleft()
                if old_cnt < 0:
                    heappush(heap, (old_cnt, old_ch))

        return "".join(ans) if len(ans) == len(s) else ""
```

**Why queue length `k`?** If `a` is chosen at index `0`, it can next be chosen at index `k`. After filling indices `0..k-1`, release it for the next choice.

**Complexity:** `O(N log U)` time and `O(N + U)` space including output (where `U` is the number of distinct characters; the queue contains at most `min(k, N, U)` active/cooling entries). For lowercase English letters, `U <= 26`.

## LC 621 — Task Scheduler: heap + queue

Example: `tasks = AAABBB`, `n = 2` → `A B idle A B idle A B`, length **8**.

```python
from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapify(heap)
        cooldown = deque()  # (ready_time, negative remaining count)
        time = 0

        while heap or cooldown:
            if heap:
                cnt = heappop(heap) + 1
                if cnt < 0:
                    cooldown.append((time + n + 1, cnt))

            time += 1  # advances even if heap empty => idle

            if cooldown and cooldown[0][0] <= time:
                _, cnt = cooldown.popleft()
                heappush(heap, cnt)

        return time
```

**Off-by-one check:** If `A` runs at time `0` and `n = 2`, next `A` is allowed at time `3` (`0 + n + 1`).

**Complexity:** `O(T log U)` time, `O(U)` space, where `T` is total schedule length (including idle) and `U <= 26`.

## LC 621 — O(N) frequency formula (preferred if only length is needed)

Let:
- `N` = number of tasks
- `f` = maximum frequency of any task
- `m` = number of task types tied at frequency `f`

```text
Most frequent tasks define f - 1 full blocks:
A _ _ | A _ _ | A
  each block has width n + 1

If A, B both have max frequency:
A B _ | A B _ | A B
                   ↑ final group contains m max-frequency tasks
```

Thus:

**`answer = max(N, (f - 1) * (n + 1) + m)`**

Why `max(N, ...)`? We must execute all `N` tasks; when other task types fill every cooldown gap, no idle is needed.

```python
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        f = max(freq.values())
        m = sum(cnt == f for cnt in freq.values())
        return max(len(tasks), (f - 1) * (n + 1) + m)
```

**Complexity:** `O(N)` time, `O(1)` auxiliary space for the fixed 26-letter task alphabet.

## LC 358 — quick feasibility check

Replace the LC 621 minimum separation `n + 1` with `k`:

**Possible iff `(f - 1) * k + m <= N`**, for `k >= 1`.

Example: `s = "aaabc", k = 3`: `f=3, m=1, N=5`; required positions `7 > 5`, so **impossible**.

This formula checks **existence**, but LC 358 still requires constructing the string (e.g. using the heap + queue).

## Interview memory hooks

1. **Need actual order?** → Heap + cooldown queue.
2. **Only minimum number of intervals (LC 621)?** → Frequency formula.
3. **Empty heap, items cooling?** → LC 358: return `""`; LC 621: idle.
4. **Distance vs gap:** LC 358 `k` ↔ LC 621 `n + 1`.
5. **Related:** LC 767 Reorganize String = LC 358 with `k = 2`.

## Quick examples

| Problem | Input | Result |
|---|---|---|
| 358 | `s="aabbcc", k=3` | `"abcabc"` |
| 358 | `s="aaabc", k=3` | `""` |
| 621 | `tasks=AAABBB, n=2` | `8` |
| 621 | `tasks=AAABBBCCC, n=2` | `9` |

**Key takeaway:** Both are *frequency-based scheduling under a cooldown constraint*. LC 358 constructs a no-idle arrangement; LC 621 permits idle and has a closed-form optimal length.
