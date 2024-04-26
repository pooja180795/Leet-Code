'''
Problem Name: Best time to buy and sell stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if buy < prices[i]:
                profit += prices[i] - buy
                if i != len(prices) - 1:
                    if prices[i] < prices[i+1]:
                        buy = prices[i]
                    else: buy = prices[i+1]
            else: 
                buy = prices[i]
        return profit
    
sol_obj = Solution()
print(sol_obj.maxProfit([5,4,3,2,1]))
        

        