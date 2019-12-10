"""
链接：https://www.nowcoder.com/questionTerminal/6acc6504df67406c98a75f5575e4b94a
来源：牛客网

画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
小Q有他独特的绘画技巧,每次小Q会选择一条斜线, 如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;
如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数N和M(1 <= N, M <= 50), 表示画板的长宽。
接下来的N行包含N个长度为M的字符串, 其中包含字符'B','Y','G','X',分别表示蓝色,黄色,绿色,空白。整个表示小Q要完成的作品。

示例：

4 4
YXXB
XYGX
XBYY
BXXY

输出：3

"""
import sys

def main():
    line = list(map(int, sys.stdin.readline().strip().split()))
    n, m = line[0], line[1]
    chars = list()
    for _ in range(n):
        chars.append(list(sys.stdin.readline().strip()))
    steps = 0

    for i in range(n):
        for j in range(m):
            if chars[i][j] == 'B':
                paintBlue(chars, i, j, n, m)
                steps += 1
            elif chars[i][j] == 'Y':
                paintYellow(chars, i, j, n, m)
                steps += 1
            elif chars[i][j] == 'G':
                paintBlue(chars, i, j, n, m)
                paintYellow(chars, i, j, n, m)
                steps += 2
    print(steps)

def paintBlue(chars, i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m or chars[i][j] == 'X' or chars[i][j] == 'Y':
        return
    if chars[i][j] == 'B':
        chars[i][j] = 'X'
    elif chars[i][j] == 'G':
        chars[i][j] = 'Y'

    paintBlue(chars, i + 1, j - 1, n, m)

def paintYellow(chars, i, j, n, m):
    if i < 0 or i >=n or j < 0 or j >= m or chars[i][j] == 'X' or chars[i][j] == 'B':
        return
    if chars[i][j] == 'Y':
        chars[i][j] = 'X'
    elif chars[i][j] == 'G':
        chars[i][j] = 'B'

    paintYellow(chars, i + 1, j + 1, n, m)

if __name__ == '__main__':
    main()