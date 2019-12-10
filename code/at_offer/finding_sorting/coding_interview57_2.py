"""
题目：和为s的连续正数序列
     输入一个正数s 打印出所有和为s的连续正数序列（至少含两个数） 例如 输入15 由于1+2+...+8=15 哟所打印3个连续序列1~5 4~6 7~8
"""
class Solution(object):
    def FindequenceSumSS(self, s):
        if s <= 0:
            return
        small, middle, big = 1, (s + 1)//2, 2
        curSum = small + big
        while big <= middle:
            if curSum == s:
                self.PrintResult(small, big)
                big += 1
                curSum += big

            elif curSum < s:
                big += 1
                curSum += big
            else:
                curSum -= small
                small += 1

    def PrintResult(self, small, big):
        for i in range(small, big + 1):
            print(i, end=' ')
        print('')


s = Solution()
# 测试用例：含有多个组合
s.FindequenceSumSS(15)
s.FindequenceSumSS(100)
# 测试用例：不存在组合
s.FindequenceSumSS(4)
# 测试用例：边界条件 只有一个组合
s.FindequenceSumSS(3)