"""
题目：礼物的最大价值
     在一个mxn的期盼的每一格都放有一个礼物 每个礼物有一定的价值（价值大于0） 你可以从棋盘的左上角开始拿格子里的礼物 并每次向右或者向下移动一格
      直到达到棋盘的右下角 给定一个棋盘及其上面的礼物 请计算你最多能拿到多少价值的礼物
思路：动态规划 动态规划方程 dp[i][j]=max(dp[i-1][j],dp[i][j-1])+arr[i][j]
"""


class Solution:
    def GetGiftMaxValue(self, arr):
        if arr is None or len(arr) == 0:
            return 0
        rows, cols = len(arr), len(arr[0])
        results = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                try:
                    results[i][j] = max(results[i - 1][j], results[i][j - 1]) + arr[i][j]
                except:
                    try:
                        results[i][j] = results[i - 1][j] + arr[i][j]
                    except:
                        try:
                            results[i][j] = results[i][j - 1] + arr[i][j]
                        except:
                            pass
        return results[rows - 1][cols - 1]


s = Solution()
print(s.GetGiftMaxValue([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]))
print(s.GetGiftMaxValue(None))
print(s.GetGiftMaxValue([[1, 4, 2]]))
print(s.GetGiftMaxValue([[1], [4], [2]]))
