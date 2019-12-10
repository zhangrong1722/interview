
import sys
from bisect import bisect_left

def main(nums, n, m):
    res = 0
    for i in range(n):
        for j in range(m):
            res += 6 * nums[i][j] - 2 * (nums[i][j] - 1)
            if i - 1 >= 0:
                res -=  min(nums[i][j], nums[i - 1][j])
            if i + 1 < n:
                res -= min(nums[i][j], nums[i + 1][j])
            if j - 1 >= 0:
                res -=  min(nums[i][j], nums[i][j - 1])
            if j + 1 < m:
                res -=  min(nums[i][j], nums[i][j + 1])
    print(res)


if __name__ == '__main__':
    line = list(map(int, (sys.stdin.readline().strip().split())))
    n, m = line[0], line[1]

    nums = list()
    for _ in range(n):
        nums.append(list(map(int, sys.stdin.readline().strip().split())))

    main(nums, n, m)