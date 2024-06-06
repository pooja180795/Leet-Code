'''
Problem Statement: Append Characters to String to Make Subsequence

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
'''
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        start = 0
        end = len(s)
        for i in range(len(t)):
            if t[i] in s[start:end]:
                count += 1
                start = s.find(t[i], start, end) + 1
                #print(start)
                continue
            else:
                return len(t) - count
        return 0
                
        
sol_obj = Solution()
print(sol_obj.appendCharacters("coding", "coffee"))



                                


