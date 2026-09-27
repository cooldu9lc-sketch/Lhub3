# Monotonic Stacks and Queues — LeetCode Roadmap

A **monotonic stack/queue** is a data structure that keeps **only the candidates that can still matter**, maintained in sorted order.

The central idea is:

> If a new element makes older **smaller** elements irrelevant, maintain a **decreasing** structure.
>
> If a new element makes older **larger** elements irrelevant, maintain an **increasing** structure.

---

# 1\. How to Choose Increasing vs Decreasing

Think about **what answer you are trying to find**.

| Task | Monotonic Structure |
| --- | --- |
| Next Greater Element | **Decreasing Stack** |
| Previous Greater Element | **Decreasing Stack** |
| Next Smaller Element | **Increasing Stack** |
| Previous Smaller Element | **Increasing Stack** |
| Sliding Window Maximum | **Decreasing Deque** |
| Sliding Window Minimum | **Increasing Deque** |

## Why?

Suppose you want the **Next Greater Element**.

If a new number `x` arrives, then any earlier number smaller than `x` may have just found its answer.

For example:

```
nums = [5, 3, 2, 7]
```

Before `7` arrives:

```
Stack:

5
3
2
```

When `7` arrives:

```
7 > 2  → pop 2
7 > 3  → pop 3
7 > 5  → pop 5
```

Therefore:

```
NGE(2) = 7
NGE(3) = 7
NGE(5) = 7
```

The stack naturally maintains elements in **decreasing order**.

```
Bottom        Top
  ↓            ↓

[ 9, 7, 5, 3, 2 ]

Decreasing Stack
```

For **Next Smaller Element**, flip the logic.

You remove larger elements and maintain an **increasing stack**.

```
[ 1, 3, 5, 8, 10 ]

Increasing Stack
```

---

# 2\. The Fast Mental Shortcut

Instead of asking:

> "Should my stack be increasing or decreasing?"

Ask:

> **"Which elements does the current element make useless?"**

### If the current element makes SMALLER elements useless

Pop smaller elements.

```
while stack and stack[-1] < current:
    stack.pop()
```

The remaining stack is:

```
DECREASING
```

Typical applications:

```
Next Greater Element
Previous Greater Element
Sliding Window Maximum
Daily Temperatures
```

---

### If the current element makes LARGER elements useless

Pop larger elements.

```
while stack and stack[-1] > current:
    stack.pop()
```

The remaining stack is:

```
INCREASING
```

Typical applications:

```
Next Smaller Element
Previous Smaller Element
Sliding Window Minimum
Largest Rectangle in Histogram
```

---

# 3\. Strict vs Non-Strict Monotonicity

Another common source of confusion is deciding between:

```
<
```

and

```
<=
```

or between:

```
>
```

and

```
>=
```

The easiest question is:

> **Should equal values count as a valid answer?**

---

## Strictly Greater

If you want:

```
next value > current
```

then equal values are **not sufficient**.

Depending on the implementation, equal values may need to be removed.

For example:

```
while stack and nums[stack[-1]] <= nums[i]:
    stack.pop()
```

This maintains a **strictly decreasing stack**.

---

## Greater or Equal

If you want:

```
next value >= current
```

then equal values are useful.

You usually only remove strictly smaller values:

```
while stack and nums[stack[-1]] < nums[i]:
    stack.pop()
```

---

## Strictly Smaller

For:

```
next value < current
```

you often use:

```
while stack and nums[stack[-1]] >= nums[i]:
    stack.pop()
```

This maintains a **strictly increasing stack**.

---

## Smaller or Equal

For:

```
next value <= current
```

you can keep equal values:

```
while stack and nums[stack[-1]] > nums[i]:
    stack.pop()
```

---

# 4\. Important Duplicate Rule

Problems involving **counting subarrays** require special care.

Examples:

-   LC 907 — Sum of Subarray Minimums

-   LC 2104 — Sum of Subarray Ranges

You often intentionally make:

