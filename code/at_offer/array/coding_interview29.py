"""
题目：顺时针打印矩阵
     输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。例如，如果输入如下矩阵：
      1  2  3  4
      5  6  7  8
      9 10 11 12
     13 14 15 16
     则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
思路：本题目使用从外到里 逐层打印 一道好题
"""
class Solution(object):
    def printArray(self, nums):
        if nums is None or len(nums) == 0 or len(nums[0]) == 0:
            return
        if len(nums) == 1:
            for i in range(len(nums[0])):
                print(nums[0][i], end=',')
            return
        if len(nums[0]) == 1:
            for i in range(len(nums)):
                print(nums[i][0], end=',')
            return
        start = 0
        rows, cols = len(nums), len(nums[0])
        while start * 2 < rows and start * 2 < cols:
            self.helper(nums, start, rows, cols)
            start += 1

    def helper(self, nums, start, rows, cols):
        endX, endY = cols - start, rows - start
        i, j, k = 0, 0, 0
        for j in range(start, endX):
            print(nums[start][j], end=',')

        for i in range(start + 1, endY):
            print(nums[i][j], end=',')

        for k in range(j - 1, start - 1, -1):
            print(nums[i][k], end=',')

        for m in range(i - 1, start, -1):
            print(nums[m][k], end=',')

s = Solution()
s.printArray([[1, 2, 3, 4, 5, 10], [17, 18, 19, 20, 6, 21], [16, 23, 22, 21, 7, 22], [15, 24, 25, 26, 9, 23], [14, 13, 12, 11, 10, 24]])
print('')
s.printArray([[1]])
print('')
s.printArray([[1], [2], [3], [4]])
print('')
s.printArray([[1, 2, 3, 4]])