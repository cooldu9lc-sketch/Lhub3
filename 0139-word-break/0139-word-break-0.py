class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]
        ## Time complexity: O(n * m * k) where n is the length of the string s,
        #  m is the number of words in the wordDict, 
        # and k is the average length of the words in the wordDict
        ## Space complexity: O(n) where n is the length of the string s
