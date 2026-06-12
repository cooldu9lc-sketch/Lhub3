class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m,n=len(word1),len(word2)
        if m==0 or n==0:
            return max(m,n)
        dp= list(range(n+1))
        for i in range(1,m+1):
            dp[0]= i
            diag=i-1
            for j in range(1,n+1):
                next_diag =dp[j]
                dp[j]=min(dp[j]+1,dp[j-1]+1,diag+int(word1[i-1]!=word2[j-1]))
                diag=next_diag
        return dp[n]
        
        
        
        """m,n=len(word1),len(word2)
        if m==0 or n==0:
            return max(m,n)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for j in range(1,n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            dp[i][0]=i
            for j in range(1,n+1):
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+int(word1[i-1]!=word2[j-1]))
        return dp[m][n]"""