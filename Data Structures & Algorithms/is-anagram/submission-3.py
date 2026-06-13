class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        MapS ={}
        MapT ={}

        for i in range(len(s)):
            if s[i] in MapS: MapS[s[i]] +=1 
            else : MapS[s[i]] = 1
            if t[i] in MapT: MapT[t[i]] +=1 
            else : MapT[t[i]] = 1
        
        return MapS == MapT