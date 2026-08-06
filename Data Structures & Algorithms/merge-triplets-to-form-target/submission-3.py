class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        fx = fy = fz = False
        x,y,z = target

        for t in triplets:

            if t[0] > x or t[1] > y or t[2] > z:
                continue
            
            if t[0] == x:
                fx = True
            
            if t[1] == y:
                fy = True
            
            if t[2] == z:
                fz = True

            if fx == fy == fz == True:
                return True
        
        return False