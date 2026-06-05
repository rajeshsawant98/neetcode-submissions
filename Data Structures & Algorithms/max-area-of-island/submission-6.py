class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        MaxA = 0
        visit = set()

        def bfs(r,c):
            A = 1
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            directions = [[-1,0], [1,0],[0,-1],[0,1]]

            while q:
                row, col = q.popleft()
                

                for dr,dc in directions:
                    r, c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        A += 1
                        q.append((r,c))
                        visit.add((r,c))
                
            return A

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    MaxA = max(MaxA, bfs(r,c))
        
        return MaxA
