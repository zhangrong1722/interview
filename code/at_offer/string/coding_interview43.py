"""
题目：整数中1出现的次数（从1到整数n中1出现的次数）
     求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
     ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
思路：看到网上有个十分暴力的方式 直接将数字转为字符串 然后直接统计字符串中1出现的次数 这样的时间复杂度就为O(n) 例如n=11
       则需要得出1-11之间中1出现的次数 将每个整数转为字符串再拼接在一起为 1234567891011 接下来只需要统计该字符串中1出现的次数即可
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n <= 0:
            return 0
        ss, results = '', 0
        for i in range(1, n + 1):
            ss += str(i)
        for s in ss:
            if '1' in s:
                results += 1
        return results

s = Solution()
print(s.NumberOf1Between1AndN_Solution(1000))