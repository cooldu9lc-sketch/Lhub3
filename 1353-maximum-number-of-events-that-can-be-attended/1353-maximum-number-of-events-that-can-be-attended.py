import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()

        heap = []
        i = 0
        day = 0
        attended = 0

        while i < len(events) or heap:

            if not heap:
                day = events[i][0]

            # Add all events that have started
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove expired events
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # Attend event ending earliest
            if heap:
                heapq.heappop(heap)
                attended += 1
                day += 1

        return attended
