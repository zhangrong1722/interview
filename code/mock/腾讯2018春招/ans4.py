import sys

def main():
    k = int(sys.stdin.readline().strip())
    line = list(map(int, sys.stdin.readline().strip().split()))
    A, X, B, Y = line[0], line[1], line[2], line[3]
    musics = list()
    musics.extend([A] * X)
    musics.extend([B] * Y)
    print(solver(0, musics, k, dict()) % 1000000007)

def solver(pos, musics, cur, dp):
    if (pos, cur) in dp:
        return dp[(pos, cur)]

    if cur < 0:
        return 0
    if pos == len(musics):
        return 1 if cur == 0 else 0

    for index in range(pos, len(musics)):
        if (index + 1, cur - musics[index]) not in dp:
            dp[(index + 1, cur - musics[index])] = solver(index + 1, musics, cur - musics[index], dp)
        if (index + 1, cur) not in dp:
            dp[(index + 1, cur)] = solver(index + 1, musics, cur, dp)

        return dp[(index + 1, cur - musics[index])] + dp[(index + 1, cur)]

if __name__ == '__main__':
    main()