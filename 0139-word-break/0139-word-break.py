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

        ## Time complexity: O(n^2 * k) where n is the length of the string s and k is the average length of the words in the wordDict. The outer loop runs n times, and for each end index, we check all possible start indices, which takes O(n) time. Checking if a substring is in the wordDict takes O(k) time on average.
        ## Space complexity: O(n + m * k) where n is the length of the