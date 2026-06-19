class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        # gap = r - l
        # gap = 1 means no internal cut (because of sentinel nodes) => cost 0
        for l in range(m-1,-1, -1):
            for r in range(l+2, m):
                #r = l + gap
                dp[l][r] = float('inf')

                for k in range(l+1, r):
                    cost = dp[l][k] + dp[k][r] + (cuts[r] - cuts[l])
                    dp[l][r] = min(dp[l][r], cost)

        return dp[0][m - 1]