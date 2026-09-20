# Dynamic Programming Patterns — Python Templates & Examples

A practical LeetCode reference for recognizing common DP patterns, choosing the right state, and recalling reusable Python templates.

---

## 1. Linear / 1D DP

### Recognition

Use 1D DP when the answer at position `i` depends on a small number of earlier positions.

Typical state:

```python
dp[i] = best/count/feasibility answer considering positions up to i
```

### Generic Template

```python
def solve(nums):
    n = len(nums)
    dp = [0] * n

    # Base cases
    dp[0] = ...

    for i in range(1, n):
        dp[i] = ...

    return dp[-1]
```

### Example — LC 198: House Robber

Transition:

```text
dp[i] = max(
    dp[i - 1],             # skip house i
    nums[i] + dp[i - 2]    # rob house i
)
```

Space-optimized solution:

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            cur = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = cur

        return prev1
```

**Time:** `O(n)`  
**Space:** `O(1)`

Representative problems:

- LC 70 — Climbing Stairs
- LC 746 — Min Cost Climbing Stairs
- LC 198 — House Robber
- LC 91 — Decode Ways
- LC 139 — Word Break

---

## 2. Grid DP

### Recognition

Use Grid DP when the state corresponds to a cell:

```python
dp[r][c]
```

and transitions come from neighboring cells.

### Generic 2D Template

```python
def solve(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for _ in range(rows)]

    # Initialize first row / column

    for r in range(rows):
        for c in range(cols):
            dp[r][c] = ...

    return dp[-1][-1]
```

### Space-Optimized Template

If a row only depends on the current and previous row:

```python
dp = [0] * cols

for r in range(rows):
    for c in range(cols):
        dp[c] = ...
```

### Example — LC 62: Unique Paths

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]

        return dp[-1]
```

Here:

```text
dp[c]     = value from above
dp[c - 1] = value from left
```

**Time:** `O(m * n)`  
**Space:** `O(n)`

Representative problems:

- LC 62 — Unique Paths
- LC 63 — Unique Paths II
- LC 64 — Minimum Path Sum
- LC 120 — Triangle
- LC 174 — Dungeon Game

---

## 3. Knapsack DP

Knapsack problems usually involve:

- choosing items
- target sums
- capacity
- counting combinations
- determining feasibility

The two major variants are **0/1 Knapsack** and **Unbounded Knapsack**.

---

### 3A. 0/1 Knapsack

Each item can be used **at most once**.

### Generic 2D State

```python
dp[i][capacity]
```

means:

```text
answer using the first i items with the given capacity
```

### 1D Template

```python
dp = [False] * (target + 1)
dp[0] = True

for num in nums:
    for s in range(target, num - 1, -1):
        dp[s] = dp[s] or dp[s - num]
```

### Critical Rule

Iterate capacity **backward**:

```python
for s in range(target, num - 1, -1):
```

because each item can only be used once.

### Example — LC 416: Partition Equal Subset Sum

```python
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
```

**Time:** `O(n * target)`  
**Space:** `O(target)`

Representative problems:

- LC 416 — Partition Equal Subset Sum
- LC 494 — Target Sum
- LC 1049 — Last Stone Weight II
- LC 474 — Ones and Zeroes

---

### 3B. Unbounded Knapsack

Each item can be reused an unlimited number of times.

### Template

```python
dp = [0] * (target + 1)
dp[0] = ...

for item in items:
    for s in range(item, target + 1):
        dp[s] = ...
```

### Critical Rule

Iterate capacity **forward**:

```python
for s in range(item, target + 1):
```

This allows the current item to be reused.

### Example — LC 518: Coin Change II

```python
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amount_now in range(coin, amount + 1):
                dp[amount_now] += dp[amount_now - coin]

        return dp[amount]
```

**Time:** `O(len(coins) * amount)`  
**Space:** `O(amount)`

Representative problems:

- LC 322 — Coin Change
- LC 518 — Coin Change II
- LC 279 — Perfect Squares

---

## 4. Two-Sequence / Subsequence DP

### Recognition

Common when comparing:

- two strings
- two arrays
- prefixes of two sequences

Typical state:

```python
dp[i][j]
```

means:

```text
answer involving the first i elements of A
and first j elements of B
```

