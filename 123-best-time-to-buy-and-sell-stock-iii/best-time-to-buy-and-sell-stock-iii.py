# given an array prices -> 2 transactions with max profit, no simultaneous
# DP problem at most 2 transactions -> track my state
# never bought, first buy first sell second buy second sell -> track max profit achievable
# state transition -> first buy: bought already, or buy today
# first sell -> sold already, or sell today

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_buy = float('-inf')
        second_buy = float('-inf')

        first_sell = 0
        second_sell = 0

        for price in prices:
            first_buy = max(first_buy, - price)
            first_sell = max(first_sell, first_buy + price)

            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        return second_sell