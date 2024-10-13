class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        min_price = float(inf)
        
        for i in (len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            current_profit = prices[i] - min_price
            profit.append(current_profit)
        return max(max(profit), 0)