class Solution:
    def knapsack(self, w, v, c):
        """
        dynamic programing:
        Given package space c,weights w and corresponding value v,we initialize a two-matrix dp with rows=len(w) and cols=c+1.
        Obvious,elements in the first column of matrix dp are equal to 0 because package(left space=0) can contains nothing.
        Hence,dp[i][j] denotes the max value of deciding i-th items and left space is equal to j.
        Therefore,given i-th item,if j>w[i], dp[i][j]=max{v[i]+dp[i-1][j-w[i]],dp[i-1][j]}.
        otherwise dp[i][j]=dp[i-1][j]
        Finally,return dp[len(w)-1][c].
        And we can know which items are selected by this matrix.For example,this matrix is displayed:
        [0, 1, 1, 1, 1, 1, 1, 1]
        [0, 1, 1, 4, 5, 5, 5, 5]
        [0, 1, 1, 4, 5, 6, 6, 9]
        [0, 1, 1, 4, 5, 7, 8, 9]
        As we known,element dp[3][7] is desirable.
        dp[2][7]=dp[3][7] isn't selected.And dp[2][7]!=dp[1][7] hence,2-nd item is selected.
        Hence we go back to dp[1][7-w[2]]=dp[1][3].dp[1][3]!=dp[0][3],i.e.,1-st item is also selected.
        Up to now,we can make a conclusion that selected items are 1-st and 2-nd items.
        :param w: items weight list
        :param v: corresponding items value list
        :return:
        reference: https://www.youtube.com/watch?v=8LusJS5-AGo&t=0s&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2
        """
        rows=len(w)
        dp = [[0 for _ in range(c+1)] for _ in range(rows)]
        for i in range(rows):
            for j in range(1, c+1):
                if j < w[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(v[i]+dp[i-1][j-w[i]], dp[i-1][j])
        print(dp[rows-1][c])
        k = c
        path = []
        i=rows-1
        while k > 0 and i>0:
            if dp[i][k] != dp[i-1][k]:
                k=k-w[i]
                path.append(i)
            i-=1
        print(path)

s = Solution()
s.knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7)