### Generic Template

```python
m = len(a)
n = len(b)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if a[i - 1] == b[j - 1]:
            dp[i][j] = ...
        else:
            dp[i][j] = ...

return dp[m][n]
```

### Example — LC 1143: Longest Common Subsequence

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[m][n]
```

**Time:** `O(m * n)`  
**Space:** `O(m * n)`

Representative problems:

- LC 1143 — Longest Common Subsequence
- LC 72 — Edit Distance
- LC 115 — Distinct Subsequences
- LC 583 — Delete Operation for Two Strings
- LC 712 — Minimum ASCII Delete Sum

---

## 5. LIS / Single-Sequence Subsequence DP

### Recognition

Look for:

- longest increasing/decreasing subsequence
- chain relationships
- one element extending another valid subsequence

Typical state:

```python
dp[i] = length/value of the best subsequence ending exactly at i
```

### Generic `O(n²)` Template

```python
dp = [1] * len(nums)

for i in range(len(nums)):
    for j in range(i):

        if nums[j] < nums[i]:
            dp[i] = max(
                dp[i],
                dp[j] + 1
            )

return max(dp)
```

### Example — LC 300: Longest Increasing Subsequence

```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):

                if nums[j] < nums[i]:
                    dp[i] = max(
                        dp[i],
                        dp[j] + 1
                    )

        return max(dp)
```

**Time:** `O(n²)`  
**Space:** `O(n)`

Representative problems:

- LC 300 — Longest Increasing Subsequence
- LC 673 — Number of Longest Increasing Subsequence
- LC 354 — Russian Doll Envelopes
- LC 368 — Largest Divisible Subset

---

## 6. Interval DP

### Recognition

Use Interval DP when the answer is naturally defined over:

```text
[l ... r]
```

Typical state:

```python
dp[l][r]
```

means:

```text
optimal answer for interval [l, r]
```

### Upper-Triangle Template

```python
n = len(nums)
dp = [[0] * n for _ in range(n)]

# Base cases
for l in range(n):
    dp[l][l] = ...

# Fill upper triangle by increasing right endpoint.
# l runs bottom -> top so dp[l + 1][...] already exists.
for l in range(n - 1, -1, -1):
    for r in range(l + 1, n):

        dp[l][r] = ...

return dp[0][n - 1]
```

For split-point problems:

```python
for l in range(n - 1, -1, -1):
    for r in range(l + 2, n):

        for k in range(l + 1, r):
            dp[l][r] = combine(
                dp[l][k],
                dp[k][r],
                ...
            )
```

### Example — LC 516: Longest Palindromic Subsequence

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            dp[l][l] = 1

            for r in range(l + 1, n):

                if s[l] == s[r]:
                    dp[l][r] = 2 + (
                        dp[l + 1][r - 1]
                        if l + 1 <= r - 1
                        else 0
                    )

                else:
                    dp[l][r] = max(
                        dp[l + 1][r],
                        dp[l][r - 1]
                    )

        return dp[0][n - 1]
```

**Time:** `O(n²)`  
**Space:** `O(n²)`

### Important Interval-DP Families

```text
INTERVAL DP
│
├── Split Point DP
│   ├── LC 1547 Minimum Cost to Cut a Stick
│   ├── LC 1000 Minimum Cost to Merge Stones
│   └── LC 1039 Minimum Score Triangulation
│
├── Last Operation DP
│   ├── LC 312 Burst Balloons
│   ├── LC 664 Strange Printer
│   └── LC 546 Remove Boxes
│
├── Game Interval DP
│   ├── LC 486 Predict the Winner
│   ├── LC 877 Stone Game
│   └── LC 1690 Stone Game VII
│
└── Palindrome Interval DP
    ├── LC 516 Longest Palindromic Subsequence
    ├── LC 131 Palindrome Partitioning
    └── LC 132 Palindrome Partitioning II
```

---

## 7. String / Matching DP

String DP often overlaps with two-sequence DP and state-machine DP.

Representative problems:

- LC 10 — Regular Expression Matching
- LC 44 — Wildcard Matching
- LC 91 — Decode Ways
- LC 97 — Interleaving String

### Example — LC 91: Decode Ways

State:

