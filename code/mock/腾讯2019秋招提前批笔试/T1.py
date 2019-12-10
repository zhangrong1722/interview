import sys
from collections import deque

def main(nums, n, k):
    q = deque()
    res = [sys.maxsize] * (n - k + 1)
    cur, j, m = 0, 0, 0
    while j < k:
        q.append(nums[j])
        cur += nums[j]
        j += 1

    res[m] = cur
    minStartIndex = m
    m += 1
    for i in range(j, n):
        res[m] = cur + nums[i] - q.popleft()
        cur = res[m]
        if res[m] < res[minStartIndex]:
            minStartIndex = m
        m += 1
        q.append(nums[i])

    print(minStartIndex + 1)




if __name__ == '__main__':
    line = list(map(int, sys.stdin.readline().strip().split()))
    n, k = line[0], line[1]
    nums = list(map(int, sys.stdin.readline().strip().split()))
    # nums = [1, 2, 6, 1, 1, 7, 1]
    main(nums, len(nums), 3)