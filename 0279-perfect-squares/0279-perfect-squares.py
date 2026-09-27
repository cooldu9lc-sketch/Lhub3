class Solution:
    def numSquares(self, n: int) -> int:
        if n==0:return 0
        dp=[0]+[float("inf")]*n
        coins=[i*i for i in range(int(n**0.5+1)+1)]
        for i in range(1,n+1):
            for c in coins:
                if i>=c:
                    dp[i]=min(dp[i],dp[i-c]+1)
        return dp[-1] if dp[-1]!=float("inf") else -1