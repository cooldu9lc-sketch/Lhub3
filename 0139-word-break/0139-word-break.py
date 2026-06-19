class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n=len(s)
        wordset = set(wordDict)

        dp = [False]*(n+1)

        dp[0]=True

        for end in range(1,n+1):
            for start in range(end):
                if  dp[start] and s[start:end] in wordset:
                    dp[end]=True
                    break
        return dp[-1]