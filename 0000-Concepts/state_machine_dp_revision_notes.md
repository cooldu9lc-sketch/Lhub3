# State Machine DP — LeetCode Revision Notes

> **Core idea:** Instead of only asking “what is the answer up to index `i`?”, ask:
>
> **“What state am I in after processing up to `i`, and which transitions are legal?”**

---

## 1. Recognition Pattern

State Machine DP is useful when:

- You can describe the process using a **small set of states**.
- An action moves you from one state to another.
- The previous state restricts which actions are legal next.
- The problem contains phrases such as:
  - holding / not holding
  - buy / sell / cooldown
  - same / different
  - take / skip
  - matched / unmatched
  - at most `k` operations
  - previous choice restricts current choice

### Mental Model

```text
State A ----action----> State B
   ^                       |
   |                       |
   +------action-----------+
```

DP computes the best/count/possible path through this small state graph.

---

# 2. Generic Templates

## Explicit State Template

```python
state1 = ...
state2 = ...

for x in items:
    new_state1 = transition(...)
    new_state2 = transition(...)

    state1 = new_state1
    state2 = new_state2

return answer
```

## General Graph-of-States Template

```python
states = [...]

for item in items:
    next_states = states[:]

    for old_state in states:
        for transition in legal_transitions(old_state):
            next_states[new_state] = best(
                next_states[new_state],
                value(old_state, transition)
            )

    states = next_states
```

## 2D Automaton DP

```python
dp[i][state]
```

Meaning:

```text
Answer after processing i elements while being in `state`.
```

For string matching problems, the state is often:

```python
dp[i][j]
```

where:

```text
i = position in input string
j = position in pattern / automaton
```

---

# 3. State Machine DP Roadmap

## Level 1 — Learn Explicit States

| LC | Problem | States |
|---|---|---|
| 121 | Best Time to Buy and Sell Stock | hold / cash |
| 122 | Best Time to Buy and Sell Stock II | hold / cash |
| 198 | House Robber | rob / skip |
| 256 | Paint House | red / green / blue |
| 276 | Paint Fence | same / diff |

## Level 2 — Add Transition Restrictions

| LC | Problem | Key Idea |
|---|---|---|
| 309 | Stock with Cooldown | hold / sold / rest |
| 714 | Stock with Transaction Fee | fee on transition |
| 213 | House Robber II | circular restriction |
| 790 | Domino and Tromino Tiling | full / gap |

## Level 3 — Transaction / State Count

| LC | Problem | Key Idea |
|---|---|---|
| 123 | Stock III | buy1 / sell1 / buy2 / sell2 |
| 188 | Stock IV | `buy[t]` / `sell[t]` |
| 801 | Minimum Swaps to Make Sequences Increasing | swap / no-swap |

## Level 4 — Automaton DP

| LC | Problem | State |
|---|---|---|
| 10 | Regular Expression Matching | `(i, j)` |
| 44 | Wildcard Matching | `(i, j)` |
| 552 | Student Attendance Record II | attendance states |
| 1397 | Find All Good Strings | string automaton |

---

# 4. LC 121 — Best Time to Buy and Sell Stock

## States

```text
hold = currently holding one stock
cash = currently not holding stock
```

Only one transaction is allowed.

## Transition

```python
hold = max(hold, -price)
cash = max(cash, hold + price)
```

## Code

```python
def maxProfit(prices):
    hold = float("-inf")
    cash = 0

    for price in prices:
        old_hold = hold

        hold = max(hold, -price)
        cash = max(cash, old_hold + price)

    return cash
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 5. LC 122 — Best Time to Buy and Sell Stock II

Unlimited transactions.

## State Transitions

```text
cash --buy--> hold
hold --sell--> cash

cash --skip--> cash
hold --skip--> hold
```

```python
new_hold = max(
    hold,           # do nothing
    cash - price    # buy
)

new_cash = max(
    cash,           # do nothing
    hold + price    # sell
)
```

## Code

```python
def maxProfit(prices):
    hold = float("-inf")
    cash = 0

    for price in prices:
        old_hold = hold
        old_cash = cash

        hold = max(old_hold, old_cash - price)
        cash = max(old_cash, old_hold + price)

    return cash
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 6. LC 309 — Stock with Cooldown

