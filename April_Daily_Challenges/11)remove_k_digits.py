class Solution:
    def removeKDigits(self, num, k):
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        print(stack)
        # If k is still greater than 0, remove remaining largest digits from the stack
        while k > 0:
            stack.pop()
            k -= 1
        # Concatenate the digits in the stack to form the smallest number
        smallest_num = ''.join(stack).lstrip('0')
        return smallest_num if smallest_num else '0'

sol_obj = Solution()
print(sol_obj.removeKDigits("8876", 1))
