'''
Problem Statement : Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.
'''

class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        dictionary = sorted(dictionary)
        new_list = []
        words = sentence.split(" ")
        for word in words:
            count = 0
            for root in dictionary:
                if word.startswith(root):
                    new_list.append(root)
                    count += 1
                    break
            if count < 1:
                new_list.append(word)   
        return (' ').join(new_list)
       
sol_obj = Solution()
print(sol_obj.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))