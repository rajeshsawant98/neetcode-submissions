class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        MaxA = 0
        

        def bfs(r,c):
            A = 1
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                directions = [[-1,0], [1,0],[0,-1],[0,1]]

                for dr,dc in directions:
                    r, c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 :
                        A += 1
                        q.append((r,c))
                        grid[r][c] = 0
                
            return A

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 :
                    MaxA = max(MaxA, bfs(r,c))
        
        return MaxA
