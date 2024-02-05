class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        profit = 0
        currentProfit = 0
        while buy < (len(prices) - 1) and sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit == 0:
                sell += 1
            elif profit < 0:
                buy += 1
            elif profit > 0:
                if currentProfit == profit:
                    sell += 1
                elif currentProfit > profit:
                    sell += 1
                elif currentProfit < profit:
                    currentProfit = profit
                    sell += 1

        return currentProfit




# use while loop to iterate through prices, initialise variables which keep track of index which is used to compare prices
            
        