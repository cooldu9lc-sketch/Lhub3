class Bit:
    #### Constructing fenwick tree in O(N) time
    def __init__(self,nums):
        self.bit=[0] + nums[:]
        n=len(self.bit)
        for i in range(1,n):
            j=i+ (i&-i)
            if j<n:
                self.bit[j]+=self.bit[i]
    
    def addValue(self,idx,value):
        while idx<len(self.bit):
            self.bit[idx]+=value
            idx+= idx&(-idx)
        
    def query(self,idx):
        s=0
        while idx>0:
            s+=self.bit[idx]
            idx-= idx&(-idx)
        return s

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums[:]
        self.tree=Bit(nums)

    def update(self, index: int, val: int) -> None:
        update_val=val-self.nums[index]
        self.tree.addValue(index+1,update_val)
        self.nums[index]=val        

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right+1)-self.tree.query(left)
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)