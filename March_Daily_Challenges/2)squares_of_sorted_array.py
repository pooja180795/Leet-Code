class solution:
    def SortedSquares(self, num):
        ans_arr = list()
        for i in num:
            square_value = i ** 2
            ans_arr.append(square_value)
        return ans_arr



sol_obj = solution()
print(sorted(sol_obj.SortedSquares([-7,-3,2,3,11])))