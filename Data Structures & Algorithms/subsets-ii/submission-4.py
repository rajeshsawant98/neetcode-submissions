class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        n=len(nums)

        def backtrack(i,path):
            if i== len(nums):
                res.append(path[:])
                return 
            
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()

            while i + 1 <n and nums[i] == nums[i+1] :
                i +=1
            
            backtrack(i+1,path)
        
        backtrack(0,[])

        return res