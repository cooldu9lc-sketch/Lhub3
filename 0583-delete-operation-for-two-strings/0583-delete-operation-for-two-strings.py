class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """@cache
        def recur(i,j):
            res= float("inf")
            if i==len(word1) and j==len(word2):
                return 0
            if i==len(word1):
                return len(word2)-j
            elif j==len(word2):
                return len(word1)-i
            elif word1[i]==word2[j]:
                res= recur(i+1,j+1)
            res= min(res,recur(i+1,j)+1,recur(i,j+1)+1)
            return res  
        return recur(0,0)  """
        m,n=len(word1),len(word2)
        if m==0 or n==0:
            return max(m,n)
        dp=[[float("inf")]*(n+1) for _ in range(m+1)]
        dp[0][0]=0
        for j in range(1,n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            dp[i][0]=i
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=min(dp[i][j],dp[i-1][j-1])
                else:
                    dp[i][j]=min(dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[-1][-1]
