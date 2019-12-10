# import sys
# from collections import defaultdict
#
# def statisticsFreq(nums):
#     res = list()
#     for element in nums:
#         cur = defaultdict(list)
#         for value in element:
#             cur[str(bin(value)).count('1')].append(value)
#         res.append(len(list(cur.keys())))
#     for kinds in res:
#         print(kinds)
#
#
# if __name__ == '__main__':
#     nums = list()
#     n = int(sys.stdin.readline().strip())
#     for _ in range(n):
#         counts = int(sys.stdin.readline().strip())
#         line = sys.stdin.readline().strip()
#         nums.append(list(map(int, line.split())))
#     # statisticsFreq([[8, 3, 5, 7, 2]])
#     statisticsFreq(nums)





# 开始时 给水管 排水管 打开
# 每经过t1 给水管 开到闭 或者 闭到开 +m1
# 每经过t2 排水管 开到闭 或者 闭到开 -m2
# 泳池容量m

# m t m1 t1 m2 t2
# 10 2 1 5 2 5
import sys

def main(m, t, m1, t1, m2, t2):
    addTimeLeft, subTimeLeft, addTimeOpen, subTimeOpen = t1, t2, True, True
    res = 0
    for time in range(1, t + 1):
        if addTimeOpen:
            if addTimeLeft == 0:
                addTimeLeft = t1 - 1
                addTimeOpen = False
            else:
                res += m1
                addTimeLeft -= 1
        else:
            if addTimeLeft == 0:
                addTimeLeft = t1 - 1
                res += m1
                addTimeOpen = True
            else:
                addTimeLeft -= 1

        if subTimeOpen:
            if subTimeLeft == 0:
                subTimeLeft = t2 - 1
                subTimeOpen = False
            else:
                res -= m2
                subTimeLeft -= 1
        else:
            if subTimeLeft == 0:
                subTimeLeft = t2 - 1
                res -= m2
                subTimeOpen = True
            else:
                subTimeLeft -= 1
        if res < 0:
            res = 0
        if res > m:
            res = m
    return res

if __name__ == '__main__':
    # print(main(10, 2, 1, 5, 2, 5))
    # main(10, 2, 10, 5, 2, 5)
    # main(10,2, 3, 5, 2, 5)
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().strip().split()))
        print(main(line[0], line[1], line[2], line[3], line[4], line[5]))