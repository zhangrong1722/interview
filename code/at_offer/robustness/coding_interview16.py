"""
题目：数值的整数次方
思路：本题目最重要的是考虑到代码的鲁棒性，即考虑到底数为0，指数为0或者为负数情况
"""
class Solution:
    def Power(self, base, exponent):
        if base == 0.0:
            return 0.0
        if exponent == 0:
            return 1.0
        abs_exponent = abs(exponent)
        results = 1.0
        for _ in range(abs_exponent):
            results *= base
        if exponent < 0:
            return 1.0/results
        else:
            return results