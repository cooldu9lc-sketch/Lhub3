# Binary Tree Traversals in Python
## Iterative Stack + Morris Traversal

This cheat sheet covers:

- Preorder: Root → Left → Right
- Inorder: Left → Root → Right
- Postorder: Left → Right → Root
- Iterative stack-based traversal
- Morris traversal using **O(1) auxiliary space**

---

## TreeNode Definition

```python
from typing import Optional, List


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
```

---

# 1. Preorder Traversal

Traversal order:

```text
Root -> Left -> Right
```

## 1.1 Iterative Preorder Using Stack

Because a stack is LIFO, push the **right child first** so that the left child is processed first.

```python
def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(h) average, O(n) worst case
```

---

## 1.2 Morris Preorder Traversal

### Key rule

For preorder, process `curr` when it is encountered for the **first time**.

```python
def preorder_morris(root: Optional[TreeNode]) -> List[int]:
    result = []
    curr = root

    while curr:
        if curr.left is None:
            result.append(curr.val)
            curr = curr.right

        else:
            pred = curr.left

            while pred.right and pred.right is not curr:
                pred = pred.right

            if pred.right is None:
                # First visit to curr
                result.append(curr.val)

                # Temporary thread back to curr
                pred.right = curr
                curr = curr.left

            else:
                # Second visit: restore tree
                pred.right = None
                curr = curr.right

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# 2. Inorder Traversal

Traversal order:

```text
Left -> Root -> Right
```

## 2.1 Iterative Inorder Using Stack

```python
def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    curr = root

    while curr or stack:

        # Go as far left as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process current root
        curr = stack.pop()
        result.append(curr.val)

        # Explore right subtree
        curr = curr.right

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(h)
```

---

## 2.2 Morris Inorder Traversal

For a node with a left subtree, find its inorder predecessor:

```text
rightmost node in curr.left
```

Temporarily set:

```text
predecessor.right = curr
```

This temporary pointer acts like the return address normally stored on the recursion stack.

```python
def inorder_morris(root: Optional[TreeNode]) -> List[int]:
    result = []
    curr = root

    while curr:
        if curr.left is None:
            result.append(curr.val)
            curr = curr.right

        else:
            pred = curr.left

            while pred.right and pred.right is not curr:
                pred = pred.right

            if pred.right is None:
                # First visit
                pred.right = curr
                curr = curr.left

            else:
                # Second visit: left subtree is complete
                pred.right = None
                result.append(curr.val)
                curr = curr.right

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

---

# 3. Postorder Traversal

Traversal order:

```text
Left -> Right -> Root
```

Postorder is harder because a node can only be processed after **both subtrees** have been completed.

## 3.1 Iterative Postorder — One Stack

Track the previously processed node using `last_visited`.

```python
def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    curr = root
    last_visited = None

    while curr or stack:

        if curr:
            stack.append(curr)
            curr = curr.left

        else:
            node = stack[-1]

            # Right subtree still needs to be processed
            if node.right and last_visited is not node.right:
                curr = node.right

            else:
                # Both children are done
                result.append(node.val)
                last_visited = stack.pop()

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(h)
```

---

## Alternative: Iterative Postorder Using Two Stacks

This version is easier to remember but uses more memory.

```python
def postorder_two_stacks(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    result = []

    while stack2:
        result.append(stack2.pop().val)

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

---

# 3.2 Morris Postorder Traversal

Morris postorder is the trickiest Morris traversal.

We introduce a dummy node:

```text
dummy.left = root
```

This allows the real root to be handled exactly like every other subtree.

## Helper: Reverse Right Pointers

```python
def reverse_right_path(start: TreeNode, end: TreeNode) -> None:
    # Reverse right pointers along:
    # start -> ... -> end

    if start is end:
        return

    prev = None
    curr = start

    while True:
        nxt = curr.right
        curr.right = prev
        prev = curr

        if curr is end:
            break

        curr = nxt
```

## Helper: Collect Reversed Boundary

```python
def collect_reverse_path(
    start: TreeNode,
    end: TreeNode,
    result: List[int],
) -> None:
    # Reverse the path, collect from end back to start,
    # then restore the original tree.

    reverse_right_path(start, end)

    node = end

    while True:
        result.append(node.val)

        if node is start:
            break

        node = node.right

    reverse_right_path(end, start)
