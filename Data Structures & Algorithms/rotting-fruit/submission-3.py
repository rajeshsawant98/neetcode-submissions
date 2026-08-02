class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        count = 0
        minutes = 0
        visit = set()

        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        while q and count>0:
            for _ in range(len(q)):

                row,col = q.popleft()

                directions = [(0,1),(1,0),(-1,0),(0,-1)]

                for dr,dc in directions:
                    r,c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                        count -=1

            
            minutes +=1
        
        return minutes if count <=0 else -1


