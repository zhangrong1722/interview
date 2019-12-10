class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        Assume dp[i][j] denote whether substring of s1 and s2 with length=(i+1) and length=(j+1) can form substring of s3 with length=(i+j=1).
        And we need to consider two cases:
        (1)either s1[i-1] or s2[j-1] isn't equal to s3[i+j+1],we set dp[i][j]=False.
        (2)s1[i-1] or s2[j-1] is equal to s3[i+j+1],which means the interleaved string ends with s1[i-1] or s2[j-1].Hence,dp[i-1][j] or dp[i][j-1] needs to meet same property.
        summary: The issues related to string are likely to use 2D dynamic programming,e.g, longest common subsequence,subset summing.
        reference: https://leetcode.com/articles/interleaving-strings/
        """
        if len(s1) + len(s2) != len(s3):
            return False
        rows, cols = len(s1)+1, len(s2)+1
        dp= [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    dp[i][j]=True
                elif i == 0:
                    dp[i][j] = s2[j-1] == s3[i+j-1] and dp[i][j-1]
                elif j == 0:
                    dp[i][j] = s1[i-1] == s3[i+j-1] and dp[i-1][j]
                else:
                    dp[i][j] = (s2[j-1] == s3[i+j-1] and dp[i][j-1]) or (s1[i-1] == s3[i+j-1] and dp[i-1][j])
        return dp[rows-1][cols-1]
