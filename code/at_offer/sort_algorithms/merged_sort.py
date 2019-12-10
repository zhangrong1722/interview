"""
题目：归并排序
     归并排序是分为两步的 可用"分""治"两个步骤来形容 可用递归来实现 下面以[4,5,7,8,1,2,3,6]为例来演示其过程：
                    分：         [4,5,7,8,1,2,3,6]
                                /               \
                    分：      [4,5,7,8]         [1,2,3,6]
                            /       \         /        \
                    分：    [4,5]    [7,8]     [1,2]     [3,6]
                          /  \      / \      /   \     /   \
                    分：  4   5    7   8    1    2    3    6
                           /         \        /         \
                    治：  [4,5]     [7,8]     [1,2]     [3,6]
                               /                   \
                    治：      [4,5,7,8]            [1,2,3,6]
                                          /
                    治：          [1,2,3,4,5,6,7,8]
"""


class Solution(object):
    def MergeSort(self, left, right, arr, temp):
        if left < right:
            middle = (left + right) // 2
            self.MergeSort(left, middle, arr, temp)
            self.MergeSort(middle + 1, right, arr, temp)
            self.Merge(left, middle, right, arr, temp)

    def Test(self, arr):
        if arr is None or len(arr) == 0:
            return arr
        print('input:', arr)
        temp = [0] * len(arr)
        self.MergeSort(0, len(arr) - 1, arr, temp)
        print('result:', arr)

    def Merge(self, left, middle, right, arr, temp):
        i, j, k, m = left, middle + 1, right, left
        while i <= middle and j <= right:
            if arr[i] < arr[j]:
                temp[m] = arr[i]
                i, m = i + 1, m + 1
            else:
                temp[m] = arr[j]
                j, m = j + 1, m + 1
        while i <= middle:
            temp[m] = arr[i]
            m, i = m + 1, i + 1
        while j <= right:
            temp[m] = arr[j]
            m, j = m + 1, j + 1
        for n in range(left, right + 1):
            arr[n] = temp[n]


s = Solution()
s.Test([4, 5, 7, 8, 1, 2, 3, 6])
s.Test([7, 5, 6, 4])