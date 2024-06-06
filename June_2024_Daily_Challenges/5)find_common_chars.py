'''
Problrm Statement : Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
'''
class Solution:
    def commonChars(self, words):
    
        result = []

        for char in range(ord('a'), ord('z') + 1):
            char = chr(char)
            min_count = float('inf')

            for word in words:
                count = word.count(char)
                min_count = min(min_count, count)

            result.extend([char] * min_count)
        
        return result

        
            

            

sol_obj = Solution()
print(sol_obj.commonChars(["Aooja", "pranAv"]))