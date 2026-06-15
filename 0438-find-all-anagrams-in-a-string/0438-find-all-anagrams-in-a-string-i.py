class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):return []

        pcount=Counter(p)
        scount=Counter(s)
        if pcount>scount:return []
        curr=Counter()
        res=[]
        for i in range(len(s)):
            curr[s[i]]+=1
            if i<len(p)-1:continue
            if i>=len(p):curr[s[i-len(p)]]-=1
            if curr==pcount:
                res.append(i-len(p)+1)
        return res
