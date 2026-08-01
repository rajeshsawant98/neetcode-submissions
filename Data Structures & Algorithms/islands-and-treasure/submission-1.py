class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows,cols = len(grid), len(grid[0])

        visit = set()
        dist = 0

        q = collections.deque()

        def addCell(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c) in visit:
                return
            
            q.append((r,c))
            visit.add((r,c))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 :
                    q.append((r,c))
                    visit.add((r,c))

        
        while q:
            qlen = len(q)

            for _ in range(qlen):
                r,c = q.popleft()

                grid[r][c] = dist

                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r-1,c)
                addCell(r,c-1)
            
            dist +=1
        

