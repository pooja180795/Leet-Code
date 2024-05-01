'''
Problem Name: Reverse Prefix of Word
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        string = ""
        if ch not in word:
            return word
        else:
            index = word.find(ch)
            for i in range(index, -1, -1):
                string += word[i]
            for i in range(index+1, len(word)):
                string += word[i]
        return string 

sol_obj = Solution()
print(sol_obj.reversePrefix("zxcvbnm", "c"))