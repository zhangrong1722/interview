"""
题目：二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
     请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution(object):
    def find_digit(self, nums, digit):
        if len(nums) == 0:
            return False

        rows, cols = len(nums), len(nums[0])
        i, j = rows - 1, 0
        while i >= 0 and j < cols:
            if nums[i][j] == digit:
                return True
            elif nums[i][j] > digit:
                i -= 1
            else:
                j += 1
        return False


s = Solution()
# 测试用例：没有要查找的数字
print(s.find_digit([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 3))
# 测试用例：有需要查找的数字 分别为最大值和最小值
print(s.find_digit([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 1))
print(s.find_digit([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 15))
# 空数组
print(s.find_digit([], 10))
