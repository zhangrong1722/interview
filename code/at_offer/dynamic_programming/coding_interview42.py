"""
问题：连续子数组的最大和
     HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
     当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
     连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
思路：动态规划 假设dp[i]表示以第i个元素结尾的连续子数组的最大和 则对于第i个元素 有两种策略 第一种策略是将第i个元素并入连续子数组序列中 此时dp[i]=dp[i-1]+array[i]
     否则不将第i个元素并入连续子数组序列 则将该元素作为起始序列 此时dp[i]=array[i]
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array is None or len(array) == 0:
            return None
        if len(array) == 1:
            return array[0]
        dp = [array[0]] * len(array)
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1] + array[i], array[i])
        return max(dp)

s = Solution()
print(s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))
print(s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))
print(s.FindGreatestSumOfSubArray([1, 2, 3, 4, 5, 6]))
print(s.FindGreatestSumOfSubArray([-1, -2, -3, -4, -5]))
print(s.FindGreatestSumOfSubArray(None))