import sys
class Solution(object):
    def __init__(self):
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.targetR, self.targetC = None, None
        self.cache = dict()

    def main(self, chars, n, m, startR, startC, endR, endC):
        """
        :param n: row nums
        :param m: col nums
        :return:
        """
        dp = [[0 for _ in range(m)] for _ in range(n)]
        try:
            for i in range(n):
                for j in range(m):
                    dp[i][j] = 1 if chars[i][j] == 'X' else 2
        except:
            print('this')
        self.targetR, self.targetC = endR, endC
        return self.dfs(startR, startC, dp, n, m)


    def dfs(self, startR, startC, dp, n, m):
        if (startR, startC, self.targetR, self.targetC) in self.cache:
            return self.cache[(startR, startC, self.targetR, self.targetC)]
        if 0 <= startR < n and 0 <= startC < m:
            if startR == self.targetR and startC == self.targetC and dp[startR][startC] == 0:
                return True
            for x, y in self.dir:
                if 0 <= startR + x< n and 0 <= startC + y< m and dp[startR + x][startC + y] >= 1:
                    dp[startR + x][startC + y] -= 1
                    if self.dfs(startR + x, startC + y, dp, n, m):
                        self.cache[(startR, startC, self.targetR, self.targetC)] = True
                        return True
                    dp[startR + x][startC + y] += 1
            self.cache[(startR, startC, self.targetR, self.targetC)] = False
            return False

        else:
            return False


if __name__ == '__main__':
    # chars = [['X', '.', '.', '.', 'X', 'X'],
    #          ['.', '.', '.', 'X', 'X', '.'],
    #          ['.', 'X', '.', '.', 'X', '.'],
    #          ['.', '.', '.', '.', '.', '.']]
    s = Solution()
    # print(s.main(chars, len(chars), len(chars[0]), 1 - 1, 6 - 1, 2- 1, 2 - 1))

    caseNums = int(sys.stdin.readline().strip())
    for _ in range(caseNums):
        line1 = list(map(int, sys.stdin.readline().strip().split()))
        n, m = line1[0], line1[1]
        chars = list()
        for _ in range(n):
            chars.append(list(sys.stdin.readline().strip()))

        line2 = list(map(int, sys.stdin.readline().strip().split()))
        line3 = list(map(int, sys.stdin.readline().strip().split()))
        startR, startC, endR, endC = line2[0] - 1, line2[1] - 1, line3[0] - 0, line3[0] - 0
        print('YES' if s.main(chars, n, m, startR, startC, endR, endC) else 'NO')