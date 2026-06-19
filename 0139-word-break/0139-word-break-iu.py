class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        trie = lambda : defaultdict(trie)
        root=trie()
        
        for word in wordDict:
            reduce(dict.__getitem__,word,root)["#"] = True 
        
        
        dp = [False]*(len(s))

      

        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, len(s)):
                    if s[j] in curr:
                        curr= curr[s[j]]
                        if "#" in curr:dp[j]=True
                    else:
                        break

        return dp[-1]