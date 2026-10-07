# LeetCode Interval & Scheduling Patterns — Quick Revision

## 1. The 3 Main Rules

Most interval/scheduling problems reduce to one of these:

### A. Sort by **Start Time**
Use when you need to process intervals from left to right chronologically.

Typical questions:
- Do intervals overlap?
- Can intervals be merged?
- What is the current active interval/range?

Examples:
- LC 56 — Merge Intervals
- LC 57 — Insert Interval
- LC 252 — Meeting Rooms
- LC 1288 — Remove Covered Intervals

---

### B. Sort by **End Time**
Use when you are **greedily choosing intervals**.

Main idea:

> Pick the interval that finishes earliest so you leave maximum room for future intervals.

Typical questions:
- Maximum number of non-overlapping intervals
- Minimum intervals to remove
- Minimum points/arrows needed to cover intervals

Examples:
- LC 435 — Non-overlapping Intervals
- LC 452 — Minimum Number of Arrows to Burst Balloons

---

### C. Sort by **Start Time + Min-Heap of End Times**
Use when **multiple intervals can be active simultaneously**.

Main question:

> Among all currently active intervals, which one finishes first?

Examples:
- LC 253 — Meeting Rooms II
- LC 1353 — Maximum Number of Events That Can Be Attended
- LC 759 — Employee Free Time (heap variant)

---

# 2. Decision Tree

```text
Interval Problem
│
├── Need to MERGE / CHECK OVERLAP?
│       └── Sort by START
│
├── Need MAXIMUM non-overlapping intervals?
│       └── Sort by END
│
├── Need MINIMUM removals?
│       └── Sort by END
│
├── Need to know HOW MANY are active simultaneously?
│       └── Sort by START + MIN-HEAP(end)
│
├── Need to repeatedly pick among CURRENTLY AVAILABLE intervals?
│       └── Sort by START + MIN-HEAP(priority)
│
└── Need global start/end event counts?
        └── Sweep Line
```

---

# 3. Recognition Table

| Problem Type | Sort By | Heap? | Core Idea |
|---|---|---:|---|
| Merge intervals | Start | No | Compare with last merged interval |
| Insert interval | Already sorted / Start | No | Before / overlap / after |
| Detect any overlap | Start | No | Compare adjacent intervals |
| Meeting Rooms | Start | No | Any overlap => impossible |
| Meeting Rooms II | Start | Yes | Heap stores room end times |
| Max non-overlapping intervals | End | No | Keep earliest-finishing interval |
| Minimum removals | End | No | Maximize intervals kept |
| Minimum arrows | End | No | Shoot at earliest possible end |
| Maximum events attended | Start | Yes | Heap active events by end |
| Employee Free Time | Start | Optional | Merge schedules / heap |
| Sweep-line overlap count | Start/end events | Optional | +1 at start, -1 at end |

---

# 4. LC 56 — Merge Intervals

## Recognition

Need to combine overlapping intervals.

### Rule

```text
SORT BY START
```

After sorting, an interval can only overlap the **last merged interval**.

### Code

```python
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        res = []

        for start, end in intervals:
            if not res or res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
```

### Complexity

- Sorting: `O(n log n)`
- Scan: `O(n)`
- Total: `O(n log n)`

---

# 5. LC 57 — Insert Interval

Intervals are already sorted and non-overlapping.

There are exactly **3 phases**:

```text
1. Intervals completely BEFORE newInterval
2. Intervals OVERLAPPING newInterval
3. Intervals completely AFTER newInterval
```

### Code

```python
class Solution:
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)

        # 1. Completely before
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. Overlapping
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        # 3. Completely after
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

### Complexity

`O(n)`

---

# 6. LC 252 — Meeting Rooms

## Question

Can one person attend all meetings?

### Recognition

Only need to detect whether **any two meetings overlap**.

### Rule

```text
SORT BY START
```

Then compare adjacent intervals.

### Code

```python
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
```

### Complexity

`O(n log n)`

---

# 7. LC 253 — Meeting Rooms II

## Question

What is the minimum number of rooms required?

This is different from Meeting Rooms I.

You are no longer asking:

```text
"Is there overlap?"
```

You are asking:

```text
"How many meetings are active simultaneously?"
```

### Rule

```text
SORT BY START
+
MIN-HEAP OF END TIMES
```

The smallest end time tells us which room becomes free first.

### Code

```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])

        heap = []

        for start, end in intervals:
            # Earliest room becomes free
            if heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)
