# Iterative Segment Trees — Quick Revision Notes

Source article: https://codeforces.com/blog/entry/18051

> **Convention used in these notes:** all public range operations use **inclusive** intervals `[left, right]`. The original article often uses half-open `[l, r)` ranges; the code below has been intentionally adapted to inclusive boundaries.

---

# 1. Core Mental Model

For an array of length `n`, store the segment tree in an array of size `2 * n`.

```text
tree[1]            -> root

tree[2*i]          -> left child
tree[2*i + 1]      -> right child
tree[i // 2]       -> parent

tree[n : 2*n]      -> original array / leaves
tree[1 : n]        -> internal nodes
```

Example for `n = 8`:

```text
                         tree[1]
                       /         \
                 tree[2]         tree[3]
                 /    \           /    \
             tree[4] tree[5] tree[6] tree[7]
              / \      / \     / \      / \
             8   9   10  11   12 13   14 15
```

Leaves:

```text
tree[8]  -> arr[0]
tree[9]  -> arr[1]
...
tree[15] -> arr[7]
```

---

# 2. Important Index Tricks

```python
left_child  = 2 * i
right_child = 2 * i + 1
parent      = i // 2

is_right_child = i % 2 == 1
```

Equivalent bit operations commonly seen in C++:

```text
i << 1       == 2 * i
i << 1 | 1   == 2 * i + 1
i >> 1       == i // 2
i & 1        == i % 2
i ^ 1        == sibling
```

---

# 3. The Most Important Range Loop

All iterative segment-tree range operations are based on this:

```python
l += n
r += n

while l <= r:

    if l % 2 == 1:
        # l is a right child: consume it
        # before moving to its parent's next segment.
        use_or_update(tree[l])
        l += 1

    if r % 2 == 0:
        # r is a left child: consume it
        # before moving to its parent's previous segment.
        use_or_update(tree[r])
        r -= 1

    l //= 2
    r //= 2
```

The public range convention in these notes is:

```text
[l, r]
```

Both `l` **and** `r` are included.

---

# 4. Why This Range Loop Works

At every level:

- If `l` is a **right child** (`l` is odd), its parent also contains the left sibling, which lies outside the requested range.
  - Therefore use `tree[l]` directly.
  - Then move `l += 1`.

- If `r` is a **left child** (`r` is even), its parent also contains the right sibling, which lies outside the requested range.
  - Therefore use `tree[r]` directly.
  - Then move `r -= 1`.

- After fixing the boundaries:

```python
l //= 2
r //= 2
```

Both pointers move one level upward.

Only `O(log n)` segment-tree nodes are needed.

---

# 5. Case Map

                    SEGMENT TREE
                         │
                         ▼
           Decompose [l,r) into O(log n)
                  canonical nodes
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼
       Point update              Range update
       Range query                    │
            │                         │
            │                ┌────────┴────────┐
            │                │                 │
            ▼                ▼                 ▼
         Basic        Point query only    Range query too
                          │                 │
                          ▼                 ▼
                      No lazy         Lazy propagation

| Update | Query | Lazy? | Template |
|---|---|---:|---|
| Point | Range | No | Generic iterative tree |
| Range add | Point | No | Store updates in covering nodes |
| Point | Non-commutative range query | No | Two accumulators |
| Range add | Range max/sum | Yes | Lazy propagation |
| Range assignment | Range sum | Yes | Lazy propagation + segment length |

---

# 6. Case 1 — Point Update + Range Query

This is the most useful general-purpose template.

It also correctly handles **non-commutative** combine functions because it uses two accumulators.

```python
class SegmentTree:
    """
    Generic iterative segment tree.

    Supports:
        update(index, value)
        query(left, right)

    Range convention:
        [left, right]

    Time:
        build  -> O(n)
        update -> O(log n)
        query  -> O(log n)
    """

    def __init__(self, arr, combine, identity):
        self.n = len(arr)
        self.combine = combine
        self.identity = identity

        self.tree = [identity] * (2 * self.n)

        # Put original values in the leaves.
        self.tree[self.n:] = arr

        # Build internal nodes bottom-up.
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.combine(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def update(self, index, value):
        """
        Replace arr[index] with value.
        """

        p = index + self.n

        # Update leaf.
        self.tree[p] = value

        # Rebuild ancestors.
        while p > 1:
            p //= 2

            self.tree[p] = self.combine(
                self.tree[2 * p],
                self.tree[2 * p + 1]
            )

    def query(self, left, right):
        """
        Query [left, right].
        """

        left += self.n
        right += self.n

        left_result = self.identity
        right_result = self.identity

        while left <= right:

            # left is a right child, so its sibling is outside the range.
            if left % 2 == 1:
                left_result = self.combine(
                    left_result,
                    self.tree[left]
                )
                left += 1

            # right is a left child, so its sibling is outside the range.
            if right % 2 == 0:
                right_result = self.combine(
                    self.tree[right],
                    right_result
                )
                right -= 1

            left //= 2
            right //= 2

        return self.combine(
            left_result,
            right_result
        )
```

