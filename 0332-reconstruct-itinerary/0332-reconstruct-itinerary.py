class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G=defaultdict(list)
        for u,v in tickets:
            G[u].append(v)
        for u,v in tickets:
            G[u].sort(reverse=True)
        
      
        def dfs(node):
            #res.append(node)
            while len(G[node]):
                neigh = G[node].pop()
                dfs(neigh)
            res.append(node)

        res=[]
        dfs("JFK")
        return res[::-1]