```

## Complete Morris Postorder

```python
def postorder_morris(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []

    dummy = TreeNode(0)
    dummy.left = root

    curr = dummy

    while curr:
        if curr.left is None:
            curr = curr.right

        else:
            pred = curr.left

            while pred.right and pred.right is not curr:
                pred = pred.right

            if pred.right is None:
                # First visit
                pred.right = curr
                curr = curr.left

            else:
                # Second visit:
                # emit the right boundary of the left subtree
                # in reverse order.
                collect_reverse_path(
                    curr.left,
                    pred,
                    result,
                )

                pred.right = None
                curr = curr.right

    return result
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

The output list is not counted as auxiliary space.

---

# Morris Traversal Pattern

At node `curr`, find:

```text
pred = rightmost node of curr.left
```

Then there are two cases.

## First Visit

```python
if pred.right is None:
    pred.right = curr
    curr = curr.left
```

We temporarily create a thread:

```text
predecessor.right -> curr
```

## Second Visit

```python
else:
    pred.right = None
    curr = curr.right
```

The temporary thread tells us that the left subtree has already been traversed.

---

# Preorder vs Inorder Morris

The core algorithm is almost identical.

The important difference is **when `curr` is processed**.

## Preorder

```text
Root -> Left -> Right
```

Process on the **first visit**:

```python
if pred.right is None:
    result.append(curr.val)
```

## Inorder

```text
Left -> Root -> Right
```

Process on the **second visit**:

```python
else:
    pred.right = None
    result.append(curr.val)
```

---

# Quick Comparison

| Traversal | Iterative Technique | Morris Processing |
|---|---|---|
| Preorder | Pop root; push right then left | Process on first visit |
| Inorder | Push full left path; pop root | Process on second visit |
| Postorder | Track `last_visited` | Reverse right boundary when removing thread |

---

# Complexity Summary

| Traversal | Method | Time | Auxiliary Space |
|---|---|---:|---:|
| Preorder | Iterative Stack | O(n) | O(h) |
| Preorder | Morris | O(n) | O(1) |
| Inorder | Iterative Stack | O(n) | O(h) |
| Inorder | Morris | O(n) | O(1) |
| Postorder | Iterative One Stack | O(n) | O(h) |
| Postorder | Morris | O(n) | O(1) |

For a balanced tree:

```text
h = O(log n)
```

For a completely skewed tree:

```text
h = O(n)
```

---

# Interview Cheat Sheet

## Preorder — Stack

```python
stack = [root]

while stack:
    node = stack.pop()
    visit(node)

    if node.right:
        stack.append(node.right)

    if node.left:
        stack.append(node.left)
```

Remember:

```text
Push RIGHT before LEFT.
```

---

## Inorder — Stack

```python
while curr or stack:

    while curr:
        stack.append(curr)
        curr = curr.left

    curr = stack.pop()
    visit(curr)
    curr = curr.right
```

Remember:

```text
Go LEFT completely -> POP -> go RIGHT
```

---

## Postorder — Stack

```python
while curr or stack:

    if curr:
        stack.append(curr)
        curr = curr.left

    else:
        node = stack[-1]

        if node.right and last_visited is not node.right:
            curr = node.right

        else:
            visit(node)
            last_visited = stack.pop()
```

Remember:

```text
Process the node only after BOTH children are done.
```

---

# Morris Cheat Sheet

## Find the predecessor

```python
pred = curr.left

while pred.right and pred.right is not curr:
    pred = pred.right
```

## First visit

```python
if pred.right is None:
    pred.right = curr
    curr = curr.left
```

## Second visit

```python
else:
    pred.right = None
    curr = curr.right
```

The main difference between the traversals is:

```text
Preorder:
    process on first visit

Inorder:
    process on second visit

Postorder:
    process the reversed right boundary
    when removing the Morris thread
```

---

# Mental Model

Recursive traversal normally relies on the call stack:

```text
Parent
  ↓
Left subtree
  ↓
return to Parent
  ↓
Right subtree
```

Morris traversal temporarily stores that **return address inside the tree itself**:

```text
predecessor.right -> parent
```

After returning, the temporary pointer is removed:

```text
predecessor.right = None
```

Therefore the original tree structure is restored before the traversal finishes.
