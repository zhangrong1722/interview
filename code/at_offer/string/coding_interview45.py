"""
题目：把数组排成最小的数字
     输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路：最简单最直接的方法自然用全排列得出所有的数字 然后比较得出其中的最小值 全排列的时间复杂度是n! 因此这种算法显得不太现实
     本题实际上求一个序列（证明见剑指offer面试题45）现在使用较简单的算法 设m和n分别为两个数字 我们自然选组合数字mn和nm中较小的一个 对于大数字
     我们自然可以想到用字符串比较 而又由于mn和nm两者的长度一致 因此可以直接
     使用Python中的'>'、'<'和'='来比较即可 最终时间复杂度为O(n) 排序比较好的办法是快排 这里为了代码书写方便 使用冒泡排序
"""
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers is None or len(numbers) == 0:
            return ''
        if len(numbers) == 1:
            return str(numbers[0])
        numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] > numbers[j] + numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(numbers)

s = Solution()
print(s.PrintMinNumber([3, 5, 1, 4, 2]))
print(s.PrintMinNumber([3, 32, 321]))
print(s.PrintMinNumber([3]))
print(s.PrintMinNumber(None))
