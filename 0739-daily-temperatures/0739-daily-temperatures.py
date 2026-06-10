class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
               idx=stack.pop()
               ans[idx]=i-idx
            stack.append(i)
        return ans