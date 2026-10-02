class SegmentTree:
        def __init__(self, size:int):
            self.l = size
            self.tree = [0]*(2*size)
            for i in range(self.l - 1, 0, -1):
                self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

        def update(self, index: int, val: int) -> None:
            n = self.l + index
            self.tree[n] = self.tree[n]+val
            while n > 1:
                self.tree[n>>1] = self.tree[n] + self.tree[n^1]
                n >>= 1

        def sumRange(self, left: int, right: int) -> int:
            m = self.l + left
            n = self.l + right
            res = 0
            while m <= n:
                if m & 1:
                    res += self.tree[m]
                    m += 1
                m >>= 1
                if n & 1 ==0:
                    res += self.tree[n]
                    n -= 1
                n >>= 1
            return res

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        values = sorted(set(nums))

        rank = {
            value: i
            for i, value in enumerate(values)
        }
        size = len(values)
        #offset=
        tree=SegmentTree(size)
        res=[]
        length=len(nums)
        for i in range(length-1,-1,-1):
            res.append(tree.sumRange(0,rank[nums[i]]-1))
            tree.update(rank[nums[i]],1)
        return res[::-1]
        