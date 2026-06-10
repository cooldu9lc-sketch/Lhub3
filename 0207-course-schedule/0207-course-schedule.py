class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G=defaultdict(set)
        ind=defaultdict(int)
        for u,v in prerequisites:
            #G[u].add(v)
            G[v].add(u)
            ind[u]+=1
        q=[course for course in range(numCourses) if ind[course]==0]
        q=deque(q)
        taken=0
        while q:
            node=q.popleft()
            taken+=1
            for neigh in G[node]:
                ind[neigh]-=1
                if ind[neigh]==0:
                    q.append(neigh)
        return taken==numCourses