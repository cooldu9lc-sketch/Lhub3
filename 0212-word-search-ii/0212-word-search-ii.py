class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie=lambda:defaultdict(trie)
        root=head=trie()
        for word in words:
            reduce(dict.__getitem__,word,root)["#"]=word
            """node=root
            for char in word:
                node=node[char]
            node["#"]=word"""
        res=[]
        
        def dfs(i,j,parent):
            #print(i,j)
            char = board[i][j]
            curr= parent[char]
            board[i][j]="$"
            #wordm = curr.pop("#",None)
            if "#" in curr:
                res.append(curr["#"])
                del curr["#"]
            
            for dx,dy in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if dx<0 or dx>=m or dy<0 or dy>=n:
                    continue
                if board[dx][dy] in curr:
                    dfs(dx,dy,curr)
            
            board[i][j]=char
            if len(curr)==0:
                del parent[char] ##PRUNING
        
        m,n=len(board),len(board[0])
        for r,c in product(range(m),range(n)):
            if board[r][c] in root:
                dfs(r,c,root)

        return res