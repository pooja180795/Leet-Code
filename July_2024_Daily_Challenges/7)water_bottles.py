'''
Problem Name: Water Bottles
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_btl_drnk = numBottles
        temp = numBottles
        
        while temp >= numExchange:
            div = temp // numExchange
            max_btl_drnk += div
            remainder = temp % numExchange
            
            temp = div + remainder
            
        return max_btl_drnk
    
sol_obj = Solution()
print(sol_obj.numWaterBottles(9.3))