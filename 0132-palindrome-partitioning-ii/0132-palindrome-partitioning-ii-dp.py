class Solution:
    def minCut(self, s: str) -> int:
        
        def findcut(start,end,i):
            while start>=0 and end<len(s) and s[start]==s[end]:
                dp[end]=min(dp[end],dp[start-1]+1)
                start-=1
                end+=1
        
        
        dp=[i for i in range(len(s))]+[-1]
        for i in range(len(s)):
            findcut(i,i,i)
            findcut(i-1,i,i)
        return dp[len(s)-1]

       
