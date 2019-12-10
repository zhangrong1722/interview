"""
题目：丑数
     把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路一：可以写一个函数判断一个整数是否是整数 接下来我们只需要依次查找即可 但是这种算法效率不是很高
思路二：我们可以用数组dp[i]表示第i个丑数 显然该数组是有序的 且第i个位置的丑数肯定是前面某个元素乘以2、3或者5得到 为求dp[i] 我们可以依次将所有前面所有位置元素都乘以2
      这里面肯定有比dp[i-1]小的 我们只关心第一个比dp[i-1]大的元素 记为M1 同理 我们将前面所有元素乘以3和5 我们将第一个比dp[i-1]的元素记为M2 M3
      显然 dp[i]=min(M1,M2,M3) 同样 我们在寻找M1、M2和M3的过程中存在重复计算 我们只需要记住上次位置即可
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index is None or index <= 1:
            return 1
        dp = [1] * index
        ugleNumberIndex2, ugleNumberIndex3, ugleNumberIndex5 = 1, 1, 1
        for i in range(1, index):
            dp[i] = min(ugleNumberIndex2 * 2, ugleNumberIndex3 * 3, ugleNumberIndex5 * 5)
            if dp[i] == ugleNumberIndex2 * 2:
                ugleNumberIndex2 += 1
            if dp[i] == ugleNumberIndex3 * 3:
                ugleNumberIndex3 += 1
            if dp[i] == ugleNumberIndex5 * 5:
                ugleNumberIndex5 += 1
        return dp[index - 1]

s = Solution()
print(s.GetUglyNumber_Solution(7))
print(s.GetUglyNumber_Solution(8))
print(s.GetUglyNumber_Solution(9))
print(s.GetUglyNumber_Solution(1500))
print(s.GetUglyNumber_Solution(1))
print(s.GetUglyNumber_Solution(0))

