class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSums = {0:1}
        res =0
        prefixSum = 0

        for n in nums:

            prefixSum +=n
            diff = prefixSum - k

            
            res += prefixSums.get(diff, 0)
            
            prefixSums[prefixSum] = 1 + prefixSums.get(prefixSum,0) 
        
        return res