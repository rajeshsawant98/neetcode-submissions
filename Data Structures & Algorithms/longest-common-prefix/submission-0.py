class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res =""

        Small = len(strs[0])
        SmallS = strs[0]

        for s in strs:
            if len(s) < Small:
                Small = len(s)
                SmallS = s

        for i in range(Small):
            for s in strs:
                if s[i] != SmallS[i]:
                    return res
            res += SmallS[i]
        
        return res
