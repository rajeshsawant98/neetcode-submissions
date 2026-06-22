class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        longest = set()

        l = 0

        for r in range(len(s)):
            while s[r] in longest:
                longest.remove(s[l])
                l +=1
            
            longest.add(s[r])
            res = max(res, (r-l)+1)
        
        return res
