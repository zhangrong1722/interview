"""
链接：https://www.nowcoder.com/questionTerminal/bf877f837467488692be703735db84e6
来源：牛客网

牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。

输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。


输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
"""

# import sys
#
# def main():
#     line = list(map(int, sys.stdin.readline().strip().split()))
#     n, w = line[0], line[1]
#     v = list(map(int, sys.stdin.readline().strip().split()))
#     if sum(v) <= w:
#         print(2**n)
#         return
#     dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
#     for i in range(n + 1):
#         dp[i][0] = 1
#
#     for i in range(w + 1):
#         dp[0][i] = 1
#     for i in range(1, n + 1):
#         for j in range(1, w + 1):
#             dp[i][j] += dp[i - 1][j]
#             if j - v[i - 1] >= 0:
#                 dp[i][j] += dp[i - 1][j - v[i - 1]]
#     print(dp[-1][-1])
#
# if __name__ == '__main__':
#     main()

import sys

def solver(w, v, pos, dp):
    if (w, pos) in dp:
        return dp[(w, pos)]
    if w < 0:
        return 0
    if pos == len(v):
        return 1 if w >= 0 else 0
    else:
        if (w, pos + 1) not in dp:
            dp[(w, pos + 1)] = solver(w, v, pos + 1, dp)
        if (w - v[pos]) not in dp:
            dp[(w - v[pos], pos + 1)] = solver(w - v[pos], v, pos + 1, dp)
        dp[(w, pos)] = dp[(w, pos + 1)] + dp[(w - v[pos], pos + 1)]
        return dp[(w, pos)]

if __name__ == '__main__':

    line = list(map(int, sys.stdin.readline().strip().split()))
    n, w = line[0], line[1]
    v = list(map(int, sys.stdin.readline().strip().split()))
    if sum(v) <= w:
        print(2**n)
        exit(0)
    print(solver(w, v, 0, dict()))