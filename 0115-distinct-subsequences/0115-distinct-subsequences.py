class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1 ## This is initialized to 1 (not i)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]
        """
        m,n=len(s),len(t)
        dp=[0]*(n+1) 
        
        for i in range(1,m+1):
            diag=1
            for j in range(1,n+1):
                next_diag=dp[j]
                if s[i-1]==t[j-1]:
                    dp[j]+=diag
                else:
                    dp[j]=dp[j]
                diag=next_diag
        return dp[-1]
        """