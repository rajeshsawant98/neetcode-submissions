class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res =[]

        n = len(candidates)

        def backtrack(i,path,total):
            if total == target:
                res.append(path[:])
                return 

            if total > target or i == n:
                return
            
            for j in range(i,n):
                if j >i and candidates[j] == candidates[j-1]:
                    continue
                
                path.append(candidates[j])
                backtrack(j+1,path,total + candidates[j])
                path.pop()
            

        backtrack(0,[],0)

        return res
