# LC 1353 --- Maximum Number of Events That Can Be Attended

## Why Doesn't a Simple End-Time Sort Work?

A common first thought for **LC 1353 --- Maximum Number of Events That
Can Be Attended** is:

> "If I can attend only one event at a time, why not sort by end time
> and greedily pick the earliest-ending event?"

That works for classic **Activity Selection / Non-overlapping
Intervals**, but LC 1353 has an important difference:

> An event `[start, end]` only consumes **one day anywhere inside its
> range**.

It does **not** occupy the entire interval.

------------------------------------------------------------------------

# 1. Classic Activity Selection

Suppose an interval is:

``` text
[1, 3]
```

If you choose it, you are occupied for the whole interval:

``` text
Day:     1   2   3
         █████████
```

So for:

``` text
[1,3]
[2,5]
[4,6]
```

choosing `[1,3]` means you cannot choose `[2,5]`.

The standard greedy strategy is:

``` python
intervals.sort(key=lambda x: x[1])
```

Then repeatedly choose the interval that finishes earliest.

### Why?

Finishing as early as possible leaves maximum room for future intervals.

This pattern appears in problems such as:

-   LC 435 --- Non-overlapping Intervals
-   Activity Selection
-   LC 452 --- Minimum Number of Arrows to Burst Balloons (closely
    related greedy reasoning)

------------------------------------------------------------------------

# 2. LC 1353 Is Different

For LC 1353, an event:

``` text
[start, end]
```

means:

> You may attend this event on **any one day** from `start` through
> `end`.

For example:

``` text
[1,5]
[1,5]
[1,5]
[1,5]
[1,5]
```

All five events can be attended:

``` text
Day 1 -> Event 1
Day 2 -> Event 2
Day 3 -> Event 3
Day 4 -> Event 4
Day 5 -> Event 5
```

So the answer is:

``` text
5
```

The interval `[1,5]` does **not** mean that attending the event occupies
days 1 through 5.

It means that we need to assign **one available day** inside `[1,5]`.

------------------------------------------------------------------------

# 3. Why End-Time Sorting Alone Is Not the Right Model

Consider:

``` text
[1,2]
[1,2]
[2,3]
```

Sorting by end gives:

``` text
[1,2]
[1,2]
[2,3]
```

But after sorting, we still have another decision:

> **Which day should each event use?**

For example:

``` text
Event [1,2] -> Day 1
Event [1,2] -> Day 2
Event [2,3] -> Day 3
```

All three can be attended.

The problem is therefore not simply:

``` text
Which interval should I select?
```

It is:

``` text
Which event should I assign to each day?
```

------------------------------------------------------------------------

# 4. The Correct Greedy Perspective

Imagine processing time one day at a time.

Suppose on Day 3 these events are available:

``` text
[1,10]
[2,4]
[3,5]
```

Their deadlines are:

``` text
Event      End
----------------
[1,10]      10
[2,4]        4
[3,5]        5
```

Which event should we attend on Day 3?

Choose:

``` text
[2,4]
```

because it expires first.

If we postpone `[2,4]`, we might lose it after Day 4.

But `[1,10]` has plenty of flexibility.

Therefore the greedy rule is:

> Among all events that have already started and have not expired,
> attend the event with the **earliest end day**.

------------------------------------------------------------------------

# 5. Why We Need a Heap

The set of events available to us changes as time progresses.

For example:

### Day 1

Available:

``` text
[1,10]
```

### Day 2

Available:

``` text
[1,10]
[2,4]
```

### Day 3

Available:

``` text
[1,10]
[2,4]
[3,5]
```

Every day we need to answer:

> Among all currently available events, which event ends earliest?

That is exactly what a **min-heap** is good at.

The heap stores:

``` text
end times
```

so:

``` python
heap[0]
```

is always the active event with the earliest deadline.

------------------------------------------------------------------------

# 6. Why Sort by Start Time?

We sort events by start time so that as we move through days, we can
efficiently discover which events have become available.

``` python
events.sort(key=lambda x: x[0])
```

Then on each day:

1.  Add every event that has started.
2.  Remove events that already expired.
3.  Attend the active event with the earliest ending time.

This gives the pattern:

``` text
SORT BY START
      +
MIN-HEAP BY END
```

------------------------------------------------------------------------

# 7. LC 1353 Algorithm

``` python
import heapq

class Solution:
    def maxEvents(self, events):
        events.sort(key=lambda x: x[0])

        heap = []
        i = 0
        day = 0
        attended = 0
        n = len(events)

        while i < n or heap:

            # If nothing is available, jump directly
            # to the next event's start day.
            if not heap:
                day = events[i][0]

            # Add every event that has started.
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove events that have already expired.
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # Attend the event that expires earliest.
            if heap:
                heapq.heappop(heap)
                attended += 1
                day += 1

        return attended
```

------------------------------------------------------------------------

# 8. Complexity

Sorting:

``` text
O(n log n)
```

Every event enters the heap once and leaves the heap once:

``` text
O(n log n)
```

Overall:

``` text
Time:  O(n log n)
Space: O(n)
```

