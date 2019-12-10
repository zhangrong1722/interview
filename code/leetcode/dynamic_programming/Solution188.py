class Solution:
    def maxProfit_as_many_transactions(self, prices):
        if prices == []:
            return 0
        profit, prev = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                profit = profit + prices[i] - prices[i - 1]
        return profit

    def maxProfit(self, K, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        reference: # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54135/Python-solution-with-detailed-explanation
        we use 2D array dp[k][i] denotes max profile up to prices[i] at most k transactions.For acquiring dp[k][i],we have to consider prices[i].
        If we include it,dp[k][i]=[max(dp[k-1][j]+prices[i]-prices[j]) for j in range(0,i-1)],otherwise,dp[k][i]=dp[k][i-1].
        Therefore,dp[k][i]=max(dp[k][i-1],max[prices[i]+max(dp[k-1][j]-prices[j]) for j in range(0,i-1)])
        dp[k][0]=0
        dp[0][i]=0
        """
        if not prices:
            return 0
        K = min(K, len(prices) - 1)
        if K == 0:
            return 0
        if K >= len(prices) // 2:
            return self.maxProfit_as_many_transactions(prices)
        N = len(prices)
        dp = [[0] * N for _ in range(K + 1)]
        for k in range(1, K + 1):
            tmpMax = - prices[0]
            for i in range(1, N):
                dp[k][i] = max(dp[k][i - 1], prices[i] + tmpMax)
                # f[k, i] = max(f[k, i-1], price[i] + max(f[k-1, j-1]--price[j]))
                # max(f[k-1, j-1]--price[j]) => tmpMax
                tmpMax = max(tmpMax, dp[k - 1][i - 1] - prices[i])
        return dp[K][N - 1]
