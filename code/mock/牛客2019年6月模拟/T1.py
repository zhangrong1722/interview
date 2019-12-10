import sys

def main():
    ss = sys.stdin.readline().strip()
    print(solver(0, len(ss) - 1, ss))

def solver(l, r, ss):
    if l > r:
        return len(ss)

    if ss[l: r + 1] == ss[l: r + 1][::-1]:
        return r - l + 1

    if l == r:
        return 1

    if r - l == 1:
        return 1 if ss[r] == ss[l] else 2

    if ss[l] == ss[r]:
        return solver(l + 1, r - 1, ss)
    else:
        # left, right = solver(l + 1, r, ss), solver(l, r - 1, ss)
        # if (r - l) % 2 == 0:
        #     return min(left, right)
        # else:
        #     return min(left, right) + 1
        # if solver(l + 1, r, ss) == 1 or solver(l, r - 1, ss) == 1:
        #     return
        return min(solver(l + 1, r, ss), solver(l, r - 1, ss)) + 1

if __name__ == '__main__':
    main()