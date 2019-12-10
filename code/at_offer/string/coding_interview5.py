"""
题目：替换空格
请实现一个函数，把字符串中的每个空格替换成"%20"。例如，输入"We are happy."，则输出"We%20are%20happy."
"""
class Solution(object):

    def aux_space(self, string):
        """
        拿到题目，最简单的方式自然是依次遍历字符串，如果遇到空格，则将后面字符串都往后移动2个位置，再将以空格开始的三个字符替换为%20。该算法建立在
        字符串内存是无限制的，且算法复杂度相对较高，为O(n^2)。为了降低算法复杂度到线性复杂度，我们可以使用一个辅助数组，首先遍历一次原字符串，
        便能得到空格的个数，进而计算出辅助数组的长度，再遍历一次字符串，依次将原字符串复制到辅助数组即可。
        """
        nums = 0
        N = len(string)
        for i in range(N):
            if string[i] == ' ':
                nums += 1
        new_string = [' ']*(N + 2 * nums)

        p1, p2 = 0, 0
        while p1 < N:
            if string[p1] == ' ':
                new_string[p2] = '%'
                new_string[p2+1] = '2'
                new_string[p2+2] = '0'
                p2 += 3
            else:
                new_string[p2] = string[p1]
                p2 += 1
            p1 += 1
        return new_string


s = Solution()
print(s.aux_space('We are happy.'))