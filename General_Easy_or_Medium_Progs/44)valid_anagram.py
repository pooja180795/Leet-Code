class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1

        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1

        for k, v in s_dict.items():
            if k in t_dict:
                if t_dict[k] != v:
                    return False

            else: return False
        for k, v in t_dict.items():
            if k not in s_dict:
               return False
            print(k)
        return True

sol_obj = Solution()
print(sol_obj.isAnagram("a", "ab"))