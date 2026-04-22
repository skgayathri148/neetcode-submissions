class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pac_res = [[False] * cols for _ in range(rows)]
        atl_res = [[False] * cols for _ in range(rows)]

        def bfs(source, result):
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                result[r][c] = True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and not result[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        queue.append((nr,nc))

        pac_src = []
        atl_src = []

        for c in range(cols):
            pac_src.append((0, c))
            atl_src.append((rows-1, c))

        for r in range(rows):
            pac_src.append((r, 0))
            atl_src.append((r, cols-1))

        bfs(pac_src, pac_res)
        bfs(atl_src, atl_res)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac_res[r][c] and atl_res[r][c]:
                    res.append([r,c])
        
        return res
