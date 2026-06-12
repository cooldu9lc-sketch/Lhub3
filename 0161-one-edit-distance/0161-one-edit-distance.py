class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        replace=(len(s)==len(t))
        insert= (len(s)+1==len(t))
        delete= (len(s)-1==len(t))
        if not any([replace,insert,delete]):
            return False
        op=i=j=0
        while i<len(s) and j<len(t):
            if s[i]!=t[j]:
                if op:return False
                if replace:
                    op+=1
                    i+=1
                    j+=1
                    continue
                elif insert:
                    j+=1
                    op+=1
                elif delete:
                    i+=1
                    op+=1
            else:    
                i+=1
                j+=1
        ### The return condition makes sure that the edit distance=1 and not zero i.e s!=t
        return  op==1 or(i==len(s)-1 and j==len(t)) or (i==len(s) and j==len(t)-1)