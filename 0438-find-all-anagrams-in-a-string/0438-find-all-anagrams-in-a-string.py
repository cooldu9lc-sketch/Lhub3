from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        """
        ## you always add the character even if the count becomes negative because
        ## when you're removing the character from window , there can be 2 cases
        ## the count of s[end-np] character is positive in which case we know that it was included in the window but if is zero we cannot tell  in which iteration the  count[s] was made zero. So we always make sure to to take all keys of p
        and the count of an element if it's above zero or below zero tells us if its' part of the window
        """
        
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