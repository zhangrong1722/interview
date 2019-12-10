import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    if n == 1:
        print(1)
        return
    print(solver(2, n, ['Y']))

def solver(pos, n, cur):
    if pos > n:
        return 1

    flag = True

    for i in range(2, int(pos ** 0.5) + 1):
        if cur[i - 1] == 'N' and pos % i == 0:
            flag = False
            break

    if flag:
        cur.append('N')
        res1 = solver(pos + 1, n, cur)
        cur.pop()

        cur.append('Y')
        res2 = solver(pos + 1, n, cur)
        cur.pop()
        return res1 + res2
    else:
        cur.append('N')
        res1 = solver(pos + 1, n, cur)
        cur.pop()
        return res1


if __name__ == '__main__':
    main()