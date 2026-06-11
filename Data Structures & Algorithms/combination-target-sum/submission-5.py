class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i,path,total):
            if total == target :
                res.append(path[:])
                return
            
            if total > target or i == n:
                return

            path.append(nums[i])
            backtrack(i, path,total + nums[i])
            path.pop()
            backtrack(i+1, path, total )

        backtrack(0,[],0)

        return res