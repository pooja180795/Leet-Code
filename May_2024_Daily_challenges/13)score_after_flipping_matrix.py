class Solution:
    def convert_matrix(self, grid, r, c):
            if grid[r][c] == 0:
                        grid[r][c] = 1
            else : 
                grid[r][c] = 0
    def matrixScore(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            if grid[r][0] != 1:
                grid[r][0] = 1
                for c in range(1, cols):
                    self.convert_matrix(grid, r, c)
                    
                    
        for c in range(1, cols):
            zeros, ones = 0, 0
            for r in range(rows):
                if grid[r][c] == 0:
                    zeros += 1
                else: ones += 1
            if zeros > ones:
                for r in range(rows):
                    self.convert_matrix(grid, r, c)
        sum = 0
        for r in range(rows):
            count = len(grid[0]) - 1
            for c in range(cols):
                sum += (2 ** count)  * grid[r][c]
                count -= 1
        return sum


sol_obj = Solution()
print(sol_obj.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))