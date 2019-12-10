import sys


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        rows, cols = len(matrix), len(matrix[0])

        is_zero = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                is_zero[i][j] = 0 == matrix[i][j]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0 and is_zero[i][j]:
                    for m in range(cols):
                        matrix[i][m] = 0
                    for n in range(rows):
                        matrix[n][j] = 0
