"""
题目：和为s的数字
     输入一个递增排序的数组和一个数字 在数组中查找两个数 使得它们的和正好是s 如果有多对数字的和等于s 输出一堆即可
思路一：最直观的办法是用两层循环遍历 时间复杂度为O(n^2) 这种算法没有利用好排好序这个条件
思路二：看到拍好序的数组 很容易想到和二分法相关的算法 比如这道题 假设数组为{1,2,4,7,11,15}和数字15。设置left和right分别指向最小值和最大值
     如果指针之和大于15 则right指针-1 否则left指针+1 这样时间复杂度为线性复杂度
"""
class Solution:
    def FindSumS(self, data, k):
        if data is None or len(data) == 0:
            return False
        left, right = 0, len(data) - 1
        while left < right:
            if data[left] + data[right] == k:
                return True
            elif data[left] + data[right] < k:
                left += 1
            else:
                right -= 1
        return False