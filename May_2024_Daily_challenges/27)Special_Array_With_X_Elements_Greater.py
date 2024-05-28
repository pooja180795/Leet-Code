'''
Question : Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

'''

class Solution:
    def specialArray(self, nums):
        N = len(nums)
        
        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1
        
        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i
        
        return -1

sol_obj = Solution()
print(sol_obj.specialArray([3,5]))
            
        