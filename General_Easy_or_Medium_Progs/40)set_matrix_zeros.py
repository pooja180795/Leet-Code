class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_arr = list()
        col_arr = list()
        needed_dict = dict()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r not in row_arr:
                        row_arr.append(r)
                    if c not in col_arr:
                        col_arr.append(c)

        for r in row_arr:
            for c in range(cols):
                matrix[r][c] = 0
        for c in col_arr:
            for r in range(rows):
                matrix[r][c] = 0

        return matrix

sol_obj = Solution()
print(sol_obj.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))