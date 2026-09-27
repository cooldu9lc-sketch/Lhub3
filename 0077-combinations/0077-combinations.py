class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(pos = 1, curr = []):
           ####
        ###The terminating condition is DEPENDENT ONLY ON the size of output, not on i
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(pos, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output