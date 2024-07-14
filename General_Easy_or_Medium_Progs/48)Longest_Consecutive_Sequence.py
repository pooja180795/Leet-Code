'''
Question Name: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

'''
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0
        
        for start in nums:
            if (start - 1) not in nums_set:
                end = start + 1
                
                while end in nums_set:
                    end += 1
                
                longest_length = max(longest_length, end - start)
        
        return longest_length
    
sol_obj = Solution()
print(sol_obj.longestConsecutive([100,4,200,1,3,2]))