'''
Problem Name: Rotate array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

'''

class Solution:
    def rotate(self, arr, k: int) -> None:
        while k != 0:
            arr.insert(0, arr[-1])
            arr.pop()
            k -= 1
        return arr

sol_obj = Solution()
print(sol_obj.rotate([1,2,3,4,5,6,7], 3))
