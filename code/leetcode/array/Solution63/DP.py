class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        dynamic programming: a matrix A[i][j] denotes the unique path nums from start to end
        1.for first row, if A[0][j-1] is equal to 1, A[0][j]=1 otherwise A[0][j]=0
        2.for first column, if A[j-1][0] is equal 1, A[j][0]=1 otherwise A[j][0]=0
        3.other nodes,A[i][j]=A[i-1][j]+A[i][j-1]
        :param obstacleGrid:
        :return:
        """
        rows = len(obstacleGrid)
        if rows == 0 or obstacleGrid[0][0] ==1:
            return 0
        cols = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        # first row
        for i in range(1, cols):
            obstacleGrid[0][i] = int(obstacleGrid[0][i-1]==1 and obstacleGrid[0][i]==0)
        # first column
        for j in range(1, rows):
            obstacleGrid[j][0] = int(obstacleGrid[j-1][0]==1 and obstacleGrid[j][0] == 0)
        i,j =1, 1
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[rows-1][cols-1]
