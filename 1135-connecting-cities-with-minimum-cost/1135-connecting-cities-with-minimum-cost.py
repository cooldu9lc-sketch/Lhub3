class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        
      
        if len(connections) < n-1:
            return -1
        
        parent={i:i for i in range(1,n+1)}
        size={i:1 for i in range(1,n+1)}

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        ans=0
        
        for u,v,w in sorted(connections,key=lambda x:(x[2],x)):
            pu,pv=find(u),find(v)
            if pu!=pv:
                if size[pu]>=size[pv]:
                    parent[pv]=pu
                    size[pu]+=size[pv]
                else:
                    parent[pu]=pv
                    size[pv]+=size[pu]
                ans+=w
              
        return ans if size[find(1)]==n else -1
        
        
        
        
        
    