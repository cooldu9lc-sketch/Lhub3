class Solution:
    def numTilings(self, n: int) -> int:
    

        MOD = 10**9 + 7

        full = [0]*(n+1)
        gap = [0]*(n+1)

        ##f(i): The number of ways to fully cover a board of width i
        ##g(i): The number of ways to partially cover a board of width i

        full[0] = 1
        full[1] = 1

        for i in range(2,n+1):

            full[i] = (
                full[i-1]
                + full[i-2]
                + 2*gap[i-1]
            ) % MOD

            gap[i] = (
                gap[i-1]
                + full[i-2]
            ) % MOD

        return full[n]
