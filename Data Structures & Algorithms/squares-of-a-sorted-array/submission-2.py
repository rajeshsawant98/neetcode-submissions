class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        p = len(nums)-1

        l,r = 0 , p

        while(l<=r):
            leftSquare = nums[l]**2
            rightSquare = nums[r]**2

            if leftSquare >= rightSquare:
                res[p]= leftSquare
                l+=1
            else:
                res[p]= rightSquare
                r-=1
            
            p-=1
        
        return res
