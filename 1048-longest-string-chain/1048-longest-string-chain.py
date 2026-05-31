class Solution:
    def longestStrChain(self, words: List[str]) -> int:
  
        dp = defaultdict(int)
        result = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]

                if pred in dp and dp[pred]+1 > dp[word]:
                    dp[word] = dp[pred] + 1
                    result = max(result, dp[word])

        return result