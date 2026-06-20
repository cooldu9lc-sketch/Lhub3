class Solution:
    def countSubstrings(self, s: str) -> int:


        def expandFromCenter(s,l,r):
            ans=0
            while l >=0 and r < len(s) and s[l] ==s[r]:
                l -= 1
                r += 1
                ans+=1
            return ans
                
        return sum(expandFromCenter(s,i,i)+expandFromCenter(s,i,i+1)  for i in range(len(s)))       
        