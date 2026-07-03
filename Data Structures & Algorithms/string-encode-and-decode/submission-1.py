class Solution:

    def encode(self, strs: List[str]) -> str:

        res =""

        for s in strs:
            l = len(s) 
            res+= str(l) +"#" + s
        
        return res


    def decode(self, s: str) -> List[str]:

        res= []

        l,r = 0,0

        while r<(len(s)):

            if s[r] =="#":
                L = int(s[l:r])
                res.append(s[r+1:r+1 + L])
                l = r = r+1 + L
            r+=1
        
        return res

