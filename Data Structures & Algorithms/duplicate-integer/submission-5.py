class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dup = set()

        for i in range(len(nums)):
            if nums[i] in Dup:
                return True
            Dup.add(nums[i])
        
        return False