class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0

        MaxProfit = 0

        for r in range(len(prices)):
            if prices[l] <= prices[r]:
                MaxProfit = max(MaxProfit, prices[r] - prices[l] )
            else:
                l = r
        
        return MaxProfit