## States

```text
hold = holding stock
sold = sold stock today
rest = not holding and allowed/resting
```

## State Machine

```text
rest ----buy----> hold
hold ----sell---> sold
sold -----------> rest

hold ----wait---> hold
rest ----wait---> rest
```

You cannot directly do:

```text
sold -> hold
```

because of the cooldown.

## Transitions

```python
new_hold = max(
    hold,
    rest - price
)

new_sold = hold + price

new_rest = max(
    rest,
    sold
)
```

## Code

```python
def maxProfit(prices):
    hold = float("-inf")
    sold = float("-inf")
    rest = 0

    for price in prices:
        old_hold = hold
        old_sold = sold
        old_rest = rest

        hold = max(old_hold, old_rest - price)
        sold = old_hold + price
        rest = max(old_rest, old_sold)

    return max(sold, rest)
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 7. LC 714 — Stock with Transaction Fee

## States

Same as unlimited stock:

```text
cash <----sell---- hold
  |                 ^
  +------buy--------+
```

Pay the fee when selling:

```python
new_hold = max(
    hold,
    cash - price
)

new_cash = max(
    cash,
    hold + price - fee
)
```

## Code

```python
def maxProfit(prices, fee):
    hold = float("-inf")
    cash = 0

    for price in prices:
        old_hold = hold
        old_cash = cash

        hold = max(old_hold, old_cash - price)
        cash = max(old_cash, old_hold + price - fee)

    return cash
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 8. LC 123 — At Most Two Transactions

## States

```text
buy1 -> sell1 -> buy2 -> sell2
```

Meaning:

```text
buy1  = best profit after first buy
sell1 = best profit after first sell
buy2  = best profit after second buy
sell2 = best profit after second sell
```

## Transitions

```python
buy1  = max(buy1, -price)
sell1 = max(sell1, buy1 + price)

buy2  = max(buy2, sell1 - price)
sell2 = max(sell2, buy2 + price)
```

## Code

```python
def maxProfit(prices):
    buy1 = float("-inf")
    sell1 = 0

    buy2 = float("-inf")
    sell2 = 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)

        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 9. LC 188 — At Most K Transactions

Generalize:

```text
buy1 -> sell1 -> buy2 -> sell2 -> ... -> buyK -> sellK
```

## Transition

For transaction `t`:

```python
buy[t] = max(
    buy[t],
    sell[t - 1] - price
)

sell[t] = max(
    sell[t],
    buy[t] + price
)
```

## Code

```python
def maxProfit(k, prices):
    buy = [float("-inf")] * (k + 1)
    sell = [0] * (k + 1)

    for price in prices:
        for t in range(1, k + 1):
            buy[t] = max(
                buy[t],
                sell[t - 1] - price
            )

            sell[t] = max(
                sell[t],
                buy[t] + price
            )

    return sell[k]
```

**Time:** `O(nk)`  
**Space:** `O(k)`

---

# 10. LC 198 — House Robber

This is also a state machine.

## States

```text
rob  = current house is robbed
skip = current house is skipped
```

## Legal Transitions

```text
skip -> rob
skip -> skip
rob  -> skip
```

Illegal:

```text
rob -> rob
```

because adjacent houses cannot both be robbed.

## Transition

```python
new_rob = skip + money

new_skip = max(
    rob,
    skip
)
```

## Code

```python
def rob(nums):
    rob_state = 0
    skip_state = 0

    for money in nums:
        new_rob = skip_state + money
        new_skip = max(rob_state, skip_state)

        rob_state = new_rob
        skip_state = new_skip

    return max(rob_state, skip_state)
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 11. LC 256 — Paint House

## States

State = color of previous/current house.

```text
R = minimum cost ending in red
G = minimum cost ending in green
B = minimum cost ending in blue
```

Same colors cannot be adjacent.

## Transitions

```python
new_R = red_cost + min(G, B)
new_G = green_cost + min(R, B)
new_B = blue_cost + min(R, G)
```

## Code

