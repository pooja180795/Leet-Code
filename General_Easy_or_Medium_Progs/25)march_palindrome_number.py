class Solution:
    def isPalindrome(self, x: int) -> bool:
        abs_num = abs(x)
        reversed_num = int(str(abs_num)[::-1])
        if reversed_num == x:
            print(1)
        else: print(0)
        
sol_obj = Solution()
sol_obj.isPalindrome(-121)