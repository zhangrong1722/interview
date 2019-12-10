import sys

def main(has, prices, n, money):
    minValue, maxValue = min(has), max(has) + money // min(has)
    for need in range(minValue, maxValue + 1):
        cur = money
        for ownIndex in range(len(has)):
            if need <= has[ownIndex]:
                cur -= 0
            else:
                cur -= (need - has[ownIndex]) * prices[ownIndex]
            if cur < 0:
                return need - 1
    return maxValue


if __name__ == '__main__':
    # print(main([2, 5, 3], [2, 1, 3], 3, 10))
    line = list(map(int, sys.stdin.readline().strip().split()))
    n, m = line[0], line[1]
    has = list(map(int, sys.stdin.readline().strip().split()))
    prices = list(map(int, sys.stdin.readline().strip().split()))
    print(main(has, prices, n, m))

