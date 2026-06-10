class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G=defaultdict(set)
        visited = {} ## 1:current path 2:PRevious branch
        for u,v in prerequisites:
            #G[u].add(v)
            G[v].add(u)
      
        def dfs(node):
            if node not in visited:
                visited[node]=1
            elif node in visited and visited[node]==1:
                return False
            elif visited[node]==2:
                return True
            for neigh in G[node]:
                if not dfs(neigh):
                    return False
            visited[node]=2
            return True
            
            



        return all([dfs(i) for i in range(1,numCourses)])




     