```python
def minCost(costs):
    R = G = B = 0

    for red, green, blue in costs:
        new_R = red + min(G, B)
        new_G = green + min(R, B)
        new_B = blue + min(R, G)

        R, G, B = new_R, new_G, new_B

    return min(R, G, B)
```

**Time:** `O(n)`  
**Space:** `O(1)`

---

# 12. LC 276 — Paint Fence

Constraint:

```text
No more than two adjacent fence posts can have the same color.
```

## States

Do **not** track the actual color.

Track the relationship with the previous post:

```text
same = last two posts have the same color
diff = last two posts have different colors
```

## State Machine

```text
            same color
diff --------------------> same

             different
same --------------------> diff
diff --------------------> diff
```

Illegal:

```text
same -> same
```

That would produce three consecutive posts of the same color.

---

## Transition 1 — Make Current Same

If current color equals previous color, the previous state must have been `diff`.

There is only one choice: use the previous color.

```python
new_same = diff
```

---

## Transition 2 — Make Current Different

Previous state can be either:

```text
same
diff
```

Choose any color except the previous color:

```text
k - 1 choices
```

Therefore:

```python
new_diff = (same + diff) * (k - 1)
```

---

## Code

```python
def numWays(n, k):
    if n == 0:
        return 0

    if n == 1:
        return k

    # After first post:
    same = 0
    diff = k

    for _ in range(2, n + 1):
        new_same = diff

        new_diff = (
            same + diff
        ) * (k - 1)

        same = new_same
        diff = new_diff

    return same + diff
```

**Time:** `O(n)`  
**Space:** `O(1)`

### Remember

```text
SAME can only come from DIFF.

DIFF can come from either state.
```

---

# 13. LC 790 — Domino and Tromino Tiling

This is a **boundary/profile state machine**.

Instead of remembering the entire board, remember only what the boundary currently looks like.

## States

```text
full[i] = number of ways to completely tile width i

gap[i] = number of ways to tile width i with one boundary square missing
```

The upper-gap and lower-gap configurations are symmetric, so one `gap` state can represent either orientation.

---

## Full State

```text
██
██
```

## Gap State

One orientation:

```text
██
█.
```

Symmetric orientation:

```text
█.
██
```

---

## Transitions

For a completely filled board:

```python
full[i] = (
    full[i - 1]
    + full[i - 2]
    + 2 * gap[i - 1]
)
```

Why?

```text
full[i-1]      -> add vertical domino
full[i-2]      -> add two horizontal dominoes
2 * gap[i-1]   -> complete either gap orientation using tromino
```

Gap transition:

```python
gap[i] = (
    gap[i - 1]
    + full[i - 2]
)
```

A gap can:

```text
gap -> gap
full -> gap
```

---

## Code

```python
def numTilings(n):
    MOD = 10**9 + 7

    if n == 0:
        return 1

    if n == 1:
        return 1

    full = [0] * (n + 1)
    gap = [0] * (n + 1)

    full[0] = 1
    full[1] = 1

    for i in range(2, n + 1):
        full[i] = (
            full[i - 1]
            + full[i - 2]
            + 2 * gap[i - 1]
        ) % MOD

        gap[i] = (
            gap[i - 1]
            + full[i - 2]
        ) % MOD

    return full[n]
```

**Time:** `O(n)`  
**Space:** `O(n)` — can be compressed.

### Recognition Insight

If a tiling problem leaves only a few possible shapes at the frontier:

> **Make each frontier shape a state.**

---

# 14. LC 10 — Regular Expression Matching

Pattern syntax:

```text
. = any single character
* = zero or more occurrences of the PREVIOUS element
```

Important:

```text
a*
```

means:

```text
"", "a", "aa", "aaa", ...
```

`*` does **not** independently mean "anything".

---

## State

```python
dp(i, j)
```

means:

```text
Can s[i:] match p[j:]?
```

State:

```text
(i, j)
```

is therefore:

```text
input position + pattern position
```

---

## Normal Character / `.`

If characters match:

```text
(i, j)
   |
 consume both
   v
(i+1, j+1)
```

Match condition:

