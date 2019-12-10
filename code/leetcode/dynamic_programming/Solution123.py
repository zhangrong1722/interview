class Solution:
    def maxProfit(self, prices):
        """
        Considering the fact we may complete at most two transactions.We can assume that first transaction is finished at i-th element.
        And we just need to cosider the subarry [:i] abd [i+1: lens],where the former and the latter represent the max value for subarray[:i] and subarray[i+1:len(prices)-1]
        :type prices: List[int]
        :rtype: int
        reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/200126/simple-c%2B%2B-DP-beats-99.66-with-explanation
        """
        if len(prices) <= 1:
            return 0
        left = [0] * len(prices)
        right = [0] * len(prices)
        min_prices, max_prices = prices[0], prices[-1]
        for i in range(1, len(prices)):
            min_prices = min(min_prices, prices[i])
            left[i] = max(prices[i]-min_prices, left[i-1])

        for j in range(len(prices)-2, -1, -1):
            max_prices = max(max_prices, prices[j])
            right[j] = max(max_prices - prices[j], right[j+1])
        results = [left[i]+right[i] for i in range(len(prices))]
        return max(results)