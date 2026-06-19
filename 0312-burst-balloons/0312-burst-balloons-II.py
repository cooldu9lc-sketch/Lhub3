from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        # length is the distance between l and r
        # we need at least one balloon inside, so r - l >= 2
        for length in range(2, n):
            for l in range(0, n - length):
                r = l + length
                best = 0

                for k in range(l + 1, r):
                    coins = dp[l][k] + arr[l] * arr[k] * arr[r] + dp[k][r]
                    best = max(best, coins)

                dp[l][r] = best

        return dp[0][n - 1]
