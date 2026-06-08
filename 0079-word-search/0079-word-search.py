class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ## i is the index for the char to be matched in word
        ## r,c are board position of char matched at word[i-1] 
        def backtrack(i,r,c):
            
            char=board[r][c]
            board[r][c]="#"
            ret=False
            for dx,dy in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=dx<m and 0<=dy<n and board[dx][dy]==word[i]:
                    if i==len(word)-1 or backtrack(i+1,dx,dy):
                        ret=True
                        break
            board[r][c]=char   
            return ret
        
        m,n=len(board),len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y]==word[0]:
                    if len(word)==1 or backtrack(1,x,y):
                        return True
        return False