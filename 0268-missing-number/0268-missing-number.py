class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums) # Initialize with n
        for i, num in enumerate(nums):
            missing ^= i ^ num # XOR the index and the value
        return missing