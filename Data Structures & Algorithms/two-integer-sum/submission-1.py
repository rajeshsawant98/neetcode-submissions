class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        val = {}

        for i in range(len(nums)):
            a = target - nums[i]
            if a in val:
                return [val[a],i]
            val[nums[i]]= i

        