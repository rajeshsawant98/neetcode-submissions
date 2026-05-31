class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,col=[],[]

        def backtrack(i):
            if i == len(nums):
                res.append(col[:])
                return 
            
            col.append(nums[i])
            backtrack(i+1)

            col.pop()
            backtrack(i+1)

            return
        
        backtrack(0)

        return res

