class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.results = 0
        self.rows = len(obstacleGrid)
        if self.rows == 0 or obstacleGrid[0][0]==1:
            return 0
        self.cols = len(obstacleGrid[0])
        self.find(0, 0, obstacleGrid)
        return self.results
    def find(self, i ,j, grid):
        if i == self.rows - 1 and j == self.cols - 1 and grid[i][j] == 0:
            self.results +=1
        if j < self.cols - 1 and grid[i][j+1] == 0:
            self.find(i, j+1, grid)
        if i < self.rows - 1 and grid[i+1][j] == 0:
            self.find(i+1, j, grid)

s = Solution()
print(s.uniquePathsWithObstacles([[1,0]])) #0