```
one boundary STRICT
other boundary NON-STRICT
```

For example:

```
Previous Less       → strictly less
Next Less           → less or equal
```

This prevents duplicate elements from causing the same subarray to be counted multiple times.

---

# 5\. Monotonic Stack / Queue Roadmap

## Pattern A — Next / Previous Greater or Smaller

These are the fundamental monotonic-stack problems.

Learn these first.

### Problems

-   LC 496 — Next Greater Element I

-   LC 503 — Next Greater Element II

-   LC 739 — Daily Temperatures

-   LC 901 — Online Stock Span

-   LC 1475 — Final Prices With a Special Discount

These teach:

```
Next Greater
Previous Greater
Next Smaller
Previous Smaller
Circular arrays
Distance to next greater
```

---

# Pattern B — Subarray Boundaries

These problems use monotonic stacks to determine:

```
How far left can this element extend?

How far right can this element extend?
```

Important problems:

-   LC 84 — Largest Rectangle in Histogram

-   LC 85 — Maximal Rectangle

-   LC 907 — Sum of Subarray Minimums

-   LC 2104 — Sum of Subarray Ranges

These problems are extremely important because they generalize the monotonic-stack idea.

---

# Pattern C — Sliding Window Maximum / Minimum

These use a **monotonic deque** instead of a stack.

Important problems:

-   LC 239 — Sliding Window Maximum

-   LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

-   LC 862 — Shortest Subarray With Sum at Least K

The fundamental idea is:

```
Deque front = current best candidate
Deque back  = candidates that may become useful later
```

---

# Pattern D — Remove Dominated Elements

Sometimes the problem does not explicitly ask for:

```
next greater
next smaller
```

but the same idea appears.

A new element may make previous elements permanently useless.

Important problems:

-   LC 402 — Remove K Digits

-   LC 316 — Remove Duplicate Letters

-   LC 1673 — Find the Most Competitive Subsequence

These are essentially **greedy + monotonic stack** problems.

---

# 6\. Core Monotonic Stack Template

Use a stack of **indices** whenever position matters.

```
stack = []

for i, x in enumerate(nums):

    while stack and nums[stack[-1]] <= x:
        stack.pop()

    stack.append(i)
```

This maintains a:

```
DECREASING STACK
```

Swap:

```
<=
```

with:

```
>=
```

to maintain an:

```
INCREASING STACK
```

---

# 7\. Core Monotonic Queue Template

For sliding-window problems, use a deque.

```
from collections import deque

dq = deque()

for i, x in enumerate(nums):

    # Remove dominated elements
    while dq and nums[dq[-1]] <= x:
        dq.pop()

    dq.append(i)

    # Remove elements outside the window
    while dq and dq[0] <= i - k:
        dq.popleft()

    # Maximum of current window
    maximum = nums[dq[0]]
```

The deque contains indices whose values are:

```
DECREASING
```

Therefore:

```
nums[dq[0]]
```

is always the maximum.

---

# 8\. LC 496 — Next Greater Element I

## Problem Pattern

For each number, find the first larger number appearing to its right.

This is the classic:

```
NEXT GREATER ELEMENT
```

pattern.

Therefore:

```
Use a DECREASING stack.
```

---

## Solution

```
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}

        stack = []

        for x in nums2:

            while stack and stack[-1] < x:
                smaller = stack.pop()
                next_greater[smaller] = x

            stack.append(x)

        return [
            next_greater.get(x, -1)
            for x in nums1
        ]
```

---

## Example

```
nums2 = [2, 1, 5]
```

Process `2`:

```
stack = [2]
```

Process `1`:

```
1 < 2

stack = [2, 1]
```

Process `5`:

```
5 > 1

pop 1

NGE(1) = 5
```

Then:

```
5 > 2

pop 2

NGE(2) = 5
```

Finally:

```
stack = [5]
```

---

## Complexity

Each element enters the stack once and leaves at most once.

