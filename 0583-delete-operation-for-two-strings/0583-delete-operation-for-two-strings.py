class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
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
        return recur(0,0)  

