<<<<<<< HEAD
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in s_dict and t[i] not in s_dict.values():
                s_dict[s[i]] = t[i]
            else:
                continue

        new_str = str()

        for i in s:
            if i not in s_dict:
                return False
            else:
                new_str += s_dict[i]

        if new_str == t:
            return True
        else:
            return False

sol_obj = Solution()
print(sol_obj.isIsomorphic("badc", "baba"))

        
=======
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in s_dict and t[i] not in s_dict.values():
                s_dict[s[i]] = t[i]
            else:
                continue

        new_str = str()

        for i in s:
            if i not in s_dict:
                return False
            else:
                new_str += s_dict[i]

        if new_str == t:
            return True
        else:
            return False

sol_obj = Solution()
print(sol_obj.isIsomorphic("badc", "baba"))

        
>>>>>>> 69f7814c79c2c38546be09a7175733d9a63436ce
        