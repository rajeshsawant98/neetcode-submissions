class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        MapS, MapT = {}, {}

        for i in range(len(s)):
            MapS[s[i]] = 1 + MapS.get(s[i],0)
            MapT[t[i]] = 1 + MapT.get(t[i],0)
        
        return MapS == MapT

        