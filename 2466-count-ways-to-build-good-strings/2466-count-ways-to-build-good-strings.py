class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=10**9+7
        res=0
        dp = [0] * (high+1)
        dp[0] = 1

        for i in range(1,high+1):
            if i-zero>=0:
                dp[i]+=dp[i-zero]
            if i-one>=0:
                dp[i]+=dp[i-one]
            if i>=low:
                res=(res+dp[i])%MOD
        return res