"""
题目：翻转字符串
     输入一个英文句子 翻转句子中单词的顺序 单单词内字符的顺序不变 为简单起见 标点符号和普通字符一样处理 例如输入字符 "I am a student."
     则输出"student. a am I"
思路：通过两次翻转完成该任务 先将整个字符翻转 变为".uneduts a ma I" 然后以空格为界 将各个单词翻转即可得到 "student. a am I"
"""


class Solution(object):
    def ReverseString(self, ss):
        if ss is None or len(ss) <= 1:
            return ss
        ss = ss[::-1]
        return ' '.join(s[::-1] for s in ss.split(' '))


s = Solution()
print(s.ReverseString('I am a student.'))
print(s.ReverseString('student.'))
print(s.ReverseString('   '))
