class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftCursor, rightCursor = 0, len(height)-1
        leftMax, rightMax, storedWater = 0, 0, 0
        
        while (leftCursor <= rightCursor):
            leftMax = max(leftMax, height[leftCursor])
            rightMax = max(rightMax, height[rightCursor])
            if leftMax < rightMax:
                storedWater += leftMax - height[leftCursor]
                leftCursor += 1
            else:
                storedWater += rightMax - height[rightCursor]
                rightCursor -= 1
                
        return storedWater