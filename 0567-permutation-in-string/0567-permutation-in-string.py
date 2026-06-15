class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False

        pcount=Counter(s1)
        scount=Counter(s2)
        if pcount>scount:return False
        curr=Counter()
        for i in range(len(s2)):
            curr[s2[i]]+=1
            if i>=len(s1):curr[s2[i-len(s1)]]-=1
            if curr==pcount:
                return True
        return curr==pcount