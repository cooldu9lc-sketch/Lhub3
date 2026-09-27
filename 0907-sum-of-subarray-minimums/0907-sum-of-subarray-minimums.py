class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 10**9+7
        sums = 0
        arr.append(0) #Sentinel value to pop all elements off the stack
        stack = [-1]
        
        for i2,num in enumerate(arr):
	      #Mantain a monotone increasing stack
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]   #i1 is the nearest element to the left that is <= arr[index]
                left = index-i1 # left <=
                right = i2-index #right >
                sums += right*left*arr[index]
            stack.append(i2)
            
        return sums%M