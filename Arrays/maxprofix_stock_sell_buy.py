from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxprofit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprofit = max(profit, maxprofit)
            else:
                buy = sell
            sell += 1
        return maxprofit


pricelist = [7,1,5,3,6,4]
pricelist = [7,6,4,3,1]
print(Solution().maxProfit(pricelist))