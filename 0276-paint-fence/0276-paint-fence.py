class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k

        same = 0
        diff = k

        for _ in range(2, n + 1):
            same,diff = diff, (same + diff) * (k - 1)
        return same + diff