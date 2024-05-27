class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            sum = 0
            for char in str(number):
                sum += int(char) ** 2
            print(sum)
            return sum



        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


sol_obj = Solution()
print(sol_obj.isHappy(33))