```python
dp[i] = number of ways to decode s[i:]
```

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):

            if s[i] == "0":
                continue

            dp[i] = dp[i + 1]

            if (
                i + 1 < n
                and 10 <= int(s[i:i + 2]) <= 26
            ):
                dp[i] += dp[i + 2]

        return dp[0]
```

**Time:** `O(n)`  
**Space:** `O(n)`

---

## 8. State Machine DP

### Recognition

Use State Machine DP when you can describe the problem as moving between a small number of logical states.

Examples:

```text
holding
not holding
cooldown
transaction count
matched/unmatched
```

### Generic Template

```python
state1 = ...
state2 = ...

for x in data:
    new_state1 = transition(...)
    new_state2 = transition(...)

    state1 = new_state1
    state2 = new_state2
```

### Example — LC 122: Best Time to Buy and Sell Stock II

States:

```text
hold = best profit while holding a stock
free = best profit while not holding a stock
```

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = float("-inf")
        free = 0

        for price in prices:
            prev_hold = hold
            prev_free = free

            hold = max(
                prev_hold,
                prev_free - price
            )

            free = max(
                prev_free,
                prev_hold + price
            )

        return free
```

**Time:** `O(n)`  
**Space:** `O(1)`

Representative problems:

- LC 121 — Best Time to Buy and Sell Stock
- LC 122 — Best Time to Buy and Sell Stock II
- LC 309 — Best Time to Buy and Sell Stock with Cooldown
- LC 714 — Best Time to Buy and Sell Stock with Transaction Fee
- LC 123 — Best Time to Buy and Sell Stock III
- LC 188 — Best Time to Buy and Sell Stock IV
- LC 276 — Paint Fence
- LC 790 — Domino and Tromino Tiling
- LC 10 — Regular Expression Matching
- LC 44 — Wildcard Matching

---

## 9. Tree DP

### Recognition

Use Tree DP when the state is naturally associated with each node and the answer for a node depends on its children.

A common pattern is returning multiple states:

```python
def dfs(node):
    return state_if_skipped, state_if_taken
```

### Generic Template

```python
def dfs(node):
    if not node:
        return ...

    left = dfs(node.left)
    right = dfs(node.right)

    state1 = ...
    state2 = ...

    return state1, state2
```

### Example — LC 337: House Robber III

```python
class Solution:
    def rob(self, root) -> int:

        def dfs(node):
            if not node:
                return 0, 0

            left_skip, left_rob = dfs(node.left)
            right_skip, right_rob = dfs(node.right)

            rob_node = (
                node.val
                + left_skip
                + right_skip
            )

            skip_node = (
                max(left_skip, left_rob)
                + max(right_skip, right_rob)
            )

            return skip_node, rob_node

        skip_root, rob_root = dfs(root)

        return max(skip_root, rob_root)
```

**Time:** `O(n)`  
**Space:** `O(h)` recursion stack

Representative problems:

- LC 337 — House Robber III
- LC 124 — Binary Tree Maximum Path Sum
- LC 968 — Binary Tree Cameras

---

## 10. Bitmask DP

### Recognition

Use Bitmask DP when:

- `n` is small
- state represents which elements have already been selected/visited
- order or subset matters

Typical state:

```python
dp[mask]
```

or:

```python
dp[mask][last]
```

### Generic Template

```python
n = len(items)

dp = [INF] * (1 << n)
dp[0] = 0

for mask in range(1 << n):

    for i in range(n):

        if mask & (1 << i):
            continue

        new_mask = mask | (1 << i)

        dp[new_mask] = min(
            dp[new_mask],
            dp[mask] + cost(...)
        )
```

Typical complexity:

```text
O(2^n * n)
```

or:

```text
O(2^n * n²)
```

Representative problems:

- LC 698 — Partition to K Equal Sum Subsets
- LC 847 — Shortest Path Visiting All Nodes
- LC 1125 — Smallest Sufficient Team
- LC 1434 — Number of Ways to Wear Different Hats

---

## 11. Digit DP

### Recognition

Typical question:

> How many integers from `0 ... N` satisfy some digit property?

Typical state:

```python
dfs(position, tight, started, ...)
```

where:

- `position` = current digit
- `tight` = whether current prefix must remain ≤ N's prefix
- `started` = whether the number has begun
- additional state = digit sum, count, mask, remainder, etc.

