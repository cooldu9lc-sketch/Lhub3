class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # special case
        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        # length is the distance between l and r
        # we need at least one balloon inside, so r - l >= 2
        for l in range(n-1,-1,-1):
            for r in range(l+2,n):
                #r = l + length
                best = 0

                for k in range(l + 1, r):
                    coins = dp[l][k] + arr[l] * arr[k] * arr[r] + dp[k][r]
                    best = max(best, coins)

                dp[l][r] = best

        return dp[0][n - 1]