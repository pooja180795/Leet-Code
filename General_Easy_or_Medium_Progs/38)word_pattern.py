class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        needed_dict = {}
        needed_set = set()
        needed_arr = s.split(" ")

        for i in range(len(pattern)):
            if pattern[i] in needed_dict:
                if needed_dict[pattern[i]] != needed_arr[i]:
                    return False
            else:
                if needed_arr[i] not in needed_set:
                   needed_dict[pattern[i]] = needed_arr[i]
                   needed_set.add(needed_arr[i])
                else:
                    return False
        return True

            
        


sol_obj = Solution()
print(sol_obj.wordPattern("abba" , "dog cat cat fish"))