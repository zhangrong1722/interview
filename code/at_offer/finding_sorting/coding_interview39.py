"""
题目：数组中出现次数超过一半的数字
     数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
     由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
思路一：可遍历整个数组 并且用字典记录每个元素出现的频率 然后再次遍历字典 如果出现频率超过一半 返回该元素 否则返回0 这是一种用空间换时间的做法
       时间复杂度为O(n) 空间复杂度为O(n)
思路二：如果某个元素出现的频率超过长度的元素 则排序之后 该元素必然出现在中间位置 在此我们借用Partition函数 每次运行该函数 便能排好一个元素
       如果该元素位置在中间位置 则为所找
思路三：如果一个元素出现的次数超过了长度的一半 则该元素出现的频率大于其他所有元素出现的次数之和 我们用一个key表示元素 times表示对应出现的频率
       遍历整个数组 如果出现的元素不是key 则times减1 如果是该元素 则times加1 如果times为0 则换一个元素 并重置times
"""
class Solution:
    def MoreThanHalfNum_Solution1(self, numbers):
        if len(numbers) == 0:
            return 0

        freq = dict()
        for e in numbers:
            if e not in freq.keys():
                freq[e] = 1
            else:
                freq[e] += 1
        for key, value in freq.items():
            if value > len(numbers)//2:
                return key
        return 0

    def MoreThanHalfNum_Solution2(self, numbers):
        if len(numbers) == 0:
            return 0
        start, end = 0, len(numbers) - 1
        index = self.Partition(numbers, start, end)
        while index != len(numbers) // 2:
            if index > len(numbers) // 2:
                index = self.Partition(numbers, start, index - 1)
            else:
                index = self.Partition(numbers, index + 1, end)
        if self.CheckValid(numbers, numbers[index]):
            return numbers[index]
        else:
            return 0

    def MoreThanHalfNum_Solution3(self, numbers):
        if len(numbers) == 0:
            return 0
        results, times = numbers[0], 1
        for i in range(1, len(numbers)):
            if times == 0:
                results, times = numbers[i], 1
            elif results == numbers[i]:
                times += 1
            else:
                times -= 1
        if self.CheckValid(numbers, results):
            return results
        else:
            return 0

    def Partition(self, numbers, start, end):
        key = numbers[start]

        while start < end:
            while start < end and key <= numbers[end]:
               end -= 1
            if key > numbers[end]:
                numbers[end], numbers[start] = numbers[start], numbers[end]

            while start < end and key >= numbers[start]:
                start += 1
            if key < numbers[start]:
                numbers[end], numbers[start] = numbers[start], numbers[end]
        return start

    def CheckValid(self, numbers, element):
        times = 0
        for e in numbers:
            if e == element:
                times += 1
        return times > len(numbers) // 2


s = Solution()
print(s.MoreThanHalfNum_Solution1([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(s.MoreThanHalfNum_Solution2([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(s.MoreThanHalfNum_Solution2([1, 2, 3, 6, 7, 9, 5, 4, 2]))

print(s.MoreThanHalfNum_Solution3([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(s.MoreThanHalfNum_Solution3([1, 2, 3, 6, 7, 9, 5, 4, 2]))