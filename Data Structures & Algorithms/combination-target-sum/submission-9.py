class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)

        def backtrack(i,path,total):
            if total == target:
                res.append(path[:])
                return 
            
            if total>target or i==n:
                return
            
            for j in range(i,n):
                path.append(nums[j])
                backtrack(j,path,total+nums[j])
                path.pop()
        
        backtrack(0,[],0)

        return res