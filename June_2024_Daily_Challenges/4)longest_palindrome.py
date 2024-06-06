'''
Problem Statement:  Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        needed_dict = {}
        length, c = 0, 0
        
        for i in s:
            needed_dict[i] = needed_dict.get(i, 0) + 1
        
        for k, v in needed_dict.items():
            if v % 2 == 0:
                length += v
            else:
                if v > 1:
                    length += v - 1
                    c = 1
                else:
                    c = 1
        
        return length + c
                
        
sol_obj = Solution()
print(sol_obj.longestPalindrome("abccccdd"))