```python
match = (
    i < len(s)
    and (
        s[i] == p[j]
        or p[j] == "."
    )
)
```

Then:

```python
match and dp(i + 1, j + 1)
```

---

## `*` Transition

Suppose pattern is:

```text
a*
```

There are two meaningful choices.

### Choice 1 — Use `a*` Zero Times

Skip the entire pair:

```text
a*
^^
```

Transition:

```python
dp(i, j + 2)
```

### Choice 2 — Consume One Character

If current character matches `a`:

```python
match and dp(i + 1, j)
```

Notice:

```text
j DOES NOT MOVE
```

because `*` may consume more characters.

---

## Core Transition

```python
if next character is "*":
    return (
        dp(i, j + 2)
        or
        (match and dp(i + 1, j))
    )
```

---

## Memoized Code

```python
from functools import cache

def isMatch(s, p):

    @cache
    def dp(i, j):

        if j == len(p):
            return i == len(s)

        match = (
            i < len(s)
            and (
                s[i] == p[j]
                or p[j] == "."
            )
        )

        if (
            j + 1 < len(p)
            and p[j + 1] == "*"
        ):
            return (
                dp(i, j + 2)
                or
                (
                    match
                    and dp(i + 1, j)
                )
            )

        return (
            match
            and dp(i + 1, j + 1)
        )

    return dp(0, 0)
```

**Time:** `O(mn)`  
**Space:** `O(mn)`

---

## Bottom-Up Transition

Define:

```text
dp[i][j] = whether s[:i] matches p[:j]
```

Normal character / `.`:

```python
dp[i][j] = dp[i - 1][j - 1]
```

For `*`:

```python
dp[i][j] = (
    dp[i][j - 2]
    or
    (
        char_matches
        and dp[i - 1][j]
    )
)
```

### The Important Regex `*` Formula

```text
dp[i][j-2]
    ^
    |
use x* ZERO times


dp[i-1][j]
    ^
    |
use x* one MORE time
```

---

# 15. LC 44 — Wildcard Matching

Wildcard syntax:

```text
? = exactly one arbitrary character
* = any sequence of characters
```

Unlike regex:

```text
Regex:
a* = zero or more "a"

Wildcard:
*  = zero or more ANY characters
```

This distinction is extremely important.

---

## State

```python
dp(i, j)
```

means:

```text
Can s[i:] match p[j:]?
```

---

## Normal Character / `?`

If:

```text
s[i] == p[j]
```

or:

```text
p[j] == "?"
```

consume both:

```text
(i, j)
   |
   v
(i+1, j+1)
```

---

# `*` Transition

Wildcard `*` has two necessary choices.

## Choice 1 — Match Empty String

```python
dp(i, j + 1)
```

Pattern advances.

String stays.

```text
(i,j) -> (i,j+1)
```

---

## Choice 2 — Consume One Character

```python
dp(i + 1, j)
```

String advances.

Pattern stays on `*`, allowing it to consume additional characters.

```text
(i,j) -> (i+1,j)
```

---

## Why Don't We Need `(i+1, j+1)`?

Because it is already represented by the two recursive possibilities.

`*` can consume:

```text
0 chars
1 char
2 chars
3 chars
...
```

through repeated:

```text
(i,j)
   |
(i+1,j)
   |
(i+2,j)
   |
(i+3,j)
```

and eventually:

```text
(i+k,j+1)
```

when we choose the empty/finish transition.

---

## Memoized Code

```python
from functools import cache

def isMatch(s, p):

    @cache
    def dp(i, j):

        if j == len(p):
            return i == len(s)

        if p[j] == "*":
            return (
                dp(i, j + 1)
                or
                (
                    i < len(s)
                    and dp(i + 1, j)
                )
            )

        match = (
            i < len(s)
            and (
                s[i] == p[j]
                or p[j] == "?"
            )
        )

        return (
            match
            and dp(i + 1, j + 1)
        )

    return dp(0, 0)
```

**Time:** `O(mn)`  
**Space:** `O(mn)`

---

## Bottom-Up Transition

Define:

```text
dp[i][j] = whether s[:i] matches p[:j]
```

For normal character or `?`:

