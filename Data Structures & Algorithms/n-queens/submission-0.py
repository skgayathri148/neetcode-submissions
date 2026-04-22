class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]

        def recursive (row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for col in range(n):
                if self.is_safe(row, col, board):
                    board[row][col] = 'Q'
                    recursive(row + 1)
                    board[row][col] = '.'

        recursive(0)
        return res

    def is_safe(self, r, c, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == 'Q':
                return False
            row -= 1
        
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == 'Q':
                return False
            row -= 1
            col += 1

        return True
