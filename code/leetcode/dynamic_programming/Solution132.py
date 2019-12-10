class Solution:
    def minCut(self, s):
        """
        assume dp[i][j] and min_cut[j] denotes whether substring s[i]~s[j] is partitioning and correspondingly min cutting if dp[i][j]=True.
        Obvious,j>=i.we need s[i]=s[j] and j-i>=1 or dp[i+1][j-1]=True such that s[i]~s[j] is partitioning.
        In this case,if j=0,it means s[i] and s[j] is adjacent.Hence,s[i]~s[j] is partitioning and min_cut[j]=0.
        Otherwise,it means s[i+1]~s[j-1] is partitioning.So we just need to consider s[0]~s[i-1] and min_cut[j]=min(m,min_cut[i-1]+1).
        :type s: str
        :rtype: int
        reference: https://leetcode.com/problems/palindrome-partitioning-ii/discuss/192705/Java-DP-with-my-understanding
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        min_cut = [0] * len(s)
        for i in range(len(s)):
            m = i
            for j in range(i+1):
                if s[i] == s[j] and (i - j <=1 or dp[j+1][i-1]):
                    dp[j][i]=True
                    if j == 0:
                        m = 0
                    else:
                        m = min(m, min_cut[j-1]+1)
            min_cut[i] = m
        return min_cut[len(s)-1]