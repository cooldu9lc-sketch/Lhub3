"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res
