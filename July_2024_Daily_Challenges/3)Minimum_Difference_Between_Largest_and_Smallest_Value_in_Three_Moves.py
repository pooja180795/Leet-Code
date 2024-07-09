'''
Problem Name: Minimum Difference Between Largest and Smallest Value in Three Moves
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
'''
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) <= 4:
            return 0
        
        min_diff = float("inf")
        
        for left in range(4):
            right = len(nums) - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])
        
        return min_diff
    
sol_obj = Solution()
sol_obj.minDifference([5,3,2,4])