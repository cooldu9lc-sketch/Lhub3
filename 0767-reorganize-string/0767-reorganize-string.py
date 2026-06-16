class Solution:
    def reorganizeString(self, s: str) -> str:
        s=list(s)
        n=len(s)
        count = Counter(s)
        s.sort(key=lambda x: (count[x],x))

        if count[s[-1]]>(n+1)//2:return ""
        res= [""]*n
        for i in range(0,n,2):
            res[i]=s.pop()
        for i in range(1,n,2):
            res[i]=s.pop()
        return "".join(res)        
