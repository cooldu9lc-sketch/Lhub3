class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:return x

        left,right=1,x+1
        while left<right:
            mid = (left+ right)//2
            if mid*mid>x:
                right=mid
            else:
                left=mid+1
        return left-1  