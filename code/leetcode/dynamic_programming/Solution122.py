class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        results = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                results += prices[i] - prices[i-1]
        return results