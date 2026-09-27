class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}

        stack = []

        for x in nums2:

            while stack and stack[-1] < x:
                smaller = stack.pop()
                next_greater[smaller] = x

            stack.append(x)

        return [
            next_greater.get(x, -1)
            for x in nums1
        ]
        