class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(res):
            count,s=1,0
            for num in nums:
                if s+num<=res:
                    s+=num
                else:
                    count+=1
                    if count>k:return False
                    s=num
            return count<=k

        left,right=max(nums),sum(nums)
        while left<right:
            mid = (left+right)//2
            if isPossible(mid):
                right=mid
            else:
                left=mid+1
        return left