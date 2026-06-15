class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0

        for i,num in enumerate(nums):
            if maxi<i:
                return False
            maxi=max(maxi,i+num)
        return True