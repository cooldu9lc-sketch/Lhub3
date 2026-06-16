from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
      

        n = len(values)

        dp = [[0] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):

            for r in range(l + 2, n): ##gap should be at least 2

                dp[l][r] = float('inf')

                for k in range(l + 1, r): #both left and right are not included and used as

                    dp[l][r] = min(dp[l][r],dp[l][k]+ dp[k][r]+ values[l] * values[k] * values[r])

        return dp[0][n - 1]