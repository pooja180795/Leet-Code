'''
Question Name: Sort the Jumbled Numbers
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
'''
from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr, ans = [], []
        for num in nums:
            digits_list = [int(digit) for digit in str(num)]
            str_map_num = ''
            for n in digits_list:
                str_map_num = str_map_num + str(mapping[n])
            map_num = int(str_map_num)
            arr.append((map_num,num))
        arr.sort(key=lambda x: x[0])
       
        for num in arr:
           ans.append(num[1])
        
        return ans
    
sol_obj = Solution()
print(sol_obj.sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]))


