"""
链接：https://www.nowcoder.com/questionTerminal/46e837a4ea9144f5ad2021658cb54c4d
来源：牛客网

为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。


输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
"""
import sys


def main():
    lines = sys.stdin.readlines()
    lines = [l.strip().split() for l in lines if l.strip()]

    n, m = int(lines[0][0]), int(lines[0][1])
    res = [0] * (n + m)
    abilities = list(map(int, lines[-1]))
    maps = dict()

    for index, l in enumerate(lines[1:-1]):
        d, s = int(l[0]), int(l[1])
        maps[d] = s
        res[index] = d

    for index, ability in enumerate(abilities):
        res[index + n] = ability
        if ability not in maps:
            maps[ability] = 0
    res.sort()

    maxSalary = 0
    for index in range(n + m):
        maxSalary = max(maxSalary, maps[res[index]])
        maps[res[index]] = maxSalary

    for index in range(m):
        print(maps[abilities[index]])


if __name__ == '__main__':
    main()