class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #low keeps tarck of the lowest index of the chars currently in window
        start=res=0
        d={}
        for i,c in enumerate(s):
            if c not in d and len(d)==2:
                while d[s[start]]!=start:
                    start+=1
                del d[s[start]]
                start+=1
            d[c]=i
            res=max(res,i-start+1)
        return res