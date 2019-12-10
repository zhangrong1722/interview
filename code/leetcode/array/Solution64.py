class Solution:
    def minPathSum(self, grid):
        """
        this solution is based on Solution63.
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        # first row
        for i in range(1, cols):
            grid[0][i] += grid[0][i-1]
        # first column
        for j in range(1, rows):
            grid[j][0] += grid[j-1][0]
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[rows-1][cols-1]


