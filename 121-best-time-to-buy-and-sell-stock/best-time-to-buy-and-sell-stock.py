class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price  = float('inf')
        max_profit = 0

        for index, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

          
        