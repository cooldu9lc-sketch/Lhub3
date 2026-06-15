class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def recur(l=0,r=0,curr=[]):
            if l==r==n:
                res.append("".join(curr))
            if l<n:
                recur(l+1,r,curr+["("])
            if r<l:
                recur(l,r+1,curr+[")"])
        recur()
        return res