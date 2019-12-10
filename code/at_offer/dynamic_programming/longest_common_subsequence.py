class Solution(object):
    def longset_common_subsequence(self, par, sub):
        """
        we let rows=len(sub)+1, cols=len(par)+1.And elements in the 1-st row and 1-st column are 0.
        assume dp[rows][cols] denote the longest common subsequence between par[:i+1] and sub[:j+1].Therefore,state transition equation is following:
        if par[i]==sub[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        Finally,dp[rows][cols] is desirable.Next we find correspondingly common subsequence.For example,the matrix dp is displayed above:
        [0, 0, 0, 0, 0, 0, 0]
        [0, 1, 1, 1, 1, 1, 1]
        [0, 1, 1, 2, 2, 2, 2]
        [0, 1, 2, 2, 2, 2, 2]
        [0, 1, 2, 3, 3, 3, 3]
        [0, 1, 2, 3, 3, 3, 4]
        And we start with the element dp[5][6] in the lower right corner.Obviously,
        if dp=max(dp[4][6], dp[5][5]),sub[5]!=par[6],we will go back to the position with max value.
        otherwise,it demonstrates sub[5]=par[6],which is common character.
        Similarly,the finding path is as follows: dp[5][6]->dp[4][5]->dp[4][4]->dp[4][3]->dp[3][2]->dp[2][1]->dp[1][1]->dp[0][0].
        And the common subsequence is 'abcf'.
        :param par:
        :param sub:
        :return:(common subsequence, length)
        reference: https://www.youtube.com/watch?v=NnD96abizww&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2
        """
        rows, cols = len(sub)+1, len(par)+1
        dp=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(1, rows):
            for j in range(1, cols):
                if sub[i-1] == par[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        i, k = rows-1, cols-1
        common_subsequence=[]
        while i >=0 and k >= 0:
            if max(dp[i-1][k], dp[i][k-1]) == dp[i][k] and dp[i-1][k] == dp[i][k]:
                i-=1
            elif max(dp[i-1][k], dp[i][k-1]) == dp[i][k] and dp[i][k-1] == dp[i][k]:
                k-=1
            else:
                common_subsequence.append(sub[i-1])
                i-=1
                k-=1
        return common_subsequence[::-1], dp[rows-1][cols-1],


s = Solution()
print(s.longset_common_subsequence(par="abcdaf", sub="acbcf"))