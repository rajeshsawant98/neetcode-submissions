class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        res =[]

        def backtrack(i,path,total):
            if total == target :
                res.append(path[:])
                return
            
            if total > target or i == n:
                return
            
            path.append(candidates[i])
            backtrack(i+1,path,total+candidates[i])
            path.pop()

            while i + 1< n and candidates[i] == candidates[i+1]:
                i +=1
            backtrack(i+1,path,total)
        
        backtrack(0,[],0)

        return res