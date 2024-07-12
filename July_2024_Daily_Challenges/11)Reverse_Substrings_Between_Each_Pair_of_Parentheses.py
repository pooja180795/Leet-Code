'''
Problem Name: Reverse Substrings Between Each Pair of Parentheses
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        bracket_stack = []
        char_arr = []
        track_count_arr = []
        
        for i in range(len(s)):
            if s[i] == "(":
                bracket_stack.append(s[i])
                track_count_arr.append(len(char_arr))
            elif s[i] == ")":
                bracket_stack.pop()
                start  = track_count_arr[-1]
                end = len(char_arr) - 1
                
                while start <= end:
                    char_arr[start], char_arr[end] = char_arr[end], char_arr[start]
                    start += 1
                    end -= 1
                track_count_arr.pop()
                    
            else:
                char_arr.append(s[i])
        
        return ''.join(char_arr)
    
sol_obj = Solution()
print(sol_obj.reverseParentheses("(ed(et(oc))el)"))