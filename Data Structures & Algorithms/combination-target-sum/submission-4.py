class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []


        def backtrack(start,sol,total):
            if total == target:   # 1. Base case
                res.append(sol[:])
                return

            for i in range(start,len(nums)):    # 2. Choices
                if total + nums[i] > target:  # 3. Constraints
                    continue

                sol.append(nums[i])
                backtrack(i,sol,total + nums[i])
                sol.pop()           # 4. Backtracking step
                
        
        backtrack(0,[],0)

        return res