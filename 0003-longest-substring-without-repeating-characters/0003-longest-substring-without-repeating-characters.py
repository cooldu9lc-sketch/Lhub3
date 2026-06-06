class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        left=0
        res=0
        for right,char in enumerate(s):
            if char in d:
                left=max(left,d[char]+1)
            res=max(res,right-left+1)
            ### SIZE OF LARGEST WINDOW IS BEING UPDATED AT THE END OF EACH ITERARTION. #c   #   HENCE WE CAN REDUCE THE LEFT INDEX OF THE WINDOW aka left element at the  #        beggining of the iteration under the if condition
            d[char]=right
        return res