class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        l=0 
        r = len(s1)-1

        while r < len(s2):
            Cop = count.copy()

            for i in range(l,r+1):
                if s2[i] in Cop:
                    Cop[s2[i]] -=1
                    if Cop[s2[i]] == 0:
                        del Cop[s2[i]]

                else:
                    break
            
            if not Cop:
                return True
            l+=1
            r+=1
        
        return False