```python
dp[i][j] = (
    char_matches
    and dp[i - 1][j - 1]
)
```

For wildcard `*`:

```python
dp[i][j] = (
    dp[i][j - 1]
    or
    dp[i - 1][j]
)
```

Interpretation:

```text
dp[i][j-1]
    |
    +-- * matches EMPTY

dp[i-1][j]
    |
    +-- * consumes another character
```

---

# 16. LC 10 vs LC 44 — Must Know

| Feature | LC 10 Regex | LC 44 Wildcard |
|---|---|---|
| Single wildcard | `.` | `?` |
| `*` meaning | repeats previous token | matches arbitrary sequence |
| Example | `a*` | `*` |
| Empty transition | `j - 2` | `j - 1` |
| Consume transition | `dp[i-1][j]` | `dp[i-1][j]` |

## Regex

```text
a*

ZERO a:
dp[i][j-2]

MORE a:
dp[i-1][j]
```

Formula:

```python
dp[i][j] = (
    dp[i][j - 2]
    or
    (
        matches_previous_token
        and dp[i - 1][j]
    )
)
```

## Wildcard

```text
*

ZERO chars:
dp[i][j-1]

MORE chars:
dp[i-1][j]
```

Formula:

```python
dp[i][j] = (
    dp[i][j - 1]
    or
    dp[i - 1][j]
)
```

---

# 17. Three Major State-Machine DP Families

## Type 1 — Small Explicit State

Examples:

```text
Stock:
hold / cash

House Robber:
rob / skip

Paint Fence:
same / diff
```

Typical representation:

```python
state1 = ...
state2 = ...

for x in input:
    new_state1 = ...
    new_state2 = ...
```

---

## Type 2 — Boundary / Profile State

Example:

```text
LC 790

full
gap
```

Common in:

- tiling
- board filling
- profile DP

Ask:

> What information about the boundary is sufficient to continue?

---

## Type 3 — Automaton State

Examples:

```text
LC 10
LC 44
```

State:

```text
(input_position, automaton_position)
```

Typical representation:

```python
dp(i, j)
```

Ask:

> From `(i,j)`, which transitions can the pattern make?

---

# 18. Fast Interview Checklist

When you suspect State Machine DP, do this:

### Step 1 — Ignore the DP equation initially

Ask:

```text
What situations can I currently be in?
```

### Step 2 — Name the states

Examples:

```text
hold / cash

rob / skip

same / diff

full / gap
```

### Step 3 — Draw legal arrows

Example:

```text
skip ---> rob
  |        |
  +------> skip
```

### Step 4 — Ask what each arrow costs/adds

Examples:

```text
buy:
-profit -= price

sell:
profit += price

paint different:
multiply by k-1
```

### Step 5 — Convert incoming arrows into recurrence

If:

```text
A ---> C
B ---> C
```

then generally:

```python
C = best(
    transition_from_A,
    transition_from_B
)
```

For optimization:

```python
C = max(...)
```

or:

```python
C = min(...)
```

For counting:

```python
C = sum(...)
```

For feasibility:

```python
C = OR(...)
```

---

# 19. One-Line Recognition Cheat Sheet

```text
STOCK
    holding / not holding
        -> state machine

HOUSE ROBBER
    take / skip
        -> state machine

PAINTING
    previous choice restricts current
        -> state machine

TILING
    few possible boundary shapes
        -> profile state machine

REGEX / WILDCARD
    pattern has transitions between positions
        -> automaton state machine

AT MOST K ACTIONS
    operation count becomes part of state
        -> state machine
```

---

# 20. Final Mental Model

The most useful way to remember the entire pattern:

> **State Machine DP = DP over a small directed graph of legal situations.**

Instead of thinking:

```text
"What is dp[i]?"
```

first think:

```text
"What states can exist after processing i?"
```

Then:

```text
"What legal action moves me between those states?"
```

Finally turn every arrow into a recurrence:

```text
STATE + TRANSITION -> NEXT STATE
```

That is the reusable pattern behind:

```text
LC 121 / 122 / 123 / 188
LC 198
LC 256 / 276
LC 309 / 714
LC 790
LC 10 / 44
```
