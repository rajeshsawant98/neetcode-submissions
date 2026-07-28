class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for n in numSet:
            # check if it's a start of a subsequence 

            if (n-1) not in numSet:

                length = 0
                while( (n + length) in nums):
                    length += 1
                longest = max(length,longest)
        
        return longest


