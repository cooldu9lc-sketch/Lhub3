class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n<=2:
            return k**n
        a,b=k,k*k
        for i in range(3,n+1):
            curr=(k-1)*(a+b)
            a,b=b,curr
        return b