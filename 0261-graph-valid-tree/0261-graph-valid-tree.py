class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        g= defaultdict(set)
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        
        visited = set()
        q= deque([0])
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                for neigh in g[node]:
                    if neigh not in visited:
                        q.append(neigh)
        return len(visited)==n