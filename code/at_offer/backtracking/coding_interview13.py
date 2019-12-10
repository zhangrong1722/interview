"""
题目：机器人的运动范围
"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows == 0 or cols == 0:
            return 0
        visited = [[False] * cols for _ in range(rows)]
        return self.helper(threshold, rows, cols, 0, 0, visited)

    def helper(self, threshold, rows, cols, row, col, visited):
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or self.sum(row) + self.sum(col) > threshold:
            return 0
        visited[row][col] = True
        return 1 + self.helper(threshold, rows, cols, row - 1, col, visited) + self.helper(threshold, rows, cols, row + 1, col, visited) + self.helper(threshold, rows, cols, row, col - 1, visited) + self.helper(threshold, rows, cols, row, col + 1, visited)

    def sum(self, digit):
        results = 0
        while digit > 0:
            results += digit % 10
            digit //= 10
        return results

s = Solution()
print(s.movingCount(5, 10, 10))