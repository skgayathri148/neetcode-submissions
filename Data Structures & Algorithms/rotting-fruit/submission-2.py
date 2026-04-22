class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        visit = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r,c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            time += 1

        
        return time if fresh == 0 else -1
