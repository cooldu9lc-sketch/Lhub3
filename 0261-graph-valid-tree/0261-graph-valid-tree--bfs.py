class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n==1:return True
        if len(edges)!=n-1:return False
        
        g=defaultdict(set)
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)

        visited=set()
        def dfs(node,parent):
            if node in visited:
                return  False
            visited.add(node)
            for neigh in g[node]:
                if neigh==parent:continue
                if not dfs(neigh,node):
                    return False
            #visited.add(node)
            return True

        return dfs(0,-1) and len(visited)==n