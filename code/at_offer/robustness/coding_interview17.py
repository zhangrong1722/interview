"""
题目：打印从1到最大的n位数
     输入数字n，按顺序打印从1到最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数999
思路：一拿到这道题目，首先想到的是求得最大的数字max，然后从1到max逐个打印；但是，若n比较大时，则可能造成溢出，例如32位整形，因而这个问题变成了一个大数问题，
    处理大数问题，我们首先得想到的是用字符串或者数组来处理。故，我们需要定义字符串的加法，这是比较麻烦的。
    另外一个思路是将该问题转化为0-9之间的全排列问题，我们可以通过递归解决；
"""
class Solution(object):
    def printNum(self, n):
        if n < 0:
            return
        results = []
        self.helper(results, n, 0)

    def helper(self, results, length, index):
        if index == length:
            self.printf(results)
            # print(results)
            return

        for i in range(10):
            results.append(str(i))
            self.helper(results, length, index + 1)
            results.pop()

    def printf(self, string):
        s = ''
        flag = False
        for e in string:
            if e != '0' or (e == '0' and flag):
                s += e
                flag = True
        if s == '':
            print(0)
        else:
            print(s)


s = Solution()
s.printNum(5)
s.printNum(-1)
