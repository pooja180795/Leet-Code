class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.strip(' ')               #remove white spaces from both sides
        r = t.split(' ')               #spilt the string with white space
        return len(r[-1])


sol_obj = Solution()
print(sol_obj.lengthOfLastWord("  this is my book  "))
