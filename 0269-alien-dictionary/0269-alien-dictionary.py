class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        g=defaultdict(set)
        ind=defaultdict(int)
        
        all_chars = set()
        for word in words:
            all_chars|=set(word)
        
        for w1,w2 in zip(words,words[1:]):
            for c1,c2 in zip(w1,w2):
                if c1!=c2:
                    if c2 not in g[c1]:
                        g[c1].add(c2)
                        ind[c2]+=1
                    break
            else:
            
                if len(w1)>len(w2):return ""
        
        q=deque([char for char in all_chars if ind[char]==0])
        res=[]
        #print(all_chars)
        #print(q)
        while q:
            
            char = q.popleft()
            res.append(char)
            for neigh in g[char]:
                ind[neigh]-=1
                if ind[neigh]==0:
                    q.append(neigh)
        return "".join(res) if len(res)==len(all_chars) else ""
        