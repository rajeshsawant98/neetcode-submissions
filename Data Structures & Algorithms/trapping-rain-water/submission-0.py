class Solution:
    def trap(self, height: List[int]) -> int:
        if not height :
            return 0
        
        l,r = 0, len(height)-1
        lmax , rmax = height[l],height[r]
        count = 0

        while(l<r):
            if(lmax <= rmax):
                l += 1
                if( height[l] >= lmax):
                    lmax = height[l]
                else:
                    count += lmax - height[l]
            else:
                r -= 1
                if ( height[r] >= rmax):
                    rmax = height[r]
                else:
                    count += rmax - height[r]

        
        return count