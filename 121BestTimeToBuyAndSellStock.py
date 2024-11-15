class Solution:

    def maxProfit(self, prices):
        if (len(prices) < 2):
            return 0

        minimum = float('inf')
        max_profit = 0

        for num in prices:
            if num < minimum:
                minimum = num
            profit = num - minimum
            if profit > max_profit:
                max_profit = profit
        return max_profit
