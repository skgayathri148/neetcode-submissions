class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def capture():
            queue = deque()
            for r in range(rows):
                for c in range(cols):
                    if (
                        r == 0 or r == rows - 1 or
                        c == 0 or c == cols - 1 and
                        board[r][c] == "O"
                    ):
                        queue.append((r,c))

            while queue:
                r, c = queue.popleft()
                if board[r][c] == "O":
                    board[r][c] = "#"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            queue.append((nr, nc))
        
        capture()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"