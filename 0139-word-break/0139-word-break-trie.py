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
        ## Time complexity: O(n **2 +m *k) where n is the length of the string s,
        #  m is the number of words in the wordDict,
        # and k is the average length of the words in the wordDict
        #Building the trie involves iterating over all characters of all words. This costs O(m⋅k).
        ## Space complexity: The dp array takes O(n) space. The trie can have up to m⋅k nodes in it.


