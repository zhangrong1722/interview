"""
小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力的数量M(N<=M<=100000)。

输出描述:
输出一个数表示小Q第一天最多能吃多少块巧克力。
"""
# import sys
# import math

# def main():
#     line = list(map(int, sys.stdin.readline().strip().split()))
#     n, m = line[0], line[1]
#     res = 0
#     for x in range(m, 0, -1):
#         res = x
#         sums = x
#         for i in range(1, n):
#             if x == 1:
#                 sums += n - i
#                 break
#             x = math.ceil(x/2)
#             sums += x
#             if sums > m:
#                 break
#         if sums <= m:
#             break
#     print(res)
#
# if __name__ == '__main__':
#     main()

import sys
import math

def main():
    line = list(map(int, sys.stdin.readline().strip().split()))
    n, m = line[0], line[1]
    if n == 1:
        return m
    l, r = 1, m - 1

    while l < r:
        mid = (l + r + 1) // 2
        s = sums(mid, n)
        if s == m:
            return mid
        elif s < m:
            l = mid
        else:
            r = mid - 1
    return r

def sums(x, n):
    s = x
    for _ in range(n - 1):
        x = math.ceil(x / 2)
        s += x
    return s

if __name__ == '__main__':
    print(main())