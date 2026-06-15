class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0 
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r ,c = row + dr , col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c]== 1 and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
                        area += 1

            return area 

                

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxA = max(maxA,bfs(r,c))

        return maxA