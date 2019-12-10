"""
斐波那契数列
"""
class Solution(object):
    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def dy(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        m, k, results = 0, 1, 1
        for i in range(2, n+1):
            results = m + k
            m = k
            k = results
        return results


