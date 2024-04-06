class Solution:
    def isValid(self, s: str) -> bool:
        para_stack = list()
        for p in s:
            if p in "{[(":
                para_stack.append(p)
            else:
                if not para_stack or (p == ')' and para_stack[-1] != '('):
                    return False
                if not para_stack or (p == '}' and para_stack[-1] != '{'):
                    return False
                if not para_stack or (p == ']' and para_stack[-1] != '['):
                    return False
                
                else:
                    para_stack.pop()
        print(para_stack)
        if not para_stack:
            return True
        else: return False

sol_obj = Solution()
print(sol_obj.isValid(")]"))
                            

        