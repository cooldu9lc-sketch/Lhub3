-   **2-Way Partitioning (Lomuto / Hoare):** Splits the array into two subsets ($\\le \\text{pivot}$ and $> \\text{pivot}$). If an array contains many identical elements (such as `[2, 2, 2, 2, 2]`), a 2-way partition places all duplicates into one side, reducing the active array by only one element per iteration and degrading time complexity to $O(N^2)$.

-   **3-Way Partitioning (Dutch National Flag):** Divides the array into three distinct contiguous segments: strictly less than, equal to, and strictly greater than the pivot. If target index $k$ falls within the `[lt, gt]` range of identical pivot values, the algorithm returns in that step without further recursion.

## src: https://share.gemini.google/iawwwzHvXfVA

## 1. QuickSelect with 2-Way Partitioning (Lomuto)

```python


import random


def quickselect_2way(nums: list[int], k: int) -> int:
    """Finds the k-th smallest element (0-indexed) using 2-way Lomuto partitioning."""

    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot_val = nums[pivot_idx]
        # Move pivot out of the way to the right end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1

        # Place pivot into its correct sorted location
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx

    left, right = 0, len(nums) - 1
    while left <= right:
        # Randomized pivot prevents O(N^2) on sorted inputs
        pivot_idx = random.randint(left, right)
        final_idx = partition(left, right, pivot_idx)

        if final_idx == k:
            return nums[final_idx]
        elif final_idx < k:
            left = final_idx + 1
        else:
            right = final_idx - 1

    return -1
```

## 2. QuickSelect with 3-Way Partitioning (Dutch National Flag)


```python
import random


def quickselect_3way(nums: list[int], k: int) -> int:
    """Finds the k-th smallest element (0-indexed) using 3-way partitioning.

    Guarantees O(N) performance even with extensive duplicate elements.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        pivot = nums[random.randint(left, right)]

        # 3-way pointers:
        # nums[left ... lt-1]   < pivot
        # nums[lt ... i-1]      == pivot
        # nums[gt+1 ... right]  > pivot
        lt = left
        i = left
        gt = right

        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt -= 1
            else:
                i += 1

        # Check which partition holds index k
        if lt <= k <= gt:
            return nums[k]
        elif k < lt:
            right = lt - 1
        else:
            left = gt + 1

    return -1
```

## LeetCode 215: Kth Largest Element in an Array


```python
import random


class Solution:

    def findKthLargest(self, nums: list[int], k: int) -> int:
        target_idx = len(nums) - k  # Convert k-th largest to index from left
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if lt <= target_idx <= gt:
                return nums[target_idx]
            elif target_idx < lt:
                right = lt - 1
            else:
                left = gt + 1

        return -1

```


## LeetCode 973: K Closest Points to Origin


```python
import random


import random


class Solution:

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist_sq(p: list[int]) -> int:
            return p[0] * p[0] + p[1] * p[1]

        target_idx = k - 1
        left, right = 0, len(points) - 1

        while left <= right:
            pivot_dist = dist_sq(points[random.randint(left, right)])
            lt, i, gt = left, left, right

            while i <= gt:
                d = dist_sq(points[i])
                if d < pivot_dist:
                    points[lt], points[i] = points[i], points[lt]
                    lt += 1
                    i += 1
                elif d > pivot_dist:
                    points[gt], points[i] = points[i], points[gt]
                    gt -= 1
                else:
                    i += 1

            if lt <= target_idx <= gt:
                break
            elif target_idx < lt:
                right = lt - 1
            else:
                left = gt + 1

        return points[:k]
```