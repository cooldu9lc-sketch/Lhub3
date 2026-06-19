class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        ##sort tasks by their start time
        tasks_sorted=sorted(enumerate(tasks),key=lambda x:x[1])
        heap,res=[],[]
        n=len(tasks)
        i=time=0
        while heap or i<n:
            
            while i<n and tasks_sorted[i][1][0]<=time:
                idx,(eqt,pt)=tasks_sorted[i]
                heapq.heappush(heap,(pt,idx))
                i+=1
            if not heap:###no tasks are available. Spo process the next available task
                idx,(eqt,pt)=tasks_sorted[i]
                res.append(idx)
                time=eqt+pt
                i+=1
            else:
                pt,idx=heapq.heappop(heap)
                res.append(idx)
                time+=pt
        return res