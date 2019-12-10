"""
题目：旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转，输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1
解题思路：看到递增排序的数组这一关键字，而且又是查找，因而可以联想到二分法查找，因此我们设置两个指针start和end，分别指向数组的开头和末尾，
        中间指针middle=(start+end)//2；按照旋转数组的定义，数组可分为两个各自递增排列的子数组，并且前面数组元素都大于后面数组元素；
        如果nums[start]<nums[middle]，说明start-middle序列是递增序列，此时最小元素在后半子序列中，令start=middle；
        如果nums[start]>nums[middle]，说明middle-end序列是递增序列，此时最小元素在前半部分，令end=middle
        以下以{3,4,5,1,2}为例进行说明：初始start=0，end=4，middle=(start + end) // 2=2
        (1)nums[start]=3<nums[middle]=5，因此最小元素在后半序列，令start=middle=2；
        (2)middle=(start+end)//2=3，nums[start]=5>nums[middle]=1，因此最小元素在前半部分，令end=middle=3
        (3)start=2，end=3，此时start指向前半递增序列的最后一个元素，end指向后半递增序列的第一个元素，也就是循环结束条件
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1 or len(rotateArray) == 2:
            return min(rotateArray)
        start, end = 0, len(rotateArray) - 1

        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                break
            middle = (start + end) // 2
            if rotateArray[start] <= rotateArray[middle]:
                start = middle
            if rotateArray[start] > rotateArray[middle]:
                end = middle

        return rotateArray[end]

s = Solution()
# print(s.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(s.minNumberInRotateArray([5, 6, 1, 2, 3, 4]))
