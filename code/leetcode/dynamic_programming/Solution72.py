class Solution:
    def minDistance(self, word1, word2):
        """
        dynamic programming: dp[i][j] denote substring with the first i characters in word1 converts to substring with the first j characters in word2.
        For dp[i][j],we can acquire results from dp[i-1][j],dp[i][j-1] and dp[i-1][j-1] by deleting,inserting and replacing.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cols, rows = len(word2)+1, len(word1)+1
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dp[0]=[i for i in range(cols)]
        for i in range(1, rows):
            dp[i][0]=i
        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j-1]-1, dp[i-1][j], dp[i-1][j])
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[rows-1][cols-1]