## Sum

```python
st = SegmentTree(
    arr,
    combine=lambda a, b: a + b,
    identity=0
)
```

## Minimum

```python
st = SegmentTree(
    arr,
    combine=min,
    identity=float("inf")
)
```

## Maximum

```python
st = SegmentTree(
    arr,
    combine=max,
    identity=float("-inf")
)
```

## String concatenation

Useful for understanding non-commutative operations:

```python
st = SegmentTree(
    ["A", "B", "C", "D"],
    combine=lambda a, b: a + b,
    identity=""
)

print(st.query(1, 3))
# BCD
```

---

# 7. Why Two Query Accumulators?

For sum:

```text
a + b == b + a
```

so order does not matter.

But for something like strings:

```text
"AB" + "CD" != "CD" + "AB"
```

The left boundary discovers segments from:

```text
left -> right
```

so:

```python
left_result = combine(
    left_result,
    tree[left]
)
```

The right boundary discovers segments in the opposite direction, so:

```python
right_result = combine(
    tree[right],
    right_result
)
```

Finally:

```python
return combine(left_result, right_result)
```

This preserves the original order.

---

# 8. Case 2 — Range Add + Point Query

Use this when you only need:

```text
update an entire range
query one individual position
```

No lazy propagation is necessary.

```python
class RangeAddPointQuery:
    """
    Supports:

        add(left, right, delta)
        get(index)

    add() updates [left, right].

    Time:
        range update -> O(log n)
        point query  -> O(log n)
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        # Initial array values live in leaves.
        self.tree[self.n:] = arr

    def add(self, left, right, delta):
        """
        Add delta to every element in [left, right].
        """

        left += self.n
        right += self.n

        while left <= right:

            if left % 2 == 1:
                self.tree[left] += delta
                left += 1

            if right % 2 == 0:
                self.tree[right] += delta
                right -= 1

            left //= 2
            right //= 2

    def get(self, index):
        """
        Return the value at arr[index].
        """

        p = index + self.n
        result = 0

        # Every relevant range update is stored
        # somewhere on this leaf -> root path.
        while p > 0:
            result += self.tree[p]
            p //= 2

        return result
```

### Mental model

A node storing `+5` means:

```text
Every leaf below this node conceptually receives +5.
```

For one point, simply walk from that leaf to the root and add every update encountered.

---

# 9. Case 3 — Lazy Propagation

Lazy propagation is needed when both operations involve ranges:

```text
range update
+
range query
```

Examples:

```text
range add       + range maximum
range add       + range sum
range assign    + range sum
```

The important functions are:

```text
_apply()
_push_path()
_pull_path()
```

Mental model:

```text
apply = modify one whole tree segment

push  = send deferred updates downward

pull  = recalculate ancestors after children changed
```

---

# 10. Case 3A — Range Add + Range Maximum

For maximum:

```text
max([1, 5, 3]) = 5

add +10 to everything

max([11, 15, 13]) = 15
```

Therefore:

```text
new_max = old_max + delta
```

Segment length is NOT needed.

