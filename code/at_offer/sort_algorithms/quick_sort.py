"""
python 快速排序
快速排序在大量数据排序情况下表现最佳的一种排序方法 快速排序每一趟都能排好一个元素 算法复杂度为O(nlog2n) 下面以12,20,5,16,15,1,30,45,23,9演示其过程：
第一趟：12,20,5,16,15,1,30,45,23,9
       9 20 5 16 15 1 30 45 23 12
       9 12 5 16 15 1 30 45 23 20
       9 1  5 16 15 12 30 45 23 20
       9 1  5 12 15 16 30 45 23 20
第二趟：9 1  5 12 15 16 30 45 23 20
       5 1  9 12 15 16 30 45 23 20
第三趟：5 1  9 12 15 16 30 45 23 20
       1 5  9 12 15 16 30 45 23 20
第四趟：1 5  9 12 15 16 30 45 23 20
       1 5  9 12 15 16 23 45 30 20
       1 5  9 12 15 16 23 30 45 20
下面是python实现 关键函数是Partition 每次运行Partition 均能拍好一个元素 该元素不仅可用于快排 还能用于解决其他问题 例如：查找第k大元素 查找出现次数多余一般的元素
"""
class Solution(object):
    def QuickSort(self, arr, start, end):
        if arr is not list and len(arr) <= 1:
            return
        index = self.Partition(arr, start, end)
        if index > start:
            self.QuickSort(arr, start, index - 1)
        if index < end:
            self.QuickSort(arr, index + 1, end)

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
                arr[start], arr[end] = arr[end], arr[start]
        return start

arr = [12,20,5,16,15,1,30,45,23,9]
s = Solution()
s.QuickSort(arr, 0, len(arr) - 1)
print(arr)