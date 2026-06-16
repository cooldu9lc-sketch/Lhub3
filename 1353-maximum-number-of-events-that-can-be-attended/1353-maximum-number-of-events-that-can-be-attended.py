class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key=lambda x: (x[0],x[1]))

        heap = [] #endtimes

        res = idx = 0

        current_time =  events[0][0]

        while heap or idx<len(events):
            while idx<len(events) and events[idx][0]==current_time:
                heappush(heap,events[idx][1])
                idx+=1
            while heap and heap[0]<current_time:
                heappop(heap)
            
            if heap:
                heappop(heap)
                res+=1
                current_time+=1
                continue
            elif idx<len(events):
                current_time = events[idx][0]
        return res