```
Time:  O(n)
Space: O(n)
```

---

# 9\. LC 739 — Daily Temperatures

For each day, determine how many days until a warmer temperature.

This is essentially:

```
Next Greater Element
+
Index Distance
```

Therefore use a:

```
DECREASING stack
```

of indices.

---

## Solution

```
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)

        ans = [0] * n

        stack = []

        for i, temperature in enumerate(temperatures):

            while (
                stack
                and temperatures[stack[-1]] < temperature
            ):
                j = stack.pop()

                ans[j] = i - j

            stack.append(i)

        return ans
```

---

## Why Store Indices?

Because the answer is:

```
distance = current_index - previous_index
```

For example:

```
temperatures = [73, 74]
```

When `74` arrives:

```
i = 1
j = 0

answer = 1 - 0 = 1
```

---

## Complexity

```
Time:  O(n)
Space: O(n)
```

---

# 10\. LC 239 — Sliding Window Maximum

Given:

```
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

find the maximum inside every window.

Brute force would cost:

```
O(n * k)
```

Instead, maintain a:

```
DECREASING DEQUE
```

---

## Why Decreasing?

Suppose the deque represents:

```
[9, 7, 4, 2]
```

Then:

```
front = 9
```

is automatically the maximum.

Now suppose `8` arrives.

```
[9, 7, 4, 2]
          ↑
```

Values:

```
2
4
7
```

are useless.

Why?

Because `8` is:

```
larger
AND
newer
```

Therefore `8` will remain in the window longer.

So remove them:

```
[9, 8]
```

---

## Solution

```
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()

        ans = []

        for i, x in enumerate(nums):

            # Remove smaller elements
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            dq.append(i)

            # Remove expired element
            if dq[0] <= i - k:
                dq.popleft()

            # Window is fully formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
```

---

## Complexity

Every index enters and leaves the deque at most once.

```
Time:  O(n)
Space: O(k)
```

---

# 11\. LC 84 — Largest Rectangle in Histogram

This is one of the most important monotonic-stack problems.

For every bar, imagine using that bar as the rectangle's height.

We want to determine:

```
How far LEFT can this height extend?

How far RIGHT can this height extend?
```

The rectangle stops when we encounter a:

```
SMALLER height
```

Therefore this is fundamentally a:

```
Previous Smaller
+
Next Smaller
```

problem.

That suggests an:

```
INCREASING STACK
```

---

## Core Idea

Suppose:

```
heights = [2, 3, 5, 6, 1]
```

Before `1`:

```
2
3
5
6
```

are increasing.

When `1` arrives:

```
1 < 6
```

so `6` cannot extend farther.

Pop it.

Then:

```
1 < 5
```

pop `5`.

Then:

```
1 < 3
```

pop `3`.

Each pop means:

> We just discovered the right boundary of that rectangle.

---

## Solution

```
class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)

        stack = []

        ans = 0

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:

                height = heights[stack.pop()]

                left = stack[-1] if stack else -1

                width = i - left - 1

                ans = max(
                    ans,
                    height * width
                )

            stack.append(i)

        heights.pop()

        return ans
