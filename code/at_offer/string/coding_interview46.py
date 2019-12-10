"""
题目：把数字翻译成字符串
描述：给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”...25翻译成“z”。一个数字有多种翻译可能，
     例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。实现一个函数，用来计算一个数字有多少种不同的翻译方法。
     w x y z
思路：不难想到 这道题可以用递归解决 递归树如下：
                    12258
                /           \
            b+2258          l+258
              /   \          /  \
            bc+258 bw+58  lc+58  lz+8
              / \      /     /     /
        bcc+58  bcz+8 bwf+8 lcf+8 lzi
        /       /    /       /
    bccf+8    bczf  bwfi    lcfi
    /
  bccfi
  翻译结果分别为：bccfi、bczf、bwfi、lcfi和lzi共5中翻译结果
  然后可以看到自顶向下时 很多重复了的 因此效率不够高
  我们可以使用动态规划的思想去避免冗余：设dp[i]表示自i个元素到最右边元素子串的翻译可能数目
  递归方程为：dp[i]=dp[i+1]+g[i:i+1]dp[i+2]
  g[i:i+1]表示字符i-i+1是否在0-25之间 若在为1 否则为0
  对应递归和非递归实现如下
"""


class Solution(object):
    def GetTranslationCount_DPSolution(self, number):
        if number is None or number < 0:
            return 0
        number = list(str(number))
        # 只有一个元素时
        if len(number) == 1:
            return 1
        dp = [1] * (len(number))
        # 只有两个元素
        if len(number) == 2:
            if 0 <= int(number[-2] + number[-1]) <= 25:
                return 2
            return 1
        # 有两个元素及以上
        if 0 <= int(number[-2] + number[-1]) <= 25:
            dp[-2] = 2

        for i in range(len(number) - 3, -1, -1):
            if i + 1 < len(number):
                dp[i] = dp[i + 1]
            if i + 2 < len(number) and 0 <= int(number[i] + number[i + 1]) <= 25:
                dp[i] += dp[i + 2]
        return dp[0]

    def GetTranslationCount_RecursionSolution(self, number):
        if number is None or number < 0:
            return 0
        number = list(str(number))

        return self.helper(number, 0)

    def helper(self, number, index):
        # 达到最后一个位置之前
        if index + 1 < len(number):
            if 0 <= int(number[index] + number[index + 1]) <= 25:
                return self.helper(number, index + 1) + self.helper(number, index + 2)
            else:
                return self.helper(number, index + 1)
        # 达到最后位置 探测结束 返回1
        return 1


# 测试用例
s = Solution()
print(s.GetTranslationCount_DPSolution(12251))
print(s.GetTranslationCount_DPSolution(12221))
print(s.GetTranslationCount_DPSolution(-1))
print(s.GetTranslationCount_DPSolution(1234))
print(s.GetTranslationCount_DPSolution(9))
print(s.GetTranslationCount_DPSolution(None))

print(s.GetTranslationCount_RecursionSolution(12251))
print(s.GetTranslationCount_RecursionSolution(12221))
print(s.GetTranslationCount_RecursionSolution(-1))
print(s.GetTranslationCount_RecursionSolution(1234))
print(s.GetTranslationCount_RecursionSolution(9))
print(s.GetTranslationCount_RecursionSolution(None))
