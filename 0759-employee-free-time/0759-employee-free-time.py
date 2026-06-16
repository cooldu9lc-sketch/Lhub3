"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        OPEN, CLOSE = 1, 2
        events = []
        
        for lst in schedule:
            for interv in lst:
                events.append((interv.start, OPEN))
                events.append((interv.end, CLOSE))
        
        balance = 0
        events.sort()
        ans = []
        prev = None
        
        for time, eventType in events:
            if balance == 0 and prev is not None:
                ans.append(Interval(prev, time))
            balance+= 1 if eventType ==OPEN else -1
            
            if balance == 0:
                prev = time
        
        return ans