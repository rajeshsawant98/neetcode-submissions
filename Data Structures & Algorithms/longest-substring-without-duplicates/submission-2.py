class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        m= 0 
        cmap= {}

        l,r= 0,0

        while r < len(s):
            if s[r] in cmap and cmap[s[r]] >= l:
                l = cmap[s[r]] + 1 
            cmap[s[r]] = r
            m = max(m,r-l+1)
            r+=1
        
        return m