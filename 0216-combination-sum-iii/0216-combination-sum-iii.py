class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if k>n:return []
        res=[]
        def recur(count=0,total=0,comb=[],j=1):
            if count==k:
                if total==n:
                    res.append(comb[:])
                return
            if total>=n:
                return
            for i in range(j,10):
                recur(count+1,total+i,comb+[i],i+1)
        recur()
        return res
