class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:return "0"
        n=abs(num)
        res=[]
        while n>0:
            rem=n%7
            n=n//7
            res.append(rem)
        return "".join(str(i) for i in res[::-1]) if num>=0 else "-"+ "".join(str(i) for i in res[::-1]) 