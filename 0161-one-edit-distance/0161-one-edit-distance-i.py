class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            s,t=t,s
        if len(t)-len(s)>1:
            return False
        edited=False
        i=j=0
        while i<len(s):
            if s[i]==t[j]:
                i+=1
                j+=1
                continue
            if edited:
                return False
            edited=True
            if len(s)==len(t):
                i+=1
                j+=1
            else:
                j+=1
        ### The return condition makes sure that the edit distance=1 and not zero i.e s!=t

        return (j==len(t)-1 and not edited) or (j==len(t) and edited) or (len(s)==len(t) and edited)
