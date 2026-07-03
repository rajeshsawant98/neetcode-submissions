class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dup = set()

        for n in nums:
            if n in Dup:
                return True
            Dup.add(n)
        
        return False