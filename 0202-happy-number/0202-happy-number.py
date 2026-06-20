class Solution:
    def isHappy(self, n: int) -> bool:
        def hap(x):
            return sum([int(i)*int(i) for i in str(x)])
        s=set()
        while n!=1:
            r=hap(n)
            if r in s:return False
            s.add(r)
            n=r
        return True