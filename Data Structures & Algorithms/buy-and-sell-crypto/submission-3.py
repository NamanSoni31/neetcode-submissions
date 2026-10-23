class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        minPrice = prices[0]
        profit = 0
        while i < len(prices):
            if (prices[i] - minPrice) > profit:
                profit = prices[i] - minPrice
            if prices[i] < minPrice:
                minPrice = prices[i]
            i += 1
        
        return profit
                