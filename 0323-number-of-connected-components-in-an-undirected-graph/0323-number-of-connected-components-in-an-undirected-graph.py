class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #visited={}
        # 0-> Not visited
        # 1-> visited
        #2-> current
        visited=set()
        G=defaultdict(set)
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        def dfs(val):
            if val not in visited:
                visited.add(val)
                for neigh in G[val]:
                    dfs(neigh)
                
        res=0
        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i)

        return res
        