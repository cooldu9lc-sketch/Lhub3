class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        
      
        if len(connections) < n-1:
            return -1
        
        parent={i:i for i in range(1,n+1)}
        rank={i:1 for i in range(1,n+1)}

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        ans=0
        connected=0
        
        for u,v,w in sorted(connections,key=lambda x:(x[2],x)):
            pu,pv=find(u),find(v)
            if pu!=pv:
                if rank[pu]>rank[pv]:
                    parent[pv]=pu
                elif rank[pv]>rank[pu]:
                    parent[pu]=pv
                else:
                    parent[pv]=pu
                    rank[u]+=1
                ans+=w
                connected+=1
                if connected==n-1:
                    return ans
              
        return ans if all(find(i)==find(1) for i in range(2,n+1)) else -1
        
        
        
        
    