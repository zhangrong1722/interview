"""
链接：https://www.nowcoder.com/questionTerminal/42e7ff5c5696445ab907caff17fc9e15
来源：牛客网


小Q的公司最近接到m个任务, 第i个任务需要xi的时间去完成, 难度等级为yi。
小Q拥有n台机器, 每台机器最长工作时间zi, 机器等级wi。
对于一个任务,它只能交由一台机器来完成, 如果安排给它的机器的最长工作时间小于任务需要的时间, 则不能完成,如果完成这个任务将获得200 * xi + 3 * yi收益。

对于一台机器,它一天只能完成一个任务, 如果它的机器等级小于安排给它的任务难度等级, 则不能完成。

小Q想在今天尽可能的去完成任务, 即完成的任务数量最大。如果有多种安排方案,小Q还想找到收益最大的那个方案。小Q需要你来帮助他计算一下。


输入描述:
输入包括N + M + 1行,
输入的第一行为两个正整数n和m(1 <= n, m <= 100000), 表示机器的数量和任务的数量。
接下来n行,每行两个整数zi和wi(0 < zi < 1000, 0 <= wi <= 100), 表示每台机器的最大工作时间和机器等级。
接下来的m行,每行两个整数xi和yi(0 < xi < 1000, 0 <= yi<= 100), 表示每个任务需要的完成时间和任务的难度等级。
"""
import sys


def main():
    line = list(map(int, sys.stdin.readline().strip().split()))
    n, m = line[0], line[1]
    tasks = list()
    machines = list()

    for _ in range(n):
        line = list(map(int, sys.stdin.readline().strip().split()))
        z, w = line[0], line[1]
        machines.append((z, w))

    for _ in range(m):
        line = list(map(int, sys.stdin.readline().strip().split()))
        x, y = line[0], line[1]
        tasks.append((x, y))
    machines.sort(key=lambda x: (x[0], x[1]), reverse=True)
    tasks.sort(key=lambda x: (x[0], x[1]), reverse=True)
    res, usedMachine = [0, 0], [False] * n

    # 算法复杂度过高 遍历存在冗余 实际上前面遍历过的机器工作时长都满足要求 因此接下来只需要关注等级 因为权重满足后续所有任务
    # for i in range(m):
    #     optimal = -1
    #     minWegiht = sys.maxsize
    #     for j in range(n):
    #         if not usedMachine[j] and machines[j][0] >= tasks[i][0] and machines[j][1] >= tasks[i][1] and machines[j][1] <= minWegiht:
    #             optimal = j
    #             minWegiht = machines[j][1]
    #     if optimal >= 0:
    #         usedMachine[optimal] = True
    #         res[0], res[1] = res[0] + 1, res[1] + 200 * tasks[i][0] + 3 * tasks[i][1]
    # print('%d %d' %(res[0], res[1]))

    j = 0
    cache = [0] * 101
    for i in range(m):
        while j < n and machines[j][0] >= tasks[i][0]:
            cache[machines[j][1]] += 1
            j += 1

        for k in range(tasks[i][1], 101):
            if cache[k] > 0:
                cache[k] -= 1
                res[0], res[1] = res[0] + 1, res[1] + 200 * tasks[i][0] + 3 * tasks[i][1]
                break

    print('%d %d' %(res[0], res[1]))

if __name__ == '__main__':
    main()