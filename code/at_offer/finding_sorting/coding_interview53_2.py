"""
题目：0~n-1中缺失的数字
     一个长度为n-1的递增排序数组中的所有数字都是唯一的 并且每个数字都在范围0~n-1之内 在范围0~n-1内的n个数字中有且只有一个数字不在该数组中
     请找出这个数字
思路：最直观的方法是直接扫描整个数组 此时时间复杂度为O(n) 但是这样显然没有用好递增排序数组这一条件 对于递增排序数组条件 首先想到的就是二分法查找
     假设该数字所在位置为m 则在m位置之前 所有元素值和元素下标是相等的 换句话说 这道题就转化为查找第一个元素值和下标不等的元素
"""
class Solution(object):
    def FindMissingNum(self, data):
        if data is None or len(data) == 0:
            return -1
        left, right, middle = 0, len(data) - 1, 0
        while left <= right:
            middle = (left + right) // 2
            if data[middle] != middle:
                if middle == 0 or (middle - 1 >= 0 and data[middle - 1] == middle - 1):
                    break
                right = middle - 1
            else:
                left = middle + 1
        if middle == len(data) - 1:
            return -1
        else:
            return data[middle] - 1

s = Solution()
print(s.FindMissingNum([0, 1, 2, 3]))