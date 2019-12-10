class Solution(object):
    def subset_sum(self, subset, sum):
        """
        Note list subset and sum are in no decreasing order.
        :param subset:
        :param sum:
        :return:
        """
        rows = len(subset)
        dp = [[True if col==0 else False for col in range(sum+1)] for _ in  range(rows)]

        for i in range(rows):
            for j in range(1, sum+1):
                if j < subset[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-subset[i]] or dp[i-1][j]
        print(dp[rows-1][sum])

s = Solution()
s.subset_sum(subset=[2, 3, 7, 8, 10], sum=11)