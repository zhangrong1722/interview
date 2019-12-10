class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        This problem can be solved by dynamic programming,which relies on the fact that the valid parentheses must end with character ')'.
        We can make use a dp array where i-th element in dp represents the longest valid parentheses ending with i-th element in target string.Hence,
        the length of the longest valid parentheses=max(dp).
        Obviously,dp[i]=0 if i-th element in target string = '('.We just need to deal with ')':
        (1)if s[i]=')' and s[i-1] = '('. dp[i]=dp[i-2]+2
        (2)if s[i]=')' and s[i-1] = ')'. the string looks like '....))'.
           if i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1]='(',which s[i-1] matches s[i-dp[i-1]-1].
           Therefore,the substring from (i-dp[i-1]-1)-th  to (i-1)-th is well-formed.
           Finally,dp[i]=2+dp[i-1]+dp[i-dp[i-1]-2]
        reference: https://leetcode.com/articles/longest-valid-parentheses/
        """
        if len(s) <= 1:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(dp)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i]=dp[i-2]+2 if i-2 >=0 else 2
            elif s[i] == ')' and s[i-1] ==')':
                if i - dp[i-1] -1 >=0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2 if i - dp[i-1] -2 >=0 else dp[i-1] + 2
        return max(dp)