```

---

## Why Add `0`?

```
heights.append(0)
```

acts as a sentinel.

Because `0` is smaller than every valid histogram height, it forces all remaining bars to be popped.

Without it, we would need a second cleanup loop.

---

## Width Formula

After popping index `j`:

```
right boundary = i
left boundary  = stack[-1]
```

Neither boundary can be included.

Therefore:

```
width = right - left - 1
```

or:

```
width = i - stack[-1] - 1
```

If the stack is empty:

```
left = -1
```

---

## Complexity

```
Time:  O(n)
Space: O(n)
```

---

# 12\. LC 907 — Sum of Subarray Minimums

This is one of the best problems for learning **duplicate handling**.

Instead of enumerating every subarray, ask:

> How many subarrays have `arr[i]` as their minimum?

Suppose:

```
arr[i] = x
```

and `x` can extend:

```
L positions left
R positions right
```

Then the number of subarrays where `x` is the chosen minimum is:

```
L × R
```

Therefore contribution:

```
x × L × R
```

---

## Boundary Problem

We need:

```
Previous Less
Next Less
```

But duplicates create a problem.

Suppose:

```
[2, 2]
```

Both `2`s could claim the same subarray.

Therefore we deliberately break symmetry.

One common convention:

```
Left  → Previous Less or Equal
Right → Next Strictly Less
```

or equivalently the reverse convention:

```
Left  → Previous Strictly Less
Right → Next Less or Equal
```

Either works if used consistently.

---

## Solution

```
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7

        n = len(arr)

        left = [0] * n
        right = [0] * n

        # Previous less or equal
        stack = []

        for i, x in enumerate(arr):

            count = 1

            while stack and stack[-1][0] > x:
                count += stack.pop()[1]

            left[i] = count

            stack.append((x, count))

        # Next strictly less
        stack = []

        for i in range(n - 1, -1, -1):

            x = arr[i]

            count = 1

            while stack and stack[-1][0] >= x:
                count += stack.pop()[1]

            right[i] = count

            stack.append((x, count))

        ans = 0

        for i, x in enumerate(arr):

            contribution = (
                x
                * left[i]
                * right[i]
            )

            ans = (
                ans + contribution
            ) % MOD

        return ans
```

---

## Complexity

```
Time:  O(n)
Space: O(n)
```

---

# 13\. The Interview Decision Process

Whenever you encounter a possible monotonic-stack problem, use these questions.

## Question 1 — What am I looking for?

Is the problem asking for:

```
Next Greater?
Previous Greater?

Next Smaller?
Previous Smaller?

Window Maximum?
Window Minimum?

Boundary until smaller?
Boundary until larger?
```

If yes, monotonic structures should immediately come to mind.

---

## Question 2 — What does the current element destroy?

This is the easiest way to determine direction.

### Current element destroys SMALLER elements

```
while stack and stack[-1] < current:
    stack.pop()
```

Result:

```
DECREASING STACK
```

Used for:

```
Next Greater
Previous Greater
Sliding Window Maximum
```

---

### Current element destroys LARGER elements

```
while stack and stack[-1] > current:
    stack.pop()
```

Result:

```
INCREASING STACK
```

Used for:

```
Next Smaller
Previous Smaller
Sliding Window Minimum
Histogram boundaries
```

---

# 14\. The Most Useful Cheat Sheet

```
WHAT DO I WANT?
        |
        |
        +-----------------------+
        |                       |
      GREATER                 SMALLER
        |                       |
        v                       v
   DECREASING              INCREASING
      STACK                   STACK
```

Another way to remember it:

```
Want MAX / GREATER
        ↓
Kill smaller values
        ↓
Keep decreasing order

Want MIN / SMALLER
        ↓
Kill larger values
        ↓
Keep increasing order
```

---

# 15\. Stack vs Queue

Use a **monotonic stack** when you're primarily interested in:

```
nearest greater/smaller element
boundaries
previous/next relationships
```

Examples:

```
Daily Temperatures
Largest Rectangle
Next Greater Element
Sum of Subarray Minimums
```

Use a **monotonic deque** when you're dealing with a:

```
moving / sliding window
```

because you need to remove elements from **both ends**.

Examples:

```
Sliding Window Maximum
Sliding Window Minimum
Longest Subarray Within Limit
```

---

# 16\. Why Monotonic Structures Are O(n)

A `while` loop inside a `for` loop might initially look like:

```
O(n²)
```

But consider each element individually.

An element can be:

```
pushed once
popped once
```

Therefore across the entire algorithm:

```
Total pushes <= n
Total pops   <= n
```

So:

```
Time = O(n)
```

This is called **amortized analysis**.

---

# 17\. Recommended Practice Roadmap

## Stage 1 — Learn Basic Next Greater / Smaller

Start with:

```
LC 496  Next Greater Element I
LC 739  Daily Temperatures
LC 1475 Final Prices With a Special Discount
```

Goal:

```
Understand when elements get popped.
```

---

## Stage 2 — Variations

Then:

```
LC 503  Next Greater Element II
LC 901  Online Stock Span
```

Learn:

```
Circular arrays
Previous greater
Aggregating spans
```

---

## Stage 3 — Boundary Problems

Next:

```
LC 84   Largest Rectangle in Histogram
LC 85   Maximal Rectangle
```

Learn:

```
Previous smaller
Next smaller
Boundary calculations
```

---

## Stage 4 — Contribution Problems

Then:

```
LC 907   Sum of Subarray Minimums
LC 2104  Sum of Subarray Ranges
```

Learn:

```
Contribution technique

