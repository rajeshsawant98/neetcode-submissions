class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def backtrack(i,sol,total):
            if total == target:
                res.append(sol[:])
                return
            
            if i == n or total>target:
                return 
            
            sol.append(nums[i])
            backtrack(i,sol,total+nums[i])

            sol.pop()
            backtrack(i+1,sol,total)

            return 
        
        backtrack(0,[],0)

        return res