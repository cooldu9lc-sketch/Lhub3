class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n
        back1,back2=2,1

        for i in range(3,n+1):
            curr = back1+back2
            back1,back2=curr,back1
        return back1