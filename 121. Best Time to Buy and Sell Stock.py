class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy= 0, prices[0]
        for index in range(1, len(prices)):
            if buy > prices[index]:
                buy = prices[index]
            elif profit < (prices[index] - buy):
                profit = (prices[index] - buy)
        return profit