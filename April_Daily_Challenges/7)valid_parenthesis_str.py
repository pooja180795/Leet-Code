class Solution:
    def validParenthesisStr(self, s: str) -> bool:
        minCount = 0
        maxCount = 0

        for char in s:
            
            if char == '(':
                minCount += 1
                maxCount += 1
            elif char == ')':
                minCount -= 1
                maxCount -= 1
            else:
                minCount -= 1
                maxCount += 1
            if minCount < 0:
                minCount = 0
            if maxCount < 0:
                return False
        if minCount == 0:
            return True
        else: return False
         

sol_obj = Solution()
print(sol_obj.validParenthesisStr(")*"))