```python
class LazyRangeAddMax:
    """
    Range add + range maximum.

    add(left, right, delta)
    query(left, right)

    Both use [left, right].

    Time:
        update -> O(log n)
        query  -> O(log n)
    """

    def __init__(self, arr):
        self.n = len(arr)

        # Padding to power of two makes lazy propagation easier.
        self.size = 1

        while self.size < self.n:
            self.size *= 2

        self.height = self.size.bit_length() - 1

        NEG_INF = float("-inf")

        self.tree = [NEG_INF] * (2 * self.size)

        # Internal nodes only need lazy tags.
        self.lazy = [0] * self.size

        # Leaves.
        for i, value in enumerate(arr):
            self.tree[self.size + i] = value

        # Build.
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def _apply(self, p, delta):
        """
        Apply +delta to the entire segment represented by p.
        """

        self.tree[p] += delta

        # If p is internal, remember that descendants
        # still need to receive this update.
        if p < self.size:
            self.lazy[p] += delta

    def _push_path(self, p):
        """
        Push deferred updates from root down toward p.
        """

        for shift in range(self.height, 0, -1):

            node = p >> shift
            delta = self.lazy[node]

            if delta != 0:
                self._apply(2 * node, delta)
                self._apply(2 * node + 1, delta)

                self.lazy[node] = 0

    def _pull_path(self, p):
        """
        Rebuild ancestors of p.
        """

        while p > 1:

            p //= 2

            self.tree[p] = (
                max(
                    self.tree[2 * p],
                    self.tree[2 * p + 1]
                )
                + self.lazy[p]
            )

    def add(self, left, right, delta):
        """
        Add delta to [left, right].
        """

        if left > right:
            return

        left += self.size
        right += self.size

        left_boundary = left
        right_boundary = right

        while left <= right:

            if left % 2 == 1:
                self._apply(left, delta)
                left += 1

            if right % 2 == 0:
                self._apply(right, delta)
                right -= 1

            left //= 2
            right //= 2

        # Rebuild both boundary paths.
        self._pull_path(left_boundary)
        self._pull_path(right_boundary)

    def query(self, left, right):
        """
        Maximum over [left, right].
        """

        if left > right:
            return float("-inf")

        left += self.size
        right += self.size

        # Push pending updates along both inclusive boundary paths.
        self._push_path(left)
        self._push_path(right)

        result = float("-inf")

        while left <= right:

            if left % 2 == 1:
                result = max(
                    result,
                    self.tree[left]
                )
                left += 1

            if right % 2 == 0:
                result = max(
                    result,
                    self.tree[right]
                )
                right -= 1

            left //= 2
            right //= 2

        return result
```

---

# 11. Case 3B — Range Assignment + Range Sum

Suppose a node represents 4 elements.

If we do:

```text
assign whole segment = 5
```

then:

```text
segment sum = 5 * 4 = 20
```

Therefore segment length is required.

Also:

```text
assignment order matters
```

because:

```text
assign 5
assign 10
```

is different from:

```text
assign 10
assign 5
```

Use `None` to mean:

```text
no pending assignment
```

This allows `0` to remain a valid assignment.

```python
class LazyRangeAssignSum:
    """
    Range assignment + range sum.

    assign(left, right, value)
    query(left, right)

    Both use [left, right].

    Time:
        update -> O(log n)
        query  -> O(log n)
    """

    def __init__(self, arr):
        self.n = len(arr)

        self.size = 1

        while self.size < self.n:
            self.size *= 2

        self.height = self.size.bit_length() - 1

        self.tree = [0] * (2 * self.size)

        # None = no pending assignment.
        self.lazy = [None] * self.size

        # Number of leaves represented by each node.
        self.length = [0] * (2 * self.size)

        for i in range(self.size):
            self.length[self.size + i] = 1

        for i in range(self.size - 1, 0, -1):
            self.length[i] = (
                self.length[2 * i]
                + self.length[2 * i + 1]
            )

        # Insert initial array.
        for i, value in enumerate(arr):
            self.tree[self.size + i] = value

        # Build sums.
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = (
                self.tree[2 * i]
                + self.tree[2 * i + 1]
            )

    def _apply(self, p, value):
        """
        Assign every element represented by p to value.
        """

        self.tree[p] = (
            value * self.length[p]
        )

        if p < self.size:
            self.lazy[p] = value

    def _push_path(self, p):
        """
        Push assignments from root down toward p.
        """

        for shift in range(self.height, 0, -1):

            node = p >> shift
            value = self.lazy[node]

            if value is not None:

                self._apply(
                    2 * node,
                    value
                )

                self._apply(
                    2 * node + 1,
                    value
                )

                self.lazy[node] = None

    def _pull_path(self, p):
        """
        Recalculate ancestors of p.
        """

        while p > 1:

            p //= 2

            if self.lazy[p] is None:

                self.tree[p] = (
                    self.tree[2 * p]
                    + self.tree[2 * p + 1]
                )

            else:

                # A pending assignment still defines
                # the entire segment.
                self.tree[p] = (
                    self.lazy[p]
                    * self.length[p]
                )

    def assign(self, left, right, value):
        """
        arr[left:right + 1] = value
        """

        if left > right:
            return

        left_leaf = left + self.size
        right_leaf = right + self.size

        # Assignment order matters.
        # Push old assignments first along both boundary paths.
        self._push_path(left_leaf)
        self._push_path(right_leaf)

        l = left_leaf
        r = right_leaf

        while l <= r:

            if l % 2 == 1:
                self._apply(l, value)
                l += 1

            if r % 2 == 0:
                self._apply(r, value)
                r -= 1

            l //= 2
            r //= 2

        self._pull_path(left_leaf)
        self._pull_path(right_leaf)

    def query(self, left, right):
        """
        Sum over [left, right].
        """

        if left > right:
            return 0

        l = left + self.size
        r = right + self.size

        self._push_path(l)
        self._push_path(r)

        result = 0

        while l <= r:

            if l % 2 == 1:
                result += self.tree[l]
                l += 1

            if r % 2 == 0:
                result += self.tree[r]
                r -= 1

            l //= 2
            r //= 2

        return result
```

