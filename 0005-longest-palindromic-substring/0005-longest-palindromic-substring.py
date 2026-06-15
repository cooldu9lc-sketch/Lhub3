class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(s,l,r):
            while l >=0 and r < len(s) and s[l] ==s[r]:
                l -= 1
                r += 1

            if self.maxlen < r-l-1:
                self.maxlen = r-l-1
                self.start = l + 1
        self.maxlen = 0
        self.start = 0
        for i in range(len(s)):
            expandFromCenter(s,i,i)
            expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxlen]
    