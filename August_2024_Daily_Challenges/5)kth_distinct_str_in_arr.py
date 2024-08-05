'''
Problem Name : Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
'''
from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dict = {}
        unique_arr = []
        
        # Iterate through each string and add into dictionary
        for string in arr:
            str_dict[string] = str_dict.get(string, 0) + 1

        # append each unique string in unique array
        for key, val in str_dict.items():
            if val == 1:
                unique_arr.append(key)
        # Check if there are enough distinct strings
        if len(unique_arr) >= k:
            return unique_arr[k-1]
        else:
            return ""
        
sol_obj = Solution()
print(sol_obj.kthDistinct(["pooja","bakulbhai","chothani","bakulbhai","chothani","abhi"], 1))