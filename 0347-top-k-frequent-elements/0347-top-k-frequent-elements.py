from collections import Counter
import random


class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        unique = list(count.keys())
        target_idx = len(unique) - k

        left, right = 0, len(unique) - 1
        while left <= right:
            pivot_freq = count[unique[random.randint(left, right)]]
            lt, i, gt = left, left, right

            while i <= gt:
                freq = count[unique[i]]
                if freq < pivot_freq:
                    unique[lt], unique[i] = unique[i], unique[lt]
                    lt += 1
                    i += 1
                elif freq > pivot_freq:
                    unique[gt], unique[i] = unique[i], unique[gt]
                    gt -= 1
                else:
                    i += 1

            if lt <= target_idx <= gt:
                break
            elif target_idx < lt:
                right = lt - 1
            else:
                left = gt + 1

        return unique[target_idx:]