class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        res=[]
        def recur(curr):
            if len(curr)==len(nums):
                res.append(curr[:])
            for num in count:
                if count[num]:
                    count[num]-=1
                    recur(curr+[num])
                    count[num]+=1
        recur([])
        return res