class Solution:
    def isValid(self, s: str) -> bool:

        d={
            "}":"{",
            "]":"[",
            ")":"("
        }
        if len(s)%2!=0:return False
        stack=[]
        for char in s:
            if char in d:
                if not stack or stack[-1]!=d[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack)==0