### Generic Template

```python
from functools import cache

def count(N: int) -> int:
    digits = str(N)

    @cache
    def dfs(pos, tight, started):
        if pos == len(digits):
            return int(started)

        limit = int(digits[pos]) if tight else 9

        ans = 0

        for digit in range(limit + 1):
            new_tight = tight and digit == limit
            new_started = started or digit != 0

            ans += dfs(
                pos + 1,
                new_tight,
                new_started
            )

        return ans

    return dfs(0, True, False)
```

Representative problems:

- LC 233 — Number of Digit One
- LC 902 — Numbers At Most N Given Digit Set
- LC 1012 — Numbers With Repeated Digits
- LC 2719 — Count of Integers

---

## 12. Meet in the Middle + DP / Subset Search

### Recognition

A major clue is:

```text
n ≈ 30–40
```

Too large for:

```text
O(2^n)
```

but small enough for:

```text
O(2^(n/2))
```

### Generic Idea

```python
mid = len(nums) // 2

left = nums[:mid]
right = nums[mid:]

left_sums = generate_subset_sums(left)
right_sums = generate_subset_sums(right)

# Combine/search the two halves
```

Representative problems:

- LC 805 — Split Array With Same Average
- LC 1755 — Closest Subsequence Sum
- LC 2035 — Partition Array Into Two Arrays to Minimize Sum Difference

---

## 13. Probability DP

### Recognition

State stores a probability or expected value.

```python
dp[state] = probability
```

or:

```python
dp[state] = expected value
```

Representative problems:

- LC 808 — Soup Servings
- LC 837 — New 21 Game
- LC 688 — Knight Probability in Chessboard

---

# DP Recognition Cheat Sheet

| Problem Clue | Likely DP Pattern | Typical State |
|---|---|---|
| Previous positions matter | Linear / 1D DP | `dp[i]` |
| Paths through matrix | Grid DP | `dp[r][c]` |
| Target sum / capacity / choose items | Knapsack | `dp[target]` |
| Item usable once | 0/1 Knapsack | backward capacity loop |
| Item reusable | Unbounded Knapsack | forward capacity loop |
| Compare two strings/sequences | Two-Sequence DP | `dp[i][j]` |
| Increasing/decreasing subsequence | LIS DP | `dp[i]` |
| Solve range `[l, r]` | Interval DP | `dp[l][r]` |
| Buy/sell / modes / finite states | State Machine DP | `dp[i][state]` |
| Tree decisions | Tree DP | `dp[node][state]` |
| Subsets and `n <= ~20` | Bitmask DP | `dp[mask]` |
| Count numbers `<= N` satisfying digit rules | Digit DP | `dp[pos][tight][...]` |
| Subset problem and `n ≈ 30–40` | Meet in the Middle | two sets of subset states |
| Probability / expected outcome | Probability DP | `dp[state]` |

---

# Loop-Direction Cheat Sheet

This is especially important for space-optimized DP.

## 0/1 Knapsack

Each item can be used once:

```python
for num in nums:
    for s in range(target, num - 1, -1):
        ...
```

**Go backward.**

Why?

Going backward prevents the current item from being reused during the same iteration.

---

## Unbounded Knapsack

Item can be reused:

```python
for num in nums:
    for s in range(num, target + 1):
        ...
```

**Go forward.**

Why?

Going forward allows:

```python
dp[s - num]
```

to already contain the current item.

---

## Two-Sequence DP

Normally:

```python
for i in range(1, m + 1):
    for j in range(1, n + 1):
        ...
```

Think:

```text
top
left
diagonal
```

---

## Interval DP

Think:

```text
Solve smaller intervals before larger intervals.
```

Preferred upper-triangle order:

```python
for l in range(n - 1, -1, -1):
    for r in range(l + 1, n):
        ...
```

---

# Top-Down DP Template

When the recurrence is easier to reason about recursively:

```python
from functools import cache

@cache
def dp(state):
    if base_case:
        return base_value

    answer = ...

    for choice in choices:
        answer = combine(
            answer,
            dp(next_state)
        )

    return answer
```

---

# Bottom-Up DP Template

Convert:

```python
dp(state)
```

into explicit storage:

