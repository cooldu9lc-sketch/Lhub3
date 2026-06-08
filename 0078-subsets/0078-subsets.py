class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def recur(i=0,curr=[]):
            res.append(curr)


            for j in range(i,len(nums)):
                recur(j+1,curr+[nums[j]])

        recur()
        return res