class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]

        nums.sort()
        n = len(nums)

        def backtrack(i,path):
            res.append(path[:])
            
            for j in range(i,n):
                if j>i and nums[j] == nums[j-1]:
                    continue
                
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()
            
        
        backtrack(0,[])

        return res
