class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                curProfit = prices[sell] - prices[buy]
                profit = max(profit, curProfit)
            else:
                buy = sell

            sell += 1

        return profit
