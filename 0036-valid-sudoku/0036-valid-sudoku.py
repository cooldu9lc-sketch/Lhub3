class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        ##box_id = rows//3 + cols//3

        for i,j in product(range(9),range(9)):
            if board[i][j]==".":
                continue
            val=board[i][j]
            box_id=(i//3)*3+j//3
            if val in rows[i] or val in cols[j] or val in boxes[box_id]:
                return False
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_id].add(val)
        return True