---

# 12. Lazy Propagation Cheat Sheet

Think of lazy propagation as four questions.

## 1. What does `tree[node]` mean?

Examples:

```text
range sum tree -> sum of segment
range max tree -> maximum of segment
range min tree -> minimum of segment
```

## 2. What does `lazy[node]` mean?

It means:

```text
There is an update affecting every descendant,
but it has not yet been physically propagated downward.
```

Examples:

```text
lazy[node] = +10
```

means:

```text
every descendant conceptually has +10
```

Assignment example:

```text
lazy[node] = 5
```

means:

```text
every descendant should become 5
```

## 3. How does the update affect the aggregate?

### Add + max

```text
tree[node] += delta
```

### Add + sum

```text
tree[node] += delta * segment_length
```

### Assignment + sum

```text
tree[node] = value * segment_length
```

## 4. How do lazy tags combine?

### Add after add

```text
+x
+y
```

becomes:

```text
+(x + y)
```

### Assignment after assignment

```text
=5
=10
```

becomes:

```text
=10
```

The newer assignment replaces the older one.

---

# 13. Which Template Should I Use?

```text
Do I update only one element?
        |
        +-- YES --> Point Update + Range Query tree
        |
        NO
        |
Do I only query one element?
        |
        +-- YES --> Range Add + Point Query tree
        |
        NO
        |
        --> Range Update + Range Query
            --> Lazy propagation
```

---

# 14. Complexity Summary

| Operation | Complexity |
|---|---:|
| Build iterative tree | `O(n)` |
| Point update | `O(log n)` |
| Range query | `O(log n)` |
| Range add + point query update | `O(log n)` |
| Range add + point query lookup | `O(log n)` |
| Lazy range update | `O(log n)` |
| Lazy range query | `O(log n)` |
| Memory | `O(n)` |

---

# 15. FAQ

## Q1. What does `build()` do?

`build()` computes every internal tree node from its children.

For sum:

```python
tree[i] = tree[2*i] + tree[2*i + 1]
```

For maximum:

```python
tree[i] = max(
    tree[2*i],
    tree[2*i + 1]
)
```

Build bottom-up:

```python
for i in range(n - 1, 0, -1):
    ...
```

because children must exist before their parent is calculated.

---

## Q2. What does `update()` do in the normal tree?

A point update:

1. changes one leaf,
2. walks from that leaf toward the root,
3. recomputes every ancestor.

```text
leaf
 ↑
parent
 ↑
parent
 ↑
root
```

Only one node changes per level, so complexity is:

```text
O(log n)
```

---

## Q3. What does `query()` do?

`query(l, r)` breaks the **inclusive** interval:

```text
[l, r]
```

into a small set of complete segment-tree nodes.

Instead of looking at every array element, it combines only:

```text
O(log n)
```

tree segments.

---

## Q4. Why do we do `l += n` and `r += n`?

The user gives normal array indices.

But the actual array values are stored in the leaf section:

```text
tree[n : 2*n]
```

Therefore:

```python
leaf_index = n + array_index
```

---

## Q5. What does the inclusive `[l, r]` convention mean?

Every public range operation in these notes includes **both endpoints**.

```text
[l, r]
```

means:

```text
include l
include r
```

Example:

```text
[2, 5]
```

contains:

```text
2, 3, 4, 5
```

If you wanted the same elements with Python slicing, you would write:

```python
arr[2:6]
```

This differs from the original article's usual half-open `[l, r)` convention, but the tree logic in this sheet has been fully adapted for inclusive endpoints.

---

## Q6. Why do we check `l % 2 == 1`?

An odd tree index is a right child.

```text
        parent
        /    \
     sibling   l
```

If we climbed directly to `parent`, the segment would also include the sibling, which is outside the query.

Therefore:

```python
use(tree[l])
l += 1
```

before moving upward.

---

## Q7. Why do we check `r % 2 == 0`?

Because `r` itself is included.

An even tree index is a **left child**:

```text
        parent
        /    \
       r    sibling
```

If we moved directly to the parent, we would incorrectly include the right sibling, which lies outside the requested range.

