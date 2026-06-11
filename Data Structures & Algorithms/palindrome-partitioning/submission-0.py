class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def pali(s,l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i,path):
            if i == n:
                res.append(path[:])
            
            for j in range(i,n):
                if pali(s,i,j):
                    path.append(s[i:j+1])
                    backtrack(j+1,path)
                    path.pop()
        
        backtrack(0,[])

        return res
