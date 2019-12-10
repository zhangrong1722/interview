"""
题目：统计一个数字在排序数组中出现的次数
思路一：看到这道题目 最直接的方法是算法复杂度为O(n) 即扫描一边数组
思路二：看到排序数组 首先想到的是二分法查找 首先找到目标元素 然后从该位置出现 在前后两个位置依次查找 但是该算法时间复杂度依然比较高 向前后两个方向
       查找的算法复杂度依然可能是线性的 因而仍不理想 为了进一步提高效率 我们需要好好利用二分法查找 来找到第一次出现该元素和最后一次出现该元素时位置
       因而我们可以在O(log2^n)复杂度内找到给定数字在排序数组中出现的次数。
"""
class Solution:
    def GetNumberOfK(self, data, k):
        if data is None or len(data) == 0:
            return 0
        start = self.FindLastK(data, 0, len(data) - 1, k)
        if start == -1:
            return 0
        end = self.FindFirstK(data, 0, len(data) - 1, k)
        return start - end + 1

    def FindFirstK(self, data, left, right, k):
        while left <= right:
            middle = (left + right) // 2
            if k == data[middle]:
                if middle == 0 or (middle >= 1 and data[middle - 1] != k):
                    return middle
                else:
                    right = middle - 1
            elif k < data[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def FindLastK(self, data, left, right, k):
        while left <= right:
            middle = (left + right) // 2
            if k == data[middle]:
                if middle == len(data) - 1 or (middle < len(data) and data[middle + 1] != k):
                    return middle
                else:
                    left = middle + 1
            elif k < data[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1


s = Solution()
print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 7))
print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3))
print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 5))
print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 1))