Therefore consume `tree[r]` first:

```python
use(tree[r])
r -= 1
```

Then it is safe to move both boundaries upward.

---

## Q8. What does `pull()` do?

`pull()` moves upward and recomputes parent values from their children.

Conceptually:

```python
tree[parent] = combine(
    tree[left_child],
    tree[right_child]
)
```

Use `pull()` after something below the parent changes.

Direction:

```text
bottom -> top
```

---

## Q9. What does `push()` do?

`push()` propagates a delayed update from a parent into its children.

Before:

```text
         node (+10 lazy)
         /            \
      child          child
```

After:

```text
          node
         /    \
      +10      +10
```

Then the parent's lazy marker is cleared.

Direction:

```text
top -> bottom
```

---

## Q10. What is the difference between `push()` and `pull()`?

```text
push:
    parent -> children
    send pending lazy information downward

pull:
    children -> parent
    recompute aggregate information upward
```

Memory trick:

```text
PUSH updates DOWN
PULL results UP
```

---

## Q11. Why do queries call `push()` before reading descendants?

Suppose a parent says:

```text
everything below me has +10
```

but its children have not yet received that update.

If a query wants only part of that parent's range, it must inspect those children.

Therefore the pending update must first be pushed down.

Otherwise the query would read stale child values.

---

## Q12. Why does an update call `pull()` afterward?

A range update may directly modify nodes lower in the tree.

Their ancestors may now contain outdated aggregates.

Example:

```text
parent max = 10
```

but after a child receives `+20`:

```text
child max = 25
```

the parent must be recomputed.

Therefore `pull()` restores correct parent values.

---

## Q13. Why do lazy updates exist?

Without lazy propagation, updating every element in a large range could cost:

```text
O(n)
```

Instead, update one segment-tree node representing the entire range and remember:

```text
"the children still need this update later"
```

That deferred information is the lazy tag.

---

## Q14. Why doesn't range-add + point-query need lazy propagation?

Because a point query only follows one path:

```text
leaf -> root
```

All range updates affecting that point are stored somewhere on that path.

So there is no need to maintain accurate aggregate values for every internal node.

---

## Q15. Why does range assignment require more care than range addition?

Addition combines naturally:

```text
+5 followed by +10
```

can be stored as:

```text
+15
```

Assignment overwrites:

```text
=5 followed by =10
```

must become:

```text
=10
```

The ordering matters.

---

## Q16. Why is segment length required for range sum?

Suppose a node represents `k` elements.

If we add `x` to every element:

```text
new_sum = old_sum + x * k
```

If we assign every element to `x`:

```text
new_sum = x * k
```

So the update needs to know how many elements the node represents.

---

## Q17. Why doesn't range maximum need segment length?

Adding `x` to every element changes:

```text
old_max
```

into:

```text
old_max + x
```

regardless of how many elements are present.

---

## Q18. What does `_apply()` do?

`_apply()` performs an update on one whole segment-tree node.

For range add + max:

```python
tree[node] += delta
lazy[node] += delta
```

For assignment + sum:

```python
tree[node] = value * segment_length
lazy[node] = value
```

Think:

```text
apply = "this entire node is covered by the update"
```

---

## Q19. Why is `None` useful for lazy assignment?

Using:

```python
lazy[node] = 0
```

to mean "no update" prevents us from distinguishing:

```text
no assignment
```

from:

```text
assign everything to zero
```

Using:

```python
None
```

solves this:

```text
None -> no pending assignment
0    -> assign segment to zero
```

---

## Q20. Why do some implementations pad to the next power of two?

The `2*n` iterative representation works without padding.

However, lazy propagation is easier to reason about when all leaves are at the same tree depth.

Therefore many implementations use:

```python
size = 1

while size < n:
    size *= 2
```

The asymptotic complexity remains:

```text
O(n) memory
O(log n) updates
O(log n) queries
```

---

# 16. Final Memorization Sheet

Remember these first:

```python
left_child  = 2 * i
right_child = 2 * i + 1
parent      = i // 2
```

Remember the interval decomposition:

```python
l += n
r += n

while l <= r:

    if l % 2 == 1:
        use(l)
        l += 1

    if r % 2 == 0:
        use(r)
        r -= 1

    l //= 2
    r //= 2
```

Remember lazy propagation:

```text
apply = update whole node

push  = move lazy update DOWN

pull  = rebuild aggregate UP
```

And finally:

```text
point update + range query
    -> normal tree

range update + point query
    -> store updates on covering nodes

range update + range query
    -> lazy propagation
```
