class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(i,j,m,n):
            if i<=0 or i>=m-1 or j<=0 or j>=n-1 or board[i][j]!="O":
                return 
            board[i][j]="#"
            dfs(i+1,j,m,n)
            dfs(i-1,j,m,n)
            dfs(i,j+1,m,n)
            dfs(i,j-1,m,n)
        
        
        m,n=len(board),len(board[0])
        for i in range(n):
            if board[0][i]=="O":
                dfs(1,i,m,n)
            if m!=1 and board[m-1][i]=="O":
                dfs(m-2,i,m,n)
            
        for i in range(m):
            if board[i][0]=="O":
                dfs(i,1,m,n)
            if n!=1 and board[i][n-1]=="O":
                dfs(i,n-2,m,n)
                
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="#":
                    board[i][j]="O"
        
                
        
            