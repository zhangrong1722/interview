import sys

def main():
    ss = sys.stdin.readline().strip()
    for i in range(len(ss) - 2, -1, -1):
        cur = ss[:i + 1]
        n = len(cur)
        if n % 2 == 0 and cur[: n // 2] == cur[n//2 :]:
            print(i + 1)
            break

if __name__ == '__main__':
    main()