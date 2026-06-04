class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]

        n = len(nums)

        def backtrack(i,sol,total):
            if total == target:
                res.append(sol[:])
                return
            
            if total > target or i == n:
                return
            
            sol.append(nums[i])
            backtrack(i,sol, total + nums[i])
            sol.pop()

            backtrack(i+1, sol, total)
        
        backtrack(0,[],0)

        return res