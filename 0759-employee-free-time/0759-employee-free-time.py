"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
         # idea: similar like merge interval + merge k lists
        #       put the first interval, employee idx and interval idx in a heap
        #       if next interval is not overlapping, calc the gap and save in result
        #       take the next interval and repeat merging.
        
        min_heap, res = [], []
        
        for i in range(len(schedule)):
            # the last elem in tuple is next idx of interval for the employee
            heapq.heappush(min_heap, (schedule[i][0].start, schedule[i][0].end, i, 1))
        
        end = min_heap[0][1]
        
        while min_heap:
            new_start, new_end, i, j = heapq.heappop(min_heap)
            if new_start <= end:
                end = max(end, new_end)
            else:
                res.append(Interval(end, new_start))
                end = new_end
            if j < len(schedule[i]):
                heapq.heappush(min_heap, (schedule[i][j].start, schedule[i][j].end, i, j+1))
        
        return res