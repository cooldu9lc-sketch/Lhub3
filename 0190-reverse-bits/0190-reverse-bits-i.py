class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            bit= n&1
            res+= (bit<<(31-i))
            n= n>>1
        return res
        
        """ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret"""