```python
dp = [...]

# Base cases
...

# Iterate states in dependency order
for state in states:
    dp[state] = ...

return dp[target_state]
```

The key question is:

> What states must already be calculated before I calculate this state?

That determines the loop order.

---

# The Core DP Mental Model

For almost every DP problem, answer these questions in order:

### 1. What changes?

That determines the **state variables**.

Examples:

```text
index
remaining target
left/right
transaction state
mask
tree node
```

### 2. What does `dp[state]` mean?

Write the meaning in English **before coding**.

Example:

```python
dp[i] = maximum money obtainable from houses [0 ... i]
```

### 3. What choices do I have?

Usually something like:

```text
take / skip
buy / don't buy
match / don't match
split at k
move right / down
```

### 4. What is the recurrence?

Example:

```python
dp[i] = max(
    dp[i - 1],
    nums[i] + dp[i - 2]
)
```

### 5. What are the base cases?

Determine the smallest states whose answers are known immediately.

### 6. What order must states be evaluated?

Ask:

> What does my current state depend on?

Then calculate those dependencies first.

### 7. Can dimensions be removed?

If:

```python
dp[i]
```

only needs:

```python
dp[i - 1]
dp[i - 2]
```

replace the array with variables.

If:

```python
dp[i][j]
```

only depends on the previous row, try:

```python
dp[j]
```

---

# High-Value Practice Set

A compact set that covers most major DP ideas:

| Order | Problem | Pattern |
|---:|---|---|
| 1 | LC 70 Climbing Stairs | 1D |
| 2 | LC 198 House Robber | Take/Skip |
| 3 | LC 62 Unique Paths | Grid |
| 4 | LC 322 Coin Change | Unbounded Knapsack |
| 5 | LC 416 Partition Equal Subset Sum | 0/1 Knapsack |
| 6 | LC 494 Target Sum | Knapsack / Counting |
| 7 | LC 300 Longest Increasing Subsequence | LIS |
| 8 | LC 1143 Longest Common Subsequence | Two Sequences |
| 9 | LC 72 Edit Distance | Two Sequences |
| 10 | LC 516 Longest Palindromic Subsequence | Interval |
| 11 | LC 312 Burst Balloons | Interval / Last Operation |
| 12 | LC 309 Stock with Cooldown | State Machine |
| 13 | LC 337 House Robber III | Tree DP |
| 14 | LC 698 Partition to K Equal Sum Subsets | Bitmask / Subsets |
| 15 | LC 805 Split Array With Same Average | Meet in the Middle |
| 16 | LC 2719 Count of Integers | Digit DP |

---

# One-Screen Pattern Map

```text
DYNAMIC PROGRAMMING
│
├── 1. Linear / 1D
│   ├── Climbing Stairs
│   ├── House Robber
│   └── Decode Ways
│
├── 2. Grid
│   ├── Unique Paths
│   ├── Minimum Path Sum
│   └── Dungeon Game
│
├── 3. Knapsack
│   ├── 0/1
│   │   ├── Partition Equal Subset Sum
│   │   ├── Target Sum
│   │   └── Last Stone Weight II
│   │
│   └── Unbounded
│       ├── Coin Change
│       ├── Coin Change II
│       └── Perfect Squares
│
├── 4. Two-Sequence
│   ├── LCS
│   ├── Edit Distance
│   └── Distinct Subsequences
│
├── 5. LIS
│   ├── LIS
│   ├── Count LIS
│   └── Russian Doll Envelopes
│
├── 6. Interval
│   ├── Split Point
│   ├── Last Operation
│   ├── Games
│   └── Palindromes
│
├── 7. String / Matching
│   ├── Regex
│   ├── Wildcard
│   └── Interleaving String
│
├── 8. State Machine
│   ├── Stock Problems
│   ├── Paint Fence
│   └── Domino/Tromino
│
├── 9. Tree DP
│   ├── House Robber III
│   └── Tree States
│
├── 10. Bitmask DP
│   ├── Subset states
│   └── Visited states
│
├── 11. Digit DP
│   └── Count numbers <= N
│
├── 12. Meet in the Middle
│   └── n ≈ 30–40 subset problems
│
└── 13. Probability DP
    ├── Soup Servings
    └── New 21 Game
```
