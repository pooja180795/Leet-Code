'''
Problem Name: Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict, nums2_dict = {}, {}
        m = len(nums1)
        n = len(nums2)
        result = []
        
        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1
            
        for num in nums2:
            nums2_dict[num] = nums2_dict.get(num, 0) + 1
        
        if m <= n:
            for key, val in nums1_dict.items():
                if key in nums2_dict:
                    count = min(nums1_dict[key], nums2_dict[key])
                    while count > 0:
                        result.append(key)
                        count -= 1
        elif n < m:
            for key, val in nums2_dict.items():
                if key in nums1_dict:
                    count = min(nums1_dict[key], nums2_dict[key])
                    while count > 0:
                        result.append(key)
                        count -= 1
        
        return result
            
sol_obj =Solution()
print(sol_obj.intersect([1,2,2,1], [2,2]))