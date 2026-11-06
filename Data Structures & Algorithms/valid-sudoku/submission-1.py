class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validate3x3matrix(board,rc,cc):
            seen=[]
            for r in range (rc,rc+3):
                for c in range (cc,cc+3):
                    if board[r][c] in seen and board[r][c] != '.':
                        return False
                    else:
                        seen.append(board[r][c])
            return True

        def vaidateAllRows(board):
            for cc in range(0,9):
                row=[]
                for rc in range(0,9):
                    if board[rc][cc] in row and board[rc][cc] != '.':
                        return False
                    else:
                        row.append(board[rc][cc])
            return True

        def validateAllColumns(board):
            for rc in range(0,9):
                col=[]
                for cc in range(0,9):
                    if board[rc][cc] in col and board[rc][cc] != '.':
                        return False
                    else:
                        col.append(board[rc][cc])
            return True

        if not (vaidateAllRows(board)):
            return False
        if not (validateAllColumns(board)):
            return False
        for rc in range (0,9,3):
            for cc in range (0,9,3):
                if not (validate3x3matrix(board,rc,cc)):
                    return False
        return True
        