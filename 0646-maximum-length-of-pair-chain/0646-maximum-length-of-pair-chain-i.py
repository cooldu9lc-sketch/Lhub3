class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        end=pairs[0][1]
        res=1
        for s,e in pairs:
           if s>end:
               res+=1
               end=e
        return res