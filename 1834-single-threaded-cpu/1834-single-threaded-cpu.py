class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted((t[0], t[1], i) for i, t in enumerate(tasks))

        i = 0
        heap = []
        time = 0

        while len(res) < len(tasks):

            if not heap and i < len(tasks):
                time = max(time, tasks[i][0])

            # Add all tasks that have arrived
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            # Execute shortest available task
            if heap:
                process_time, original_index = heapq.heappop(heap)
                time += process_time
                res.append(original_index)

        return res