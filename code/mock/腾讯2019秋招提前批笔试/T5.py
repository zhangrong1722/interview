import sys

dirs = [[1, -1], [1, 0], [1, 1]]

def main(nums):
    res = 0
    cache = dict()

    visited = [[False for _ in range(3)] for _ in range(len(nums))]
    for i in range(3):
        visited[0][i] = True
        res = max(res, dfs(0, i, nums, cache, visited))
        visited[0][i] = False


def dfs(r, c, nums, cache, visted):
    if (r, c) in cache:
        return cache[(r, c)]
    if 0 <= r < len(nums) and 0 <= c < 3:
        for x, y in dirs:
            res = float('inf')
            if 0 <= r + x< len(nums) and 0 <= c + y < 3 and not visted[r + x][c + y]:
                if nums[r][c] == 0:
                    pass
                    # TODO
                    # visted[][]
                    # res =  max(res, -1 * dfs(r + x, c + y, cache, visted))
    else:
        return 0


if __name__ == '__main__':
    n = list(map(int, sys.stdin.readline().strip().split()))[0]
    nums = list()
    for _ in range(n):
        nums.append(list(map(int, sys.stdin.readline().strip().split())))
    main(nums)