```

### Why only one pop?

For the final minimum room count, one pop is enough because each new meeting needs at most one room.

A more general "active intervals" version may remove all expired intervals:

```python
while heap and heap[0] <= start:
    heapq.heappop(heap)
```

### Complexity

`O(n log n)`

---

# 8. LC 435 — Non-overlapping Intervals

## Question

Minimum intervals to remove so remaining intervals do not overlap.

Equivalent transformation:

```text
minimum removed
=
total intervals - maximum intervals kept
```

So the real problem is:

> Select the maximum number of mutually non-overlapping intervals.

### Rule

```text
SORT BY END
```

Always keep the interval that finishes earliest.

### Code

```python
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        end = float("-inf")
        keep = 0

        for start, finish in intervals:
            if start >= end:
                keep += 1
                end = finish

        return len(intervals) - keep
```

### Complexity

`O(n log n)`

---

# 9. Why Sort by END for Greedy Scheduling?

Suppose we have:

```text
A = [1, 10]
B = [2, 3]
C = [4, 5]
D = [6, 7]
```

If we choose `A`, almost the entire timeline is blocked.

But if we choose the earliest finishing interval:

```text
B -> C -> D
```

we keep 3 intervals.

Therefore:

```text
Earlier finish
        ↓
More remaining space
        ↓
More possible future intervals
```

This is the core greedy argument.

---

# 10. LC 452 — Minimum Number of Arrows to Burst Balloons

Each balloon is an interval.

If several intervals overlap, one arrow can hit all of them.

### Rule

```text
SORT BY END
```

Shoot at the earliest ending balloon.

### Code

```python
class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])

        arrows = 0
        arrow_position = float("-inf")

        for start, end in points:
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows
```

### Complexity

`O(n log n)`

---

# 11. LC 1353 — Maximum Number of Events That Can Be Attended

This is an important variant.

Each event:

```text
[start_day, end_day]
```

You may attend at most one event per day.

## Why simple end-time sorting is NOT enough

Unlike normal activity selection, an event does **not consume its entire interval**.

For:

```text
[1, 4]
```

you attend it on only one day:

```text
1 OR 2 OR 3 OR 4
```

Therefore the set of valid choices changes every day.

We need:

1. Add events that have started.
2. Ignore expired events.
3. Among active events, attend the one ending earliest.

Hence:

```text
SORT BY START
+
MIN-HEAP OF END
```

### Template

```python
events.sort()

heap = []
i = 0
day = 0

while i < len(events) or heap:

    if not heap:
        day = events[i][0]

    while i < len(events) and events[i][0] <= day:
        heapq.heappush(heap, events[i][1])
        i += 1

    while heap and heap[0] < day:
        heapq.heappop(heap)

    if heap:
        heapq.heappop(heap)
        day += 1
```

### Full Code

```python
import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()

        heap = []
        i = 0
        day = 0
        attended = 0

        while i < len(events) or heap:

            if not heap:
                day = events[i][0]

            # Add all events that have started
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove expired events
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # Attend event ending earliest
            if heap:
                heapq.heappop(heap)
                attended += 1
                day += 1

        return attended
```

### Complexity

`O(n log n)`

---

# 12. General Templates

## Template A — Sort by Start / Merge

```python
intervals.sort(key=lambda x: x[0])

res = []

for start, end in intervals:
    if not res or res[-1][1] < start:
        res.append([start, end])
    else:
        res[-1][1] = max(res[-1][1], end)
```

Use for:
- Merge Intervals
- Overlap detection
- Union of intervals

---

## Template B — Greedy Sort by End

```python
intervals.sort(key=lambda x: x[1])

end = float("-inf")
count = 0

for start, finish in intervals:
    if start >= end:
        count += 1
        end = finish
```

Use for:
- Maximum non-overlapping intervals
- Activity selection
- Minimum removals

---

## Template C — Start + Heap of Ends

```python
import heapq

intervals.sort(key=lambda x: x[0])

heap = []

for start, end in intervals:

    while heap and heap[0] <= start:
        heapq.heappop(heap)

    heapq.heappush(heap, end)
```

Use when tracking currently active intervals.

---

## Template D — Available Jobs / Events

```python
items.sort(key=lambda x: x[0])

heap = []
i = 0

while i < len(items) or heap:

    while i < len(items) and items[i][0] <= current_time:
        heapq.heappush(heap, priority(items[i]))
        i += 1

    remove_expired_items()

    if heap:
        process(heapq.heappop(heap))
```

Use when choices become available over time.

Examples:
- LC 1353
- CPU scheduling variants
- Task scheduling variants

---

# 13. Sweep Line Pattern

Another major interval technique is to turn each interval into events.

For:

```text
[start, end]
```

create:

```text
(start, +1)
(end, -1)
```

Then sort events.

### Example

```python
events = []

for start, end in intervals:
    events.append((start, +1))
    events.append((end, -1))

events.sort()
```

Maintain:

```python
active += delta
```

Maximum `active` = maximum simultaneous overlap.

Useful for:
- Meeting Rooms II
- Calendar overlap problems
- Range overlap/counting
- Skyline-style problems

---

# 14. Important LeetCode Roadmap

## Level 1 — Basic Interval Manipulation

1. **LC 56 — Merge Intervals**
2. **LC 57 — Insert Interval**
3. **LC 252 — Meeting Rooms**
4. **LC 986 — Interval List Intersections**

Goal:

```text
Understand interval overlap conditions.
```

---

## Level 2 — Greedy Scheduling

5. **LC 435 — Non-overlapping Intervals**
6. **LC 452 — Minimum Number of Arrows to Burst Balloons**
7. **LC 1288 — Remove Covered Intervals**

Goal:

```text
Recognize when sorting by END gives the greedy optimum.
```

---

## Level 3 — Heap Scheduling

8. **LC 253 — Meeting Rooms II**
9. **LC 1353 — Maximum Number of Events That Can Be Attended**
10. **LC 759 — Employee Free Time**

Goal:

```text
Understand:
start-sort + active intervals + min-heap
```

---

## Level 4 — Sweep Line

11. **LC 732 — My Calendar III**
12. **LC 218 — The Skyline Problem**
13. **LC 1094 — Car Pooling**
14. **LC 1109 — Corporate Flight Bookings**

Goal:

```text
Convert intervals into events / difference arrays.
```

---

## Level 5 — Harder Scheduling

15. **LC 630 — Course Schedule III**
16. **LC 1235 — Maximum Profit in Job Scheduling**
17. **LC 2008 — Maximum Earnings From Taxi**
18. **LC 2054 — Two Best Non-Overlapping Events**

These combine intervals with:
- Heap
- DP
- Binary search
- Greedy

---

# 15. Fast Interview Heuristic

When you see an interval problem, ask these in order:

### Q1. Am I simply checking/combining overlap?

```text
YES
→ Sort by START
```

---

### Q2. Am I selecting the largest possible set of non-overlapping intervals?

```text
YES
→ Sort by END
```

---

### Q3. Can several intervals be active at the same time?

```text
YES
→ Sort by START
→ Heap of END times
```

---

### Q4. Do available choices change as time advances?

```text
YES
→ Sort by START
→ Heap of best currently available choice
```

---

### Q5. Do I only need counts at timestamps?

```text
YES
→ Sweep Line / Difference Array
```

---

# 16. One-Line Memory Trick

```text
START  = process intervals in time order
END    = choose intervals greedily
HEAP   = manage intervals currently alive
SWEEP  = count what changes at each boundary
```

Or even shorter:

```text
MERGE  → START
CHOOSE → END
ACTIVE → START + HEAP
COUNT  → SWEEP LINE
```

---

# 17. Most Important Problems to Practice

If you only have time for a small representative set:

1. **LC 56 — Merge Intervals**
2. **LC 57 — Insert Interval**
3. **LC 252 — Meeting Rooms**
4. **LC 253 — Meeting Rooms II**
5. **LC 435 — Non-overlapping Intervals**
6. **LC 452 — Minimum Arrows to Burst Balloons**
7. **LC 1353 — Maximum Number of Events That Can Be Attended**
8. **LC 986 — Interval List Intersections**
9. **LC 1094 — Car Pooling**
10. **LC 1235 — Maximum Profit in Job Scheduling**

If these are clear, most interval questions become recognizable variations of the same few patterns.
