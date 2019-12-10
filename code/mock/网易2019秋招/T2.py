import sys
from collections import defaultdict

def statisticsFreq(nums):
    res = list()
    for element in nums:
        cur = defaultdict(list)
        for value in element:
            cur[str(bin(value)).count('1')].append(value)
        res.append(len(list(cur.keys())))
    for kinds in res:
        print(kinds)


if __name__ == '__main__':
    nums = list()
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        counts = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        nums.append(list(map(int, line.split())))
    # statisticsFreq([[8, 3, 5, 7, 2]])
    statisticsFreq(nums)