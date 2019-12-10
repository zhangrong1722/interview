"""
链接：https://www.nowcoder.com/questionTerminal/fc72d3493d7e4be883e931d507352a4a
来源：牛客网

牛牛去犇犇老师家补课，出门的时候面向北方，但是现在他迷路了。虽然他手里有一张地图，但是他需要知道自己面向哪个方向，请你帮帮他。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示转方向的次数N(N<=1000)。
接下来的一行包含一个长度为N的字符串，由L和R组成，L表示向左转，R表示向右转。


输出描述:
输出牛牛最后面向的方向，N表示北，S表示南，E表示东，W表示西。
"""
import sys

def main():
    _ = int(sys.stdin.readline().strip())

    directions = sys.stdin.readline().strip()
    curPos = 'N'
    for d in directions:
        if curPos == 'N':
            curPos = 'W' if d == 'L' else 'E'
        elif curPos == 'S':
            curPos = 'E' if d == 'L' else 'W'
        elif curPos == 'W':
            curPos = 'S' if d == 'L' else 'N'
        else:
            curPos = 'N' if d == 'L' else 'S'
    return curPos

if __name__ == '__main__':
    print(main())