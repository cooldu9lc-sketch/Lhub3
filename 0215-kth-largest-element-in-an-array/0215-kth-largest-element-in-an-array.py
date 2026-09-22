class Solution:
    def findKthLargest(self, nums, k):
        target_idx = len(nums) - k  # Convert k-th largest to index from left
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if lt <= target_idx <= gt:
                return nums[target_idx]
            elif target_idx < lt:
                right = lt - 1
            else:
                left = gt + 1

        return -1