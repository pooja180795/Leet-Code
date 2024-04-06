class Solution:
    def customSortString(self, order: str, s: str) -> str:
        permuted_str = ''
        needed_dict = dict()
        for k in s:
            needed_dict[k] = needed_dict.get(k, 0) + 1
        for i in order:
            if i in s:
                for j, m in needed_dict.items():
                    if j == i:
                        while m != 0:
                            permuted_str = permuted_str + j
                            m = m - 1

        for v in s: 
            if v not in permuted_str:
                for t, y in needed_dict.items():
                    if t == v:
                        while y != 0:
                            permuted_str = permuted_str + t
                            y = y - 1
        
        return permuted_str
    

sol_obj = Solution()
print(sol_obj.customSortString('abdc', 'afghdccjiodbab'))
