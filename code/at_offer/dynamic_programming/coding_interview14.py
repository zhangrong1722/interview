"""
题目：剪绳子
给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x..xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度为2、3、3的三段，此时得到的最大乘积是18.

解题思路：设f(n)表示绳子长度为n时能得到的最大乘积，我们可以将该问题分为两个子问题：f(m)和f(n-m),1<=m<=n-1，因此f(n)=max(f(m)*f(n-m)),1<=m<=n-1
        但是需要注意的是：由于m>1，所以在n=1，n=2，n=3时的最大乘积分别为0，1，2。但是在用动态规划计算n>=4时，前三个值却不能取这三个值，而应该按照m>=0时来计算，
        主要是m>=1和m>=0，在n<=3时得到的最大乘积不同，而当n>=4时，在m>=1和m>=0得到的最大乘积是相同的
"""

class Solution(object):
    def cuttingRope(self, length):
        """
        :param length:绳子长度
        """
        if length <= 1:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        dp = [0] * (length + 1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        for i in range(4, length + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[length]


s = Solution()
print(s.cuttingRope(10))
print(s.cuttingRope(3))

