"""
题目：数组中的逆序对
     在数组中的两个数字 如果前面一个数字大于后面的数字 则这两个数字组成一个逆序对
     输入一个数组 求出这个数组中的逆序对的总数P 并将P对1000000007取模的结果输出 即输出P%1000000007
思路：借用二路归并排序思想 下面以输入{7,5,6,4}为例演示思路
                                    [7,5,6,4]
                                    /        \
                            分：   [7,5]     [6,4]
                                  /   \      /  \
                            分：  7    5     6   4
                                    /          \
                            合：   [5,7]      [4,6]               在合并排序过程中可得到两对逆序对(7,5) (6,4)
                                         /
                            合：         [4,5,6,7]                在合并排序过程中 可得到3组逆序对(7,6) (7,4)和(5,4)
     区别在于在合并时 两指针从逆序开始遍历 例如在合并[5,7]和[4,6]时 7(记为i指针)>6(记为j指针) 由于两部分各自有序 则可产生(j-middle)个逆序对
     并将data[i]赋给temp数组
     最终该算法时间复杂度为O(nlog2^n) 空间复杂度为O(n) 可以看做是以空间换时间
"""
class Solution:
    count = 0
    def InversePairs(self, data):
        if data is None or len(data) == 1:
            return 0
        if len(data) <=2:
            return 1
        temp,count = [0] * len(data), 0
        self.Helper(0, len(data) - 1, temp, data)
        print(data)
        return self.count

    def Helper(self, left, right, temp, data):
        if left < right:
            middle = (left + right) // 2
            self.Helper(left, middle, temp, data)
            self.Helper(middle + 1, right, temp, data)
            self.Merge(left, middle, right, temp, data)

    def Merge(self, left, middle, right, temp, data):
        i, j, k = middle, right, right

        while i >= left and j >= middle + 1:
            if data[i] > data[j]:
                self.count += j - middle
                temp[k] = data[i]
                i, k = i - 1, k - 1
            else:
                temp[k] = data[j]
                j, k = j - 1, k - 1

        while i >= left:
            temp[k] = data[i]
            i, k = i - 1, k + 1
        while j >= middle + 1:
            temp[k] = data[j]
            j, k = j - 1, k + 1

        for m in range(left, right + 1):
            data[m] = temp[m]

s = Solution()
print(s.InversePairs([7, 5, 6, 4]))