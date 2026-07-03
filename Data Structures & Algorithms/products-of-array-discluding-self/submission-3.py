class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        res = [1]*len(nums)
        for i,n in enumerate(nums):
            res[i] = prefix
            prefix *= n
        
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] = postfix * res[j]
            postfix *= nums[j]
        

        return res
