'''
Problem: Path with maximum gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

'''


class Solution:
    m = [1, -1, 0, 0]
    n = [0, 0, 1, -1]

    def dfs(self, grid, i, j, rows, cols):

        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            return 0
        
        curr = grid[i][j]
        grid[i][j] = 0
        localMaxGold = curr

        for x in range(4):
            new_i = i + self.m[x]
            new_j = j + self.n[x]

            localMaxGold = max(localMaxGold, curr + self.dfs(grid, new_i, new_j, rows, cols))

        grid[i][j] = curr
        return localMaxGold

    def getMaximumGold(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        maxGold = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.dfs(grid, i, j, rows, cols))
        
        return maxGold
    
    
    
sol_obj = Solution()
print(sol_obj.getMaximumGold([[1,2,0],[3,10,1],[4,2,9]]))



        