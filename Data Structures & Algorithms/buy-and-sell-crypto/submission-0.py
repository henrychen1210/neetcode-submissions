class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        res = 0

        for i in range(1, len(prices)):
            res = max(res, prices[i] - cost)
            cost = min(cost, prices[i])
        
        return res