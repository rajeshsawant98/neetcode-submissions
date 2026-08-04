class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        n = len(nums)

        def backtrack(i,path):
            if i == n:
                res.append(path[:])
                return 
            

            path.append(nums[i])
            backtrack(i+1,path)

            path.pop()
            backtrack(i+1,path)
        
        backtrack(0,[])
        return res