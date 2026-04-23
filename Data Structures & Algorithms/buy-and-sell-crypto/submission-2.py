class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min_price, max_prof = prices[0], 0
        for i in range(1, len(prices)):
            max_prof = max(max_prof, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return max_prof
        