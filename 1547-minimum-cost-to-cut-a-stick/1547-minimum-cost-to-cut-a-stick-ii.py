class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = [0] + sorted(cuts) + [n]
        m = len(c)

        dp = [[0] * m for _ in range(m)]

        # gap = r - l
        # gap = 1 means no internal cut => cost 0
        for gap in range(2, m):
            for l in range(0, m - gap):
                r = l + gap
                dp[l][r] = float('inf')

                for k in range(l + 1, r):
                    cost = dp[l][k] + dp[k][r] + (c[r] - c[l])
                    dp[l][r] = min(dp[l][r], cost)

        return dp[0][m - 1]
