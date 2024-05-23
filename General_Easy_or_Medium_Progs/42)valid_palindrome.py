'''
Problem : Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s)
        lowercase_str = new_str.lower()

        start = 0 
        end = len(lowercase_str) - 1

        while start < end:
            if lowercase_str[start] == lowercase_str[end]:
                start += 1
                end -= 1
            else: return False
        
        return True
    
sol_obj = Solution()
print(sol_obj.isPalindrome("A man, a plan, a canal: Panama"))