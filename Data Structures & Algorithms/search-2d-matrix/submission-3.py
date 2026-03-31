class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols= len(matrix), len(matrix[0])

        l,r = 0 , rows - 1

        while(l<=r):
            mid = (l+r)//2
            if target > matrix[mid][-1]:
                l= mid + 1
            elif target < matrix[mid][0]:
                r= mid - 1
            else:
                break
        
        if not (l<=r):
            return False
        
        m = mid
        l1, r1 = 0, cols - 1
        while (l1<=r1):
            m1 = (l1 + r1)//2
            if target > matrix[m][m1]:
                l1 = m1 + 1
            elif target < matrix[m][m1]:
                r1 = m1 - 1
            else:
                return True
        
        return False


        