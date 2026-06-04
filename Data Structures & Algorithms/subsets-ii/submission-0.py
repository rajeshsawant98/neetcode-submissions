class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res =[]
        n = len(nums)
        nums.sort()

        def backtrack(i,subset):
            if i == n:
                res.append(subset[:])
                return
            
            # include the subsets with nums[i]
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()

            #subsets that don't include nums[i]

            while i+1< n and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1,subset)

        backtrack(0,[])

        return res
