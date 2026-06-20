class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        stack = deque([])
        res = []

        for i,num in enumerate(nums):
            while stack and nums[stack[-1]]<=num:
                stack.pop()
            stack.append(i)
            if i<k-1:continue
            res.append(nums[stack[0]])
            if stack[0]==i-k+1: ##if window size is K , reduce it by one for next iteration
                stack.popleft()
        return res
