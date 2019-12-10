class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if rows == 0 or len(matrix[0])==0:
            return False
        if target < matrix[0][0]:
            return False
        flag = False
        cols = len(matrix[0])
        for index in range(rows*cols):
            i, j = index // cols, index % cols
            if matrix[i][j] == target:
                flag=True
                break
            if matrix[i][j] > target:
                break
        return flag
    