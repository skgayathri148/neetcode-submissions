class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        max_profit = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            else:
                max_profit = max(max_price - prices[i], max_profit)

        return max_profit
