class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]<prices[j]:
                    profit = prices[j] - prices[i]
                    d.append(profit)
        if len(d) ==0:
            return 0
        return max(d)