class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        ans=[]

        def backtrack(i=0,s=0,curr=[]):
            if s==target:
                ans.append(curr)
                return
            if i==len(candidates) or s>target:return

            
            backtrack(i,s+candidates[i],curr+[candidates[i]])
            backtrack(i+1,s,curr)


        backtrack()
        return ans