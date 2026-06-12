class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorting will help us to skip a number that have been
        # already used at i-th position at specific permutation.
        nums.sort()
        ans = []
        def backtrack(i=0, solution=[]):
            
            ###MOST IMPOrtant STEP
            ##sol is added to final ans at EVERY CALL
            ans.append(solution)
            
            for j in range(i, len(nums)):
                # We can re-use numbers, but not at this position
                # and same previous premutation
                if j > i and nums[j] == nums[j-1]:
                    continue
                #solution.append(nums[j])
                backtrack(j+1, solution+[nums[j]])
                #solution.pop()
        backtrack()
        return ans