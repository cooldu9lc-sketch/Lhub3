class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G=defaultdict(set)
        ind=defaultdict(int)
        for u,v in prerequisites:
            G[v].add(u)
            ind[u]+=1
        q=[course for course in range(numCourses) if ind[course]==0]
        q=deque(q)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for neigh in G[node]:
                ind[neigh]-=1
                if ind[neigh]==0:
                    q.append(neigh)
        return res if len(res)==numCourses else []