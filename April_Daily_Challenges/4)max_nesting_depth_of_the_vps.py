class Solution:
    def maxDepth(self, s: str) -> int:
        needed_stack = list()
        ans = 0
        for ele in s:
            if ele == '(':
                needed_stack.append(ele)
                if len(needed_stack) > ans:
                    ans = len(needed_stack)
            elif ele == ')':
                needed_stack.pop()
                
        return ans
        

sol_obj = Solution()
print(sol_obj.maxDepth("(1)+((2))+(((3)))"))