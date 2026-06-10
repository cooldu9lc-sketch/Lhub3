class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G=defaultdict(set)
        visited = {} ## 1:current path 2:PRevious branch
        res=[]
        for u,v in prerequisites:
            G[v].add(u)
      
        def dfs(node):
            if node not in visited:
                visited[node]=1
            elif visited[node]==1:
                return False
            elif visited[node]==2:
                return True
            for neigh in G[node]:
                if not dfs(neigh):
                    return False
            visited[node]=2
            res.append(node)
            return True
            
        return res[::-1] if all([dfs(i) for i in range(numCourses)]) and len(res)==numCourses else []




     