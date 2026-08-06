class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        fx= fy = fz = False
        x,y,z = target

        for a,b,c in triplets:
            if a<=x and b<=y and c<=z:
                if a==x:
                    fx= True
                if b==y:
                    fy= True
                if c==z:
                    fz= True
                
                if fx and fy and fz:
                    return True
        
        return False