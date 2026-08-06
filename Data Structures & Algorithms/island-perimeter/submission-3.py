class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        total = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            perimeter = 0

            while q:
                qlen = len(q)
                
                for _ in range(qlen):
                    row, col = q.popleft()

                    directions = [(-1,0),(1,0),(0,1),(0,-1)]

                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc 

                        if r <0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                            perimeter += 1
                        elif (r,c) not in visit:
                            visit.add((r,c))
                            q.append((r,c))
            
            return perimeter


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    total += bfs(r,c)

        return total