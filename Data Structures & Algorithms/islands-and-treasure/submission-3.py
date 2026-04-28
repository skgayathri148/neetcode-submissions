class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = set()
            visit.add((r, c))
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (
                            0 <= nr < ROWS and 0 <= nc < COLS
                            and (nr, nc) not in visit and grid[nr][nc] != -1
                        ):
                            visit.add((nr, nc))
                            q.append((nr, nc))
                steps += 1
            return INF
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)