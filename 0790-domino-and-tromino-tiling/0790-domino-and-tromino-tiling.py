class Solution:
    def numTilings(self, n: int) -> int:
        
        ## f(k) = 2* f(k-1)+f(k-3)

        if n<=2:
            return n
        MOD = (10**9)+7

        dp=[0]*(n+1)
        dp[0],dp[1],dp[2]=1,1,2

        for i in range(3,n+1):
            dp[i] = (2*dp[i-1]+ dp[i-3])%MOD

        return dp[n]