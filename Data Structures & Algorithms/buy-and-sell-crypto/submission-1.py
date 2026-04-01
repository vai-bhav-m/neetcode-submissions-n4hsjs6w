class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        min_till_i, max_prof = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < min_till_i:
                min_till_i = prices[i]
            max_prof = max(max_prof, prices[i] - min_till_i)
        return max_prof
           
