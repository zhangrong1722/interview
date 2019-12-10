import random
import sys
# N0 NNNN0 NNNNNNNN0NNNN0NNNN

class Solution(object):

    def main(self, ss):
        if len(ss) - ss.count('N') <= 2:
            return len(ss)

        notNIndex = [index for index in range(len(ss)) if ss[index] != 'N']

        # 计算源字符串最大连续长度
        maxLens = 1
        dp = [1] * len(ss)
        for index in range(1, len(ss)):
            dp[index] = dp[index - 1] + 1 if ss[index] == ss[index - 1] else 1
            maxLens = max(maxLens, dp[index])

        # 动态规划
        res = [maxLens] * len(notNIndex)
        res[0], res[1] = max(maxLens, notNIndex[1]), max(maxLens, notNIndex[2])
        for index in range(2, len(notNIndex)):
            if index == len(notNIndex) - 1:
                end = len(ss)
            else:
                end = notNIndex[index + 1]
            res[index] = max(maxLens, end - notNIndex[index - 2] - 1, res[index - 1])
        return max(res)


    def solver(self, ss):
        l, nCounts, res = 0, 0, 0
        for r in range(len(ss)):
            if ss[r] == 'N':
                nCounts += 1
            while r - l + 1 - nCounts > 2:
                if ss[l] == 'N':
                    nCounts -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    chars = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'T', 'G', 'N', 'N', 'N', 'N', 'N', 'N']
    res1, res2 = list(), list()
    for _ in range(80):
        ss = list()
        for _ in range(random.randint(0, 10000)):
            ss.append(random.choice(chars))
        ss = ''.join(ss)
        # print(s.main('NGNNNNGNNNNNNNNSNNNN'), s.solver('NGNNNNGNNNNNNNNSNNNN'))
        # print(s.main('NGNNNNGNNNNTNNNSNNNN'), s.solver('NGNNNNGNNNNTNNNSNNNN'))
        res1.append(s.main(ss)), res2.append(s.solver(ss))
    print(res1)
    print(res1 == res2)

    # n = int(sys.stdin.readline().strip())
    # for _ in range(n):
    #     ss = sys.stdin.readline().strip()
    #     print(s.main(ss))