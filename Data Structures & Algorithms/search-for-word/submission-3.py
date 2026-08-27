class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows,cols = len(board), len(board[0])

        visit = set()

        def dfs(i,row,col):
            if i == len(word):
                return True

            if row >= rows or col >= cols or row < 0 or col < 0 or board[row][col] != word[i] or (row,col) in visit:
                return False
            
            
            visit.add((row,col))
            res = dfs(i+1,row + 1,col) or dfs(i+1,row - 1,col) or dfs(i+1,row,col + 1) or dfs(i+1,row,col-1)

            visit.remove((row,col))

            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(0,r,c):
                    return True

        return False