class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n<=2:
            return k**n
        two_back,one_back=k,k*k
        for i in range(3,n+1):
            curr=(k-1)*(two_back+one_back)
            one_back,two_back=curr,one_back
        return one_back