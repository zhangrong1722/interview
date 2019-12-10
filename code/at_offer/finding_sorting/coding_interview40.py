"""
题目：最小的第k个数
     输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
思路：借助Partition函数 我们每次运行Partition函数将会排好一个元素的位置 如果该位置是倒数第k个元素 完成任务 另倒数第k个元素是第n-k+1个元素(n
     是数组长度)
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput is None:
            return -1
        lens = len(tinput)
        if k <= 0 or k > lens:
            return -1
        start, end = 0, lens - 1
        pos = self.Partition(tinput, start, end)
        while pos != lens - k:
            if pos < lens - k:
                pos = self.Partition(tinput, pos + 1, end)
            else:
                pos = self.Partition(tinput, start, pos - 1)
        return tinput[pos]

    def Partition(self, arr, start, end):
        key = arr[start]
        while start < end:
            while start < end and key <= arr[end]:
                end -= 1
            if key > arr[end]:
                arr[start], arr[end] = arr[end], arr[start]
            while start < end and key >= arr[start]:
                start += 1
            if key < arr[start]:
                arr[start], arr[end] = arr[end], arr[end]
        return start


s = Solution()
print(s.GetLeastNumbers_Solution([7, 5, 3, 2, 4, 1], 7))
print(s.GetLeastNumbers_Solution([7, 5, 3, 2, 4, 1], 1))
