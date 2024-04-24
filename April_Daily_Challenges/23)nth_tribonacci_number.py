'''
Challenge Name: Nth Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

'''


class Solution:
    def tribonacci(self, n: int) -> int:
        i = 0
        t_0, t_1, t_2 = 0, 1, 1
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 1
        else:
            while i != n - 2:
                ans = t_0 + t_1 + t_2
                t_0 = t_1
                t_1 = t_2
                t_2 = ans
                i += 1
            return ans
    
sol_obj = Solution()
print(sol_obj.tribonacci(25))