class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m,n = len(board),len(board[0])
        trie=lambda:defaultdict(trie)
        root=trie()
        res=[]
        for word in words:
            reduce(dict.__getitem__,word,root)["#"]=word

        def dfs(i,j,parent):
            if board[i][j] not in parent:
                return 
            char=board[i][j]
            node=parent[char]
            board[i][j]="*"
            if "#" in node:
                res.append(node.pop("#"))
            for dx,dy in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=dx<m and 0<=dy<n and dfs(dx,dy,node):
                    pass
            board[i][j]=char
            return
        for i,j in product(range(m),range(n)):
            dfs(i,j,root)
        return res

            
            
            

            