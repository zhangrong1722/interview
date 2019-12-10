class Solution:
    def minimumTotal(self, triangle):
        """
        dynamic programing.
        :type triangle: List[List[int]]
        :rtype: int
        """
        w = len(triangle[-1])
        dp= [[float('inf') for _ in range(w)] for _ in range(w) ]
        dp[0][0] = triangle[0][0]
        for i in range(1, w):
            for j in range(len(triangle[i])):
                cur = dp[i-1][j] if j == 0 else min(dp[i-1][j], dp[i-1][j-1])
                dp[i][j] = triangle[i][j]+cur
        return min(dp[-1])