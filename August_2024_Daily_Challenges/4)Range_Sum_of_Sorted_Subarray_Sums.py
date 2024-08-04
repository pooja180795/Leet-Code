'''
Problem Name: Range Sum of Sorted Subarray Sums
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
'''
from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        nums_sum = sum(nums)
        arr = []

        for i in range(len(nums)):
            sum_ele = nums[i]
            arr.append(sum_ele)
            for j in range(i+1, len(nums)):
                sum_ele += nums[j]
                arr.append(sum_ele)

        arr.sort()
        ans = 0
        for i in range(left-1, right):
            ans += arr[i]
        mod = 10 ** 9 + 7
        return ans % mod
    
sol_obj = Solution()
print(sol_obj.rangeSum([1,2,3,4], 4, 1, 5))