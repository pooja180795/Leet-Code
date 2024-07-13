'''
Problem Name: Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

'''

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        aCount, bCount = 0, 0
        totalPoints = 0
        
        if x < y:
            x , y = y, x
            s = s[::-1]
        
        for char in s:
            if char == "a":
                aCount += 1
            elif char == "b":
                if aCount > 0:
                    totalPoints += x
                    aCount -= 1
                else:
                    bCount += 1
            else:
                if aCount > 0 and bCount > 0:
                    totalPoints += min(aCount, bCount) * y
                    
                aCount, bCount = 0, 0
        
        totalPoints += min(aCount, bCount) * y
        return totalPoints

sol_obj = Solution()
print(sol_obj.maximumGain("cdbcbbaaabab", 5, 4))