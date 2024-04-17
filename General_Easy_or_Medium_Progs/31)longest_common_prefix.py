'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for i in strs[1:]:
            while pref != i[0: pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0: pref_len]
        return pref
    
sol_obj = Solution()
print(sol_obj.longestCommonPrefix(["Priya","Priyam","Prisa"]))