value × left_choices × right_choices
```

This is one of the most powerful monotonic-stack patterns.

---

## Stage 5 — Monotonic Queue

Then:

```
LC 239   Sliding Window Maximum
LC 1438  Longest Continuous Subarray
LC 862   Shortest Subarray With Sum at Least K
```

Learn:

```
Deque
Window expiration
Dominated candidates
```

---

## Stage 6 — Greedy Monotonic Stack

Finally:

```
LC 402   Remove K Digits
LC 316   Remove Duplicate Letters
LC 1673  Most Competitive Subsequence
```

These teach you to recognize monotonic-stack behavior even when the problem never explicitly mentions:

```
next greater
next smaller
```

---

# 18\. Good-Enough Interview Practice List

If you do not want to solve every problem in the roadmap, prioritize these:

| Priority | Problem | Main Pattern |
| --- | --- | --- |
| ⭐⭐⭐ | LC 496 — Next Greater Element I | Basic next greater |
| ⭐⭐⭐ | LC 739 — Daily Temperatures | Next greater + distance |
| ⭐⭐⭐ | LC 239 — Sliding Window Maximum | Monotonic deque |
| ⭐⭐⭐ | LC 84 — Largest Rectangle in Histogram | Boundary stack |
| ⭐⭐⭐ | LC 907 — Sum of Subarray Minimums | Contribution + boundaries |
| ⭐⭐ | LC 503 — Next Greater Element II | Circular stack |
| ⭐⭐ | LC 901 — Online Stock Span | Previous greater |
| ⭐⭐ | LC 402 — Remove K Digits | Greedy monotonic stack |
| ⭐⭐ | LC 2104 — Sum of Subarray Ranges | Min/max contribution |
| ⭐ | LC 1438 — Longest Continuous Subarray | Two monotonic deques |

---

# Final Cheat Sheet

```
==================================================
            MONOTONIC STACK DECISION
==================================================

Want NEXT/PREVIOUS GREATER?
        ↓
Maintain DECREASING stack

Want NEXT/PREVIOUS SMALLER?
        ↓
Maintain INCREASING stack

Want WINDOW MAXIMUM?
        ↓
Maintain DECREASING deque

Want WINDOW MINIMUM?
        ↓
Maintain INCREASING deque

Current value makes SMALLER values useless?
        ↓
POP SMALLER
        ↓
DECREASING structure

Current value makes LARGER values useless?
        ↓
POP LARGER
        ↓
INCREASING structure

Need positions/distances?
        ↓
Store INDICES

Need sliding window?
        ↓
Use DEQUE

Duplicates matter?
        ↓
Think carefully about < vs <=
        ↓
For contribution problems:
one boundary STRICT
other boundary NON-STRICT
==================================================
```

## The One Rule to Remember

If you forget everything else, remember:

> **Don't try to memorize whether the stack should be increasing or decreasing. Ask which elements the new value makes permanently useless.**

If it makes **smaller elements useless**, pop smaller elements and the structure becomes **decreasing**.

If it makes **larger elements useless**, pop larger elements and the structure becomes **increasing**.

That single idea covers most monotonic-stack and monotonic-queue problems.