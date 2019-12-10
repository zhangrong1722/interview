# brute force: O(n^2)
# class Solution:
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1 or n == 2:
#             return n
#         results = [0] * (n + 1)
#         results[1], results[2] = 1, 2
#
#         for i in range(1, int(n ** 0.5) + 1):
#             results[i * i] = 1
#         if results[n] != 0:
#             return results[n]
#         for i in range(3, n + 1):
#             if results[i] == 0:
#                 min_numbers = i
#                 m, k = 1, i - 1
#                 while m <= k:
#                     min_numbers = min(min_numbers, results[m] + results[k])
#                     m += 1
#                     k -= 1
#                 results[i] = min_numbers
#         return results[n]

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        reference: https://leetcode.com/problems/perfect-squares/discuss/216296/python-DP-easy-to-understand
        """
        dp = [n] * (n + 1)
        dp[0] = 0
        choices = [x ** 2 for x in range(1, int(n ** 0.5) + 1)]
        for i in choices:
            for j in range(i, n + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[n]
