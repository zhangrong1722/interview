"""
链接：https://www.nowcoder.com/questionTerminal/a22dd98b3d224f2bb89142f8acc2fe57
来源：牛客网

平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。

如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。

请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。


输入描述:
输入包括五行。
第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。
"""

import sys

def main(x1, y1, x2, y2, n):
    res = 0
    for x in x1 + x2:
        for y in y1 + y2:
            cur = 0
            for i in range(n):
                if x >= x1[i] and y >= y1[i] and x2[i] > x and y2[i] > y:
                    cur += 1
            res = max(res, cur)
    return res

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    x1 = list(map(int, sys.stdin.readline().strip().split()))
    y1 = list(map(int, sys.stdin.readline().strip().split()))
    x2 = list(map(int, sys.stdin.readline().strip().split()))
    y2 = list(map(int, sys.stdin.readline().strip().split()))
    print(main(x1, y1, x2, y2, n))