------------------------------------------------------------------------

# 9. LC 435 vs LC 1353

This distinction is extremely important.

## LC 435 --- Non-overlapping Intervals

Choosing an interval consumes the **whole interval**.

``` text
[1-------------5]
```

You are effectively choosing intervals.

Therefore:

``` text
Sort by END
```

and greedily keep the interval that finishes earliest.

------------------------------------------------------------------------

## LC 1353 --- Maximum Events Attended

Choosing an event consumes only **one day**.

``` text
Event availability:

[1-------------5]

Choose only:

       X

one day somewhere inside the interval
```

You are assigning events to days.

Therefore:

``` text
Sort by START
+
Heap by END
```

------------------------------------------------------------------------

# 10. The Most Useful Recognition Rule

When you see an interval problem, ask what the interval represents.

## Case A --- I am selecting whole intervals

Examples:

``` text
Choose maximum number of non-overlapping intervals.
Remove minimum number of overlapping intervals.
```

Think:

``` text
SORT BY END
```

Typical problems:

-   LC 435 --- Non-overlapping Intervals
-   Activity Selection
-   LC 452 --- Minimum Number of Arrows to Burst Balloons

------------------------------------------------------------------------

## Case B --- I am processing intervals chronologically

Examples:

``` text
Merge overlapping intervals.
Check whether meetings overlap.
```

Think:

``` text
SORT BY START
```

Typical problems:

-   LC 56 --- Merge Intervals
-   LC 57 --- Insert Interval
-   LC 252 --- Meeting Rooms

------------------------------------------------------------------------

## Case C --- I repeatedly choose among currently active intervals

Examples:

``` text
Which event expires first?
Which meeting room becomes free first?
Which active task has the earliest deadline?
```

Think:

``` text
SORT BY START
+
HEAP
```

Typical problems:

-   LC 1353 --- Maximum Number of Events That Can Be Attended
-   LC 253 --- Meeting Rooms II
-   LC 2402 --- Meeting Rooms III

------------------------------------------------------------------------

# 11. Mental Shortcut

Memorize this:

``` text
┌──────────────────────────────────────────────┐
│ Am I choosing WHOLE intervals?               │
│                                              │
│        YES -> Sort by END                    │
│                                              │
│ Am I processing intervals chronologically?  │
│                                              │
│        YES -> Sort by START                  │
│                                              │
│ Do active candidates change over time, and  │
│ must I repeatedly choose the best one?       │
│                                              │
│        YES -> Sort by START + HEAP           │
└──────────────────────────────────────────────┘
```

An even shorter version:

``` text
MERGE / OVERLAP
    ↓
sort START


MAXIMUM NON-OVERLAPPING SELECTION
    ↓
sort END


DYNAMIC ACTIVE SET
    ↓
sort START
+
heap by END
```

------------------------------------------------------------------------

# 12. Why LC 1353 Needs the Heap --- One Sentence

> **LC 435 chooses an interval once; LC 1353 chooses an event every day
> from a changing set of currently available events.**

That changing active set is the reason the heap appears.

------------------------------------------------------------------------

# 13. General Scheduling Template

Whenever you see:

> "At each time/day, choose one currently available item, preferably the
> one with the earliest deadline."

consider this template:

``` python
items.sort(key=lambda x: x[0])

heap = []
i = 0

while items_remaining or heap:

    # Add newly available items
    while i < len(items) and items[i][0] <= current_time:
        heapq.heappush(heap, items[i][1])
        i += 1

    # Remove expired items
    while heap and heap[0] < current_time:
        heapq.heappop(heap)

    # Greedily choose earliest deadline
    if heap:
        deadline = heapq.heappop(heap)
        process(deadline)

    current_time += 1
```

The conceptual pattern is:

``` text
Sort by availability time
        ↓
Add available candidates
        ↓
Heap orders candidates by urgency
        ↓
Choose most urgent candidate
        ↓
Advance time
```

------------------------------------------------------------------------

# Final Cheat Sheet

  -----------------------------------------------------------------------
  Problem                 What are we doing?      Strategy
  ----------------------- ----------------------- -----------------------
  LC 56 Merge Intervals   Merge chronological     Sort by start
                          overlaps                

  LC 57 Insert Interval   Merge around inserted   Start-order traversal
                          interval                

  LC 252 Meeting Rooms    Detect chronological    Sort by start
                          overlap                 

  LC 435 Non-overlapping  Select whole intervals  Sort by end
  Intervals                                       

  LC 452 Minimum Arrows   Greedily cover          Sort by end
                          intervals               

  LC 253 Meeting Rooms II Track changing active   Sort by start +
                          meetings                min-heap of ends

  LC 1353 Maximum Events  Assign one active event Sort by start +
                          to each day             min-heap of ends

  LC 2402 Meeting Rooms   Dynamically assign      Sort + heaps
  III                     available rooms         
  -----------------------------------------------------------------------

## Core Rule

``` text
WHOLE INTERVAL SELECTION
        -> END

CHRONOLOGICAL OVERLAP / MERGING
        -> START

CHANGING ACTIVE SET
        -> START + HEAP
```
