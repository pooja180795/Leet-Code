'''
Problem Name: Find the index of a first occurance of a string
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #first way
        i, j, count, start_from = 0, 0, 0, 0
        while i < len(needle) and j < len(haystack):
            if haystack[j] == needle[i]:
                if haystack[j] == needle[0]:
                    count += 1
                    if count == 2:
                        start_from = j
                j += 1
                i += 1
            elif count > 1:
                j = start_from
                i = 0
                count = 1
            elif haystack[j] == needle[0]:
                j += 1
                i = 1
            else:
                j += 1
                i = 0
        if i == len(needle):
            return j - len(needle)
        else: return -1

        #second way
        index = haystack.find(needle)
        if index:
            return index
        else: return -1

sol_obj = Solution()
print(sol_obj.strStr("aabaaabaaac", "aabaxaac"))

