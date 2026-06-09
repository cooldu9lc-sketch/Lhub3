class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(x):
            return sum(math.ceil(i/x) for i in piles)<=h

        left,right=1,max(piles)
        while left<right:
            mid=(left+right)>>1
            if possible(mid):
                right=mid
            else:
                left=mid+1
        return left