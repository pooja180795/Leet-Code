'''
Question Name: Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
                
        if start == nums[-1]:
            ans.append(str(nums[-1]))
        else:
            ans.append(str(start) + "->" + str(nums[-1]))
        
        return ans

sol_obj = Solution()
print(sol_obj.summaryRanges([0,2,3,4,6,8,9]))
                
                    
