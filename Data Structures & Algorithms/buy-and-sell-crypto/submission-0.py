class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            difference = prices[i] - min_price
            if max_profit < difference:
                max_profit = difference

        return max_profit 
            



        