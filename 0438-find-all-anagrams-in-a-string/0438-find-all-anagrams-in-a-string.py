from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        count=0
        for end in range(ns):
            if s[end] in p_count:
                if p_count[s[end]]>0:
                    count+=1
                p_count[s[end]]-=1
            if end>=np:
                char=s[end-np]
                if char in p_count:
                    p_count[char]+=1
                if p_count[char]>0:
                    count-=1
            if count == np:
                output.append(end - np + 1)
        
        return output