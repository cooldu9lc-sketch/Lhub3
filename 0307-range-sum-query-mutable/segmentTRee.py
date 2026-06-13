class NumArray:

    def __init__(self, nums: List[int]):
        self.seg=[0]*len(nums)+nums[:]
        self.n=len(nums)
        for i in range(self.n-1,0,-1):
            self.seg[i]=self.seg[i<<1]+self.seg[(i<<1)+1]
        

    def update(self, index: int, val: int) -> None:
        #update_value=val-self.seg[index+self.n]
        self.seg[index+self.n]=val
        p=index+self.n
        while p>1:
            self.seg[p>>1]=self.seg[p]+self.seg[p^1]
            p>>=1
            

    def sumRange(self, left: int, right: int) -> int:
        res=0
        l,r=left+self.n,right+self.n
        while l<=r:
            if l & 1:
                res+=self.seg[l]
                l+=1
            if r & 1==0:
                
                res+=self.seg[r]
                r-=1
            l>>=1
            r>>=1
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
