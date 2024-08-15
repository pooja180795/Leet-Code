'''
Problem Name: Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        earned_dict = {5: 0, 10: 0, 20: 0}
        for given_cost in bills:
            if given_cost == 5:
                earned_dict[given_cost] += 1
            if given_cost == 10:
                if earned_dict[5]:
                    earned_dict[5] -= 1
                    earned_dict[given_cost] += 1
                else:
                    return False
            elif given_cost == 20:
                if earned_dict[10] and earned_dict[5]:
                    earned_dict[10] -= 1
                    earned_dict[5] -= 1
                    earned_dict[given_cost] += 1
                elif earned_dict[5] >= 3: 
                    earned_dict[5] -= 3
                    earned_dict[given_cost] += 1
                else:
                    return False
                
        return True
    
sol_obj = Solution()
print(sol_obj.lemonadeChange([5,5,5,10,20]))