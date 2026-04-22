class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()
            
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        queue.append((row,col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1