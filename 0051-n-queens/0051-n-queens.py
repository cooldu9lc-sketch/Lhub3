class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        self.ans=[]
        #rows=set()
        cols=set()
        diags=set()
        antis=set()
        
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def backtrack(row):
            if row==n:
                self.ans.append(create_board(board))
                return
            #rows.add(row)
            for col in range(n):
                diag=row-col
                anti=row+col
                if col not in cols and diag not in diags and anti not in antis:
                    cols.add(col)
                    diags.add(diag)
                    antis.add(anti)
                    board[row][col]="Q"
                    backtrack(row+1)
                    cols.remove(col)
                    diags.remove(diag)
                    antis.remove(anti)
                    board[row][col]="."
            #rows.remove(row)
        backtrack(0)
        return self.ans
