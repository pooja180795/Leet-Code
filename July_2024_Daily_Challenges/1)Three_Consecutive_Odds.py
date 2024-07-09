'''
Problem Name: Three Consecutive Odds
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''
from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for num in arr:
            if num % 2 == 1:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 0
        return False
    
sol_obj = Solution()
print(sol_obj.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))