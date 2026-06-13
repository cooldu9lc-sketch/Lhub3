class Bit:
    def __init__(self,size):
        self.bit=[0]*(size+1)
    
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


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix[:]
        self.m=len(matrix)
        self.n=len(matrix[0])
        self.tree= Bit(self.m*self.n)
        for i in range(self.m):
            for j in range(self.n):
                idx= i*self.n+j+1
                self.tree.addValue(idx,matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        update_val=val-self.matrix[row][col]
        update_idx=row*self.n+col+1
        self.tree.addValue(update_idx,update_val)
        self.matrix[row][col]=val

    def getSum(self,row,col):
        idx=row*self.n+col+1
        return self.tree.query(idx)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s=0
        for r in range(row1,row2+1):
            s+=self.getSum(r,col2)-self.getSum(r,col1-1)
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
