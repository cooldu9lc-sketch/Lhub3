class MaxBIT:  # One-based indexing
    def __init__(self, size):
        self.bit = [0] * (size + 1)
    def get(self, idx):
        ans = 0
        while idx > 0:
            ans = max(ans, self.bit[idx])
            idx -= idx & (-idx)
        return ans
    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & (-idx)

class Solution:  # 360 ms, faster than 69.28%
    def lengthOfLIS(self, nums: List[int]) -> int:
        bit = MaxBIT(20001)
        BASE = 10001
        for x in nums:
            subLongest = bit.get(BASE + x - 1)
            bit.update(BASE + x, subLongest + 1)
        return bit.get(20001)