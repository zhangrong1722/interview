"""
题目：梳子序列中某一位的数字
     数字以012345678910111213...的格式序列化到一个字符序列中 在这个序列中 第5位（从0开始计数）是5 第13位是1 第19位是4等等 请写一个函数
     求任意n位对应的数字
思路：依旧是模仿coding_interview43.py中的思路 利用字符串的方式来降低算法复杂度 用一个字符串始终存储数字序列 按照0,1,2,3...序列依次添加到字符串
     中 直到字符串大于n 此时直接返回第n个位置元素即可
     最终算法复杂度为O(n)
"""
class Solution(object):
    def OneIntegerInSequence_Solution(self, n):
        if n is None or n < 0:
            return None
        sequences, num = '', 0
        while len(sequences) <= n:
            sequences += str(num)
            num += 1
        return int(sequences[n])

s = Solution()
print(s.OneIntegerInSequence_Solution(0))
print(s.OneIntegerInSequence_Solution(1))
print(s.OneIntegerInSequence_Solution(1000))
print(s.OneIntegerInSequence_Solution(5))
print(s.OneIntegerInSequence_Solution(13))
print(s.OneIntegerInSequence_Solution(19))
print(s.OneIntegerInSequence_Solution(None))