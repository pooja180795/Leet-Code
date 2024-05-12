class Solution:

    def find_local_max(self, grid,  x, y):
            max_element = 0
            for i  in range(x, x+3):
                for j in range(y, y+3):
                    max_element = max(max_element, grid[i][j])
            return max_element


    def largestLocal(self, grid):
        n = len(grid)
        max_local = []
        for i in range(n-2):
            row = []
            for j in range(n-2):
                row.append(0)
            max_local.append(row)
        

        for i in range(n-2):
            for j in range(n-2):
                max_local[i][j] = self.find_local_max(grid, i, j)
        return max_local

        



sol_obj = Solution()
print(sol_obj.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))