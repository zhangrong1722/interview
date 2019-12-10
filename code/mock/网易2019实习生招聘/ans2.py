"""
链接：https://www.nowcoder.com/questionTerminal/51dcb4eef6004f6f8f44d927463ad5e8
来源：牛客网

小Q得到一个神奇的数列: 1, 12, 123,...12345678910,1234567891011...。

并且小Q对于能否被3整除这个性质很感兴趣。

小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。


输入描述:
输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。


输出描述:
输出一个整数, 表示区间内能被3整除的数字个数。
"""
import sys

def exclude(x):
    return (x + 2) // 3

def main():
    line = sys.stdin.readline()
    line = list(map(int, line.strip().split()))
    l, r = line[0], line[1]

    print(r - l + 1 - (exclude(r) - exclude(l - 1)))


if __name__ == '__main__':
    main()