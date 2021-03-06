'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices)<2:
            return 0
        
        min_price=max(prices)
        profit=0
        
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            elif prices[i]-min_price>profit:
                profit=prices[i]-min_price
        return profit
        
