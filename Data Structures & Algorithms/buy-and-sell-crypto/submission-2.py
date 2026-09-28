class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        minPrice = prices[0]
        maxVal = 0
        while i < len(prices): 
            if (prices[i] - minPrice) > maxVal:
                maxVal = prices[i] - minPrice
            if prices[i] < minPrice:
                minPrice = prices[i]
            i += 1
        return maxVal