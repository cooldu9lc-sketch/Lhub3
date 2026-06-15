class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if m>n:return False
        s1_count=collections.Counter(s1)
        #s2_count=collections.Counter()
        count=0
        for end in range(n):
            if s2[end] in s1_count:
                if s1_count[s2[end]]>0:
                    count+=1
                s1_count[s2[end]]-=1
            if end>=m:
                char=s2[end-m]
                if char in s1_count:
                    s1_count[char]+=1
                if s1_count[char]>0:
                    count-=1
                
            if count==m:
                return True
        return False
