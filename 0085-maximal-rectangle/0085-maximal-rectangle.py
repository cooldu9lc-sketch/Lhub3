class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def area(heights):
            heights.append(0)
            stack = [-1]
            ans = 0
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
            heights.pop()
            return ans
        
        m,n=len(matrix),len(matrix[0])
        dp=[0]*n
        res=0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]=="1":
                    dp[col]+=1
                else:
                    dp[col]=0
            res=max(res,area(dp))
        return res
            