# brute force
# import sys
# class Solution:
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1:
#             return 1
#         results = [1] * n
#         for i in range(1, n):
#             temp = sys.maxsize
#             for j in range(0, i):
#                 for factor in [2, 3, 5]:
#                     if results[j] * factor > results[i-1]:
#                         temp = min(results[j] * factor, temp)
#             results[i] = temp
#         return results[n-1]
# dynamic programming
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        1x2, 2x2, 3x2, 4x2, 5x2...
        1x3, 2x3, 3x3, 4x3, 5x3...
        1x5, 2x5, 3x5, 4x5, 5x5...
        reference: https://leetcode.com/problems/ugly-number-ii/discuss/206975/Javawonderful-solution
        """
        results = [1] * n
        next_uglg2, next_uglg3, next_uglg5 = 2, 3, 5
        index2, index3, index5 = 0, 0, 0
        for i in  range(1, n):
            results[i] = min(next_uglg2, next_uglg3, next_uglg5)
            if results[i] == next_uglg2:
                index2 += 1
                next_uglg2 = results[index2] * 2
            if results[i] == next_uglg3:
                index3 +=1
                next_uglg3 = results[index3] * 3
            if results[i] == next_uglg5:
                index5 +=1
                next_uglg5 = results[index5] * 5
        return results[n-1]
