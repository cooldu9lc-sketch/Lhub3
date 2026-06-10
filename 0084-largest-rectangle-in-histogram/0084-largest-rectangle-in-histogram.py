class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(float("-inf"))

        res = 0 

        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
               l = heights[stack.pop()]
               res= max(res,l*  (i-stack[-1]-